import serial
import syslog
import time
import pickle
look = []

port = '/dev/ttyACM0'


ard = serial.Serial(port,9600,timeout=5)

try:
    while True:
        ard.flush()
        time.sleep(.1)

        msg = ard.readline()
        look.append(msg)
except KeyboardInterrupt:
    pkl_file = open('data.pkl', 'wb')
    pickle.dump(msg, pkl_file)

#import serial
#ser = serial.Serial('/dev/ttyACM0')  # open serial port
#print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
#ser.close()             # close port
