from scratchclient import ScratchSession
import time
import serial
COMport = "COM8"
projectID = 718312829
username = "ccsh_ky";password = "123456987"
try:
    serialPort = serial.Serial(port = COMport, baudrate=9600)
except: print('please check the Arduino connection');sys.exit()

session = ScratchSession(username, password)
connection = session.create_cloud_connection(projectID)

@connection.on("set")
def on_set(variable):
    global serialPort          
    if variable.name=="☁ D5_W":
        try:
            if serialPort.writable():
                print(variable.name, variable.value)
                serialPort.write(bytes([int(variable.value)]))                                
        except:print('write error')
lastV = 0    
while(True):
    samples=[]
    for i in range(10):
        if(serialPort.in_waiting > 0):
            serialString = serialPort.readline()
            T = serialString.decode().strip('\n').strip('\r')
            if len(T)>0:samples.append(int(T))
        else:break  
    if len(samples)==0:serialPort.flush();continue
    V=int(sum(samples)/len(samples))    
    if lastV!= V:
        connection.set_cloud_variable("A0_R", V)
        print('write to scratch3 cloud variable A0_R=',V) 
    lastV = V
    serialPort.flush()
