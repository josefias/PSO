import socket
import pickle
import time
from pyparrot.Minidrone import Mambo

# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

# GLOBAL 
port = 8881
msg = "nada"
droneList = []

s.connect(("10.0.6.163", port)) # IP UBI
#s.connect(("0.0.0.0", port))    # IP casa
print("conected!!")

# connect to the server on local computer 
while True:
        msg = s.recv(1024)
        time.sleep(0.5)
        msg = str(msg)
        print("recebido -%s-" % msg)
        if(msg != "abort"):
		msg = msg.split(",")
		if( len(msg) < 2 ):
			print(type(msg[0]))
                	#CODIGO PARA CLIENTE QUE APENAS OPERA 1 DRONE
                	mambo = Mambo(msg[0] , use_wifi=False)
			success = mambo.connect(num_retries=5)
			print(success)
			if(success):
				mambo.takeoff()
				mambo.smart_sleep(1)
				mambo.land()
                	
		else:
			print("is a list ||%s ||| %s|| " % (msg[0],msg[1]) )
			mambo1 = Mambo(msg[0] , use_wifi=False)
			mambo2 = Mambo(msg[1] , use_wifi=False)
			success = mambo1.connect(num_retries=5)
			print(success)
			if(success):
				success = mambo2.connect(num_retries=2)
				print(success)
			if(success):
				mambo1.takeoff()
				mambo2.takeoff()
				mambo1.smart_sleep(1)
				mambo2.smart_sleep(1)
				mambo1.land()
				mambo2.land()			
        else:
                print("there are no drones.\n you can rest now." )
                s.close()
                quit()
# close the connection
s.close()	 
