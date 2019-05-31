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
        msg = pickle.loads(msg)
        print("recebido -%s-" % msg)
        if(msg != "abort"):
                if(isinstance(msg , str)):
                        msg = msg.rstrip() #retirar um \n que vem com a string
                        print("is a string \"{%s}\"" % msg)
                        #CODIGO PARA CLIENTE QUE APENAS OPERA 1 DRONE
                        #
                        #

                if(isinstance(msg , tuple)):
                        print("is a tuple \"{%s}\"" % msg) 
                        #CODIGO PARA CLIENTE QUE OPERA 2 DRONES
                        #
                        #
        else:
                print("there are no drones.\n you can rest now.")
                s.close()
                quit()
# close the connection
s.close()	 
