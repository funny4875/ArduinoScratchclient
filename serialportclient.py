from scratchclient import ScratchSession
import time
import serial
try:
    serialPort = serial.Serial(port = 'COM6', baudrate=9600)
except: print('please check the Arduino connection');sys.exit()
while(True):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        T = serialString.decode().strip('\n').strip('\r')
        print(T)    
        serialPort.flush()
