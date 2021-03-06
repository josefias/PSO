"""
Find the BLE address for a mambo.  To run this,

sudo python findMambo.py

Note that the sudo is necessary for BLE permissions on linux.  It is only needed on
this program and nothing else.

Author: Amy McGovern
"""


try:
    from bluepy.btle import Scanner, DefaultDelegate
    BLEAvailable = True
except:
    BLEAvailable = False

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

def main():
    lista = []
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)
    fh = open("drones.txt","w")
    for dev in devices:
        #print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
        for (adtype, desc, value) in dev.getScanData():
            #print "  %s = %s" % (desc, value)
            if (desc == "Complete Local Name"):
                if ("Mambo" in value):
                    print("FOUND A MAMBO!")
                    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
                    print("  %s = %s" % (desc, value))
                    mamboName = value.split('_') 
                    mamboNum = mamboName[1]
                    lista.append( (dev.addr , mamboNum) )
                elif ("Swing" in value):
                    print("FOUND A SWING!")
                    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
                    print("  %s = %s" % (desc, value))
    print(f"temos {lista}")
    lista.sort(key = lambda tup: tup[1])
    print(f"temos2 {lista}")
    for address in lista:
        fh.writelines("%s\n" % address[0])
    fh.close()


if __name__ == "__main__":
    main()

