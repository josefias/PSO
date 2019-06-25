"""
Demo the direct flying for the python interface

Author: Amy McGovern
"""

from pyparrot.Minidrone import Mambo
import time
import threading
droneList = []


def go(mambo):
    last = (111,0,0)
    while True:
        mambo.updateXYZ()
        pos = mambo.getXYZ()
        if(pos == last):
               quit()
        print(pos)
        time.sleep(0.6)
        last = pos


def swarmAssemble():
    global droneList
    fh = open("drones.txt")
    mamboAddr = fh.readlines()

    # CONNECT TO ALL DRONES
    for droneAddr in mamboAddr:
        mambo = Mambo(droneAddr.strip(), use_wifi=False)
        print("trying to connect 1")
        success = mambo.connect(num_retries=3)
        droneList.append(mambo)
        print("connected: %s" % success)

    fh.close()


def swarmTakeoff():
    global droneList
    # TAKE OFF
    for drone in droneList:
        #i = 0
        print("sleeping")
       # drone.smart_sleep(1)
       # drone.ask_for_state_update()
        drone.smart_sleep(1)
        print("taking off")
        drone.takeoff()
        
        drone.smart_sleep(1)
        while(drone.sensors.speed_ts == 0):
            print("wait for speed sensor")
            drone.smart_sleep(0.1)
        #drone.sensors.quaternion_y = i
        #i = i + 1
        drone.updateXYZ()
        


def swarmLand():
    global droneList
    for drone in droneList:
        drone.smart_sleep(1)
        drone.land()


def swarmDisconnect():
    global droneList
    for drone in droneList:
        drone.smart_sleep(1)
        drone.disconnect()


def main():
    global droneList

    swarmAssemble()
    swarmTakeoff()
    
    for drone in droneList:
         x = threading.Thread(target=go, args=(drone,) )    
         x.start()
        
    for drone in droneList:
        y = threading.Thread( target=drone.GoTo , args=(1,0,0,))
        y.start()
        #print("aqui estamos (%.3f,%.3f,%.3f)" % drone.getXYZ() )
    
    swarmLand()
    swarmDisconnect()


if __name__ == "__main__":
    main()
