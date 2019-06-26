# grande Castro
import socket
import pickle
import time
from pyparrot.Minidrone import Mambo

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# GLOBAL
port = 8880
msg = "nada"
droneList = []
t = 0

#s.connect(("10.0.6.163", port))  # IP UBI my PC
#s.connect(("10.0.6.217", port))  # IP UBI my Rasp(082584)
s.connect(("0.0.0.0", port))    # IP local
print("conected!!")

# connect to the server on local computer
msg = s.recv(1024)
time.sleep(0.5)
msg = pickle.loads(msg)
#msg = str(msg)
time.sleep(0.5)
print(f"recebido {msg}")
if(msg != "abort"):
    msg = msg.split(",")
    if(len(msg) < 2):
        print(type(msg[0]))  # CODIGO PARA CLIENTE QUE APENAS OPERA 1 DRONE
        mambo = Mambo(msg[0].rstrip(), use_wifi=False)
        success = mambo.connect(num_retries=5)
        print(success)
        if(success):
            mambo.takeoff()
            mambo.smart_sleep(1)
            mambo.land()

    else:
        print("is a list ||%s ||| %s|| " %(msg[0].rstrip(),msg[1].rstrip()))
        mambo1 = Mambo(msg[0].rstrip(), use_wifi=False)
        mambo2 = Mambo(msg[1].rstrip(), use_wifi=False)
        success = mambo1.connect(num_retries=5)
        print(f"manbo 1 - {success}")
        if(success):
            success = mambo2.connect(num_retries=5)
            print(f"manbo 2 - {success}")
            if(success):
                mambo1.takeoff()
                mambo2.takeoff()
                mambo1.smart_sleep(1)
                mambo2.smart_sleep(1)
                mambo1.land()
                mambo2.land()
            
else:
    print("there are no drones.\n you can rest now.")
    s.close()
    quit()
# close the connection
s.close()
