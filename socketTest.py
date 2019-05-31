import socket
import pickle
import time

# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

# Define the port on which you want to connect 
port = 8881
msg = "nada"

s.connect(("10.0.6.163", port)) # IP UBI
#s.connect(("0.0.0.0", port))    # IP casa
print("conected!!")

# connect to the server on local computer 
while True:
        msg = s.recv(1024)
        time.sleep(0.5)
        msg = str(msg)
        print("recebido -%s-" % msg)
        if(msg != "abort" or msg != ['']):
		msg = msg.split(",")
		if( len(msg) < 2 ):
			print("is a string \"%s\"" % msg)
                	#CODIGO PARA CLIENTE QUE APENAS OPERA 1 DRONE
                	#
                	#
		else:
			print("is a list ||%s ||| %s|| " % (msg[0],msg[1]) )

        else:
                print("there are no drones.\n you can rest now." )
                s.close()
                quit()
# close the connection
s.close()	 
