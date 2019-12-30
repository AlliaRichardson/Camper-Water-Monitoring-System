import piplates.DAQCplate as DAQC
import time

def getBlackWater():
    sensorInput = 0
    percUsed = 200
    while sensorInput == 0:
        try:
            sensorInput = DAQC.getADC(0, 2)
            if sensorInput > 0:
                percUsed = round(((3.5 - DAQC.getADC(0, 2))/(3.5-1.9))*100)
            time.sleep(2)
        except:
            print("")
    return percUsed
