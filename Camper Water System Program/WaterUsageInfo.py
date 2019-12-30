
import piplates.DAQCplate as DAQC

def getWaterUsage(empty, full, channel):
    sensorInput = 0
    percUsed = 200
    while sensorInput == 0:
        try:
            sensorInput = DAQC.getADC(0, channel)
            print("sensor")
            print(sensorInput)
            if sensorInput > 0:
                percUsed = round(((empty - DAQC.getADC(0, channel))/(empty-full))*100)
            time.sleep(1)
        except:
            print("")
    return checkValue(percUsed)

def checkValue(percUsed):
    if percUsed > 100:
        percUsed = 100
    if percUsed < 0:
        percUsed = 0
    return percUsed

