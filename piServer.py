import socket
import time
import pickle
import threading


# GLOBAL
HEADERSIZE = 10
fh = open("drones.txt")
droneNum = 0

# FUNCTIONS
def sendData(cli , data):
    c , addr = cli
    msg = pickle.dumps(data) #codificar a data para bytes
    #msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg #
    c.sendall(msg)
    time.sleep(0.5)


### codigo necessario ao server

mamboAddr = fh.readlines()
fh.close()

print (mamboAddr)

droneNum = len(mamboAddr)


print("waiting for clients...")
piSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
piSocket.bind(('', 8880))
#piSocket.bind(('', 8881))

while True:
	piSocket.listen(5)
	c = piSocket.accept()

	print(f"Connection from {c} has been established.")


	# drones para os Clientes
	if(droneNum >= 1):
    		data = mamboAddr[0]
    		sendData(c,data)
    		mamboAddr.remove(mamboAddr[0])
    		droneNum = len (mamboAddr)
	else:
		print("NO MORE DRONES!")  
		data = "abort"
		sendData(c,data)
		#PF: atenção estou a carregar de novo a lista mas 
		#alguns endereços podem ainda estar em utilização...
		fh = open("drones.txt")
		mamboAddr = fh.readlines()
		droneNum = len(mamboAddr)
		print (mamboAddr)
		fh.close()
