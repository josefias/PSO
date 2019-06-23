"""
Demo the direct flying for the python interface

Author: Amy McGovern
"""

from pyparrot.Minidrone import Mambo

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
    while mambo.sensors.speed_ts == 0:
        mambo.smart_sleep(0.5)
        print("remember shot 3 e 4")
    # primas vai ser o primeiro time Stamp (/1000 para converter em Segundos)
    primas = mambo.sensors.speed_ts/1000
    print(primas)
    # print da velocidade antes de arrancar
    print("v= %f"% mambo.sensors.speed_x)
    
    mambo.fly_direct(0,40,0,0,1)
    mambo.smart_sleep(0.3)
    # retirar a segunda velocidade
    vel = mambo.sensors.speed_x
    # retirar o tempo depois da deslocação ter terminado
    primas = mambo.sensors.speed_ts/1000 -primas
    
    print(primas)
    print("v= %f"  % vel)
    d = vel*primas
    print("distancia = %f" % d)

    mambo.smart_sleep(0.3)
    mambo.land()
    mambo.smart_sleep(2)
    print( d , vel , primas )

    mambo.smart_sleep(2)
    mambo.takeoff()
    mambo.smart_sleep(1)
    mambo.fly_direct(0,-30,0,0,1)
    mambo.smart_sleep(1)
    mambo.land()

    print("disconnect")
    mambo.disconnect()