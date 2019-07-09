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

# s.setblocking(False)
# connect to the server on local computer
msg = s.recv(1024)
time.sleep(0.5)
msg = pickle.loads(msg)
#msg = str(msg)
time.sleep(0.5)
print(f"recebido {msg}")

# close the connection
s.close()

#exit()


if(msg != "abort"):
	msg = msg.split(",")
	if(len(msg) < 2):
		print(type(msg[0]))  # CODIGO PARA CLIENTE QUE APENAS OPERA 1 DRONE
		mambo = Mambo(msg[0].rstrip(), use_wifi=False)
		success = mambo.connect(num_retries=5)
		print(success)
		if(success):
		# get the state information
			print("sleeping")
			mambo.smart_sleep(2)
			mambo.ask_for_state_update()
			mambo.smart_sleep(2)

			print("taking off!")
			mambo.safe_takeoff(5)

#			print("Flying direct: going forward (positive pitch)")
#			mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)

			mambo.smart_sleep(10)

			print("Showing turning (in place) using turn_degrees")
			mambo.turn_degrees(90)
			mambo.smart_sleep(2)
			mambo.turn_degrees(-90)
			mambo.smart_sleep(2)

#			print("Flying direct: yaw")
#			mambo.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0, duration=1)

#			print("Flying direct: going backwards (negative pitch)")
#			mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=0.5)

#			print("Flying direct: roll")
#			mambo.fly_direct(roll=50, pitch=0, yaw=0, vertical_movement=0, duration=1)

#			print("Flying direct: going up")
#			mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)

#			print("Flying direct: going around in a circle (yes you can mix roll, pitch, yaw in one command!)")
#			mambo.fly_direct(roll=25, pitch=0, yaw=50, vertical_movement=0, duration=3)

			mambo.smart_sleep(10)

			print("Showing turning (in place) using turn_degrees")
			mambo.turn_degrees(90)
			mambo.smart_sleep(2)
			mambo.turn_degrees(-90)
			mambo.smart_sleep(2)

			mambo.smart_sleep(10)

			print("landing")
			mambo.safe_land(5)
			mambo.smart_sleep(5)

			print("disconnect")
			mambo.disconnect()
            
else:
    print("there are no drones.\n you can rest now.")
    quit()
