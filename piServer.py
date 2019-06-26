import socket
import time
import pickle
import threading
from pyparrot.Minidrone import Mambo

# GLOBAL
HEADERSIZE = 10
fh = open("drones.txt")
droneNum = 0


# FUNCTIONS
def sendData(cli , data):
    c , addr = cli
    msg = pickle.dumps(data) #codificar a data para bytes
    #msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg #
    c.send(msg)
    time.sleep(0.5)

def controlMode(msg):
    '''
    Made by: joao P.
    TODO:
    controlar os drones em server side
    param: 'msg' can be str or tuple containing the ble mac
    '''
    print("we are in control mode")
    '''
    print("is a list ||%s ||| %s|| " % (msg[0], msg[1]))
    mambo1 = Mambo(msg[0], use_wifi=False)
    mambo2 = Mambo(msg[1], use_wifi=False)
    success = mambo1.connect(num_retries=5)
    print(success)
    if(success):
        success = mambo2.connect(num_retries=5)
        print(success)
    if(success):
        mambo1.takeoff()
        mambo2.takeoff()
        mambo1.smart_sleep(1)
        mambo2.smart_sleep(1)
        mambo1.land()
        mambo2.land()
    '''

### main ###

### codigo necessario ao server
piSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
piSocket.bind(('', 8880))
#piSocket.bind(('', 8881))
piSocket.listen(5)


mamboAddr = fh.readlines()
droneNum = len(mamboAddr)

print("waiting for clients...")
# now our endpoint knows about the OTHER endpoint.
c = piSocket.accept()

print(f"Connection from {c} has been established.")
###    
### Inserir codigo apartir daqui

## selecionamos 2 drone para o proprio server
myData = (mamboAddr[0],mamboAddr[1])
mamboAddr.remove(mamboAddr[0])
mamboAddr.remove(mamboAddr[0])
droneNum = len (mamboAddr)


# drones para os Clientes
if(droneNum >= 2):
    data = (mamboAddr[0],mamboAddr[1])
    sendData(c,data)
    mamboAddr.remove(mamboAddr[0])
    mamboAddr.remove(mamboAddr[0])
    droneNum = len (mamboAddr)
    #caso apenas exista 1 drone para este cliente então enviamos a String do mac    
elif(droneNum == 1):
    data = mamboAddr[0]
    sendData(c,data)
    mamboAddr.remove(mamboAddr[0])
    droneNum = len (mamboAddr)
else:
    print("NO MORE DRONES!")  
    data = "abort"
    sendData(c,data)
    
    
### ja enviamos os mas ao cliente
### agora podemos controlar
    
controlMode(myData)    

    
    
    
    
    