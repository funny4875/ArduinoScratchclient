#dowload scratchclient: 
#pip install scratchclient
from scratchclient import ScratchSession
import time
import serial
import sys
COMport = ""
username = ""
password = ""
projectID = 0
uploadVariable = ""
downloadVariable = ""


if len(sys.argv) < 7:
    print('Need 6 arguments==> argv[1...5]\COMport username password projectID uploadVariable downloadVariable')
    sys.exit()
else: COMport,username,password,projectID,uploadVariable,downloadVariable = sys.argv[1:]

try:
    serialPort = serial.Serial(port = COMport, baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except: print('please check the Arduino connection');sys.exit()

session = ScratchSession(username, password)
connection = session.create_cloud_connection(projectID)

#connection.set_cloud_variable("x", "123456")

@connection.on("set")
def on_set(variable):
    global serialPort          
    if variable.name[2:]==downloadVariable:
        try:
            if serialPort.writable():
                #print(variable.name, variable.value)
                serialPort.write(bytes([int(variable.value)]))                                
        except:print('write error')
    
while(True):
    samples=[]
    for i in range(10):
        if(serialPort.in_waiting > 0):
            serialString = serialPort.readline()
            T = serialString.decode().strip('\n').strip('\r')
            if len(T)>0:samples.append(int(T))
        else:break
    
    if len(samples)==0:serialPort.flush();continue
    V =0
    if not 0 in samples:
        V=int(sum(samples)/len(samples))
    print('write to scratch3 cloud variable',uploadVariable,"=",V)
    connection.set_cloud_variable(uploadVariable, V)
    serialPort.flush()
    



