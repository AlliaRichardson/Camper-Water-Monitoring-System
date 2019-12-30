#-----------------------------imports-------------------------------------------
import piplates.DAQCplate as DAQC
#-------------------------------------------------------------------------------
#   Method getPercentage
#    Description:
#        Determines what percent of the sensor that was used, which
#        indicates the percentage in the tanks.
#    Parameters:
#        float empty - coltage the sensor gives for empty
#        float full - voltage the sensor gives for full
#        int channel - the daqc channel the sensor is on
#    Return:
#        int checkValue - returns the percentage of the voltage
def getPercentage(empty, full, channel, typeSensor):
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
                if typeSensor == 'W':
				    percent = round(((empty - voltageInput)/(empty-full))*100)
                elif typeSensor == 'B':
                    percent = round((sensorInput/5)*100)
			time.sleep(1)
        #If not voltage was read or it errored
		except:
			print("")
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
