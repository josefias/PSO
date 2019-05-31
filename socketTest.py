# Import socket module 
import socket
import pickle
import time

# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

# Define the port on which you want to connect 
port = 8881
aux  = 0
s.connect(("10.0.6.163", port))
print("conected to 10.0.6.163")
# connect to the server on local computer 
while(aux < 11):
        strs = s.recv(1024)
        strs = pickle.loads(strs)
        print(aux,strs)
        aux = aux + 1
        time.sleep(2)
# receive data from the server 
#strs = b'client data' 

# close the connection
s.close()	 
