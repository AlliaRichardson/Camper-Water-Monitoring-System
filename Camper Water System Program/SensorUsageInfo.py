#-----------------------------imports-------------------------------------------
import piplates.DAQCplate as DAQC
#-------------------------------------------------------------------------------
#   Method getWaterUsage
#    Description:
#        Determines what percent of the sensor that was used, which
#        indicates the percentage in the tanks.
#    Parameters:
#        float empty - coltage the sensor gives for empty
#        float full - voltage the sensor gives for full
#        int channel - the daqc channel the sensor is on
#    Return:
#        int checkValue - returns the percentage of the voltage
def getWaterUsage(empty, full, channel):
    voltageInput = 0     #initialize sensorInput
    percent = 200      #initialize percUsed

    #while input is zero - zero means it didn't get a reading
    while voltageInput == 0:
        #try to get a reading
        try:
            #gets the voltage inut from the daqc board
            voltageInput = DAQC.getADC(0, channel)
            #if the voltage is greater than 0 it got a reading.
            if voltageInput > 0:
                #calculates the percentage
                percent = round(((empty + voltageInput)/(empty+full))*100)
            time.sleep(2)
        #If not voltage was read or it errored
        except:
            print("")
    #checkValue of the percentage bounds and than return it
    return checkValue(percent)

#-------------------------------------------------------------------------------
#   Method - getBattery()
#    Description:
#        Determines what percent of the sensor that was used, which
#        indicates the percentage in the tanks.
#    Parameters:
#        Not applicable
#    Return:
#        int checkValue - returns the percentage of the voltage
def getBattery():
    voltageInput = 0     #initialize sensorInput
    percent = 200      #initialize percent

    #while input is zero - zero means it didn't get a reading
    while voltageInput == 0:
        #try to get a reading
        try:
            #gets the voltage inut from the daqc board
            sensorInput = DAQC.getADC(0, 7)
            #print (sensorInput)
            #gets the voltage inut from the daqc board
            if sensorInput > 0:
                #calculates the percentage
                percent = round((sensorInput/5)*100)
                #print(percent)
            time.sleep(2)
        #If not voltage was read or it errored
        except:
            print("")
            exit()
    #checkValue of the percentage bounds and than return it
    return checkValue(percent)

#-------------------------------------------------------------------------------
#   Method - checkValue()
#    Description:
#        Checks to make sure that the percentage that was calculated is 
#        between 0 and 100
#    Parameters:
#        Not applicable
#    Return:
#        int percent - returns the percentage of the sensor
def checkValue(percent):
    if percent > 100:
        percent = 100
    if percent < 0:
        percent = 0
    return percent