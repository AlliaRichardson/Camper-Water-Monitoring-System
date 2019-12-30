import piplates.DAQCplate as DAQC

def getFreshWater():
    sensorInput = 0
    percUsed = 200
    while sensorInput == 0:
        try:
            sensorInput = DAQC.getADC(0, 0)
            if sensorInput > 0:
                percUsed = round((3.55(DAQC.getADC(0, 0))/(3.55-2.3))*100)
            time.sleep(2)
        except:
            print("")
    return percUsed
