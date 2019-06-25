import socket
import time
import pickle
import threading
from pyparrot.Minidrone import Mambo

droneList = []
HEADERSIZE = 10
fh = open("drones.txt")



def sendData(cli , data):
    c , addr = cli
    if(isinstance(data,tuple)):
        print(f"thread sendData({data}) to -{addr}")
    elif(isinstance(data,str)):
        print(f"thread sendData({data.rstrip()}) to -{addr}")
    msg = pickle.dumps(data)
    #msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg #
    c.send(msg)
    time.sleep(0.5)


### codigo necessario ao server
piSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#piSocket.bind(('', 8880))
piSocket.bind(('', 8881))
piSocket.listen(5)
cliList = []

mamboAddr = fh.readlines()
droneNum = len(mamboAddr)
aux = 0

while True:
    # now our endpoint knows about the OTHER endpoint.
    cPi1, addressPi1 = piSocket.accept()
    cliList.append( (cPi1,addressPi1) )
    print(f"Connection from {addressPi1} has been established. {len(cliList)}")
    ###    
    ### Inserir codigo apartir daqui    
    

    if(len(cliList) >= 3): # espera por 3 clientes
            for c in cliList: # distribui os mac address dos drones pelos clientes
                #caso ajam 2 drones enviamos um tuplo com ambos os mac's
                if(droneNum >= 2):
                    data = (mamboAddr[0],mamboAddr[1])
                    x = threading.Thread(target=sendData, args=(c,data))
                    mamboAddr.remove(mamboAddr[0])
                    mamboAddr.remove(mamboAddr[0])
                    droneNum = len (mamboAddr)
                    x.start()
                #caso apenas exista 1 drone para este cliente então enviamos a String do mac    
                elif(droneNum == 1):
                    data = mamboAddr[0]
                    x = threading.Thread(target=sendData, args=(c,data))
                    mamboAddr.remove(mamboAddr[0])
                    droneNum = len (mamboAddr)
                    x.start()
                else:
                    print("NO MORE DRONES!")  
                    data = "abort"
                    x = threading.Thread(target=sendData, args=(c,data))
                    x.start()      
   