
from pyparrot.Minidrone import Mambo
import threading
import time

def run(mambo):
    tot = 0
    avg = 0
    n = 0
    last = 0
    while True:
        speed = mambo.sensors.speed_x
        time = mambo.sensors.speed_ts
        if(speed == last):
            quit()
        n = n + 1
        tot = tot + speed
        avg = tot / n
        print(f"speed-{speed} | avg-{avg}")
        time.sleep(1)
        last = speed

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

# you will need to change this to the address of YOUR mambo
mamboAddr = "d0:3a:e3:53:e6:3a"

# make my mambo object
# remember to set True/False for the wifi depending on if you are 
mambo = Mambo(mamboAddr, use_wifi=False)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    mambo.smart_sleep(1)
    mambo.ask_for_state_update()
    mambo.smart_sleep(1)

    print("taking off!")
    mambo.takeoff()

    # enquanto o speed_ts == 0 esperar, pois os sensores ainda não responderam todos
    aux = 0
    while mambo.sensors.speed_ts == 0:
        mambo.smart_sleep(0.5)
        aux = aux + 1
        if(aux == 10):
            quit()
        print("remember shot 3 e 4")

    x = threading.Thread(target=go, args=(mambo,) )    
    x.start()

    mambo.fly_direct(0,40,0,0,1)
    mambo.smart_sleep(4)

    mambo.land()
    mambo.disconnect()