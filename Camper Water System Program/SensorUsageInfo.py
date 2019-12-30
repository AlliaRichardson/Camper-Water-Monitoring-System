#   SensorUsageInfo.py
#-----------------------------imports-------------------------------------------
import piplates.DAQCplate as DAQC
#import time
#-------------------------------------------------------------------------------
def getSensorPercentage(empty, full, channel, typeSensor):
	'''
    Description:
        Determines what percent of the sensor that was used, which
        indicates the percentage in the tanks.
    Parameters:
        empty : float - coltage the sensor gives for empty
        full : float - voltage the sensor gives for full
        channel : int - the daqc channel the sensor is on
    Return:
        checkValue : int - returns the percentage of the voltage
	'''
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
				#calculates the percentage for water
                if typeSensor == 'W':
                    percent = round(((empty - voltageInput)/(empty-full))*100)
                #calculates the percentage for the battery
				elif typeSensor == 'B':
                    percent = round((voltageInput/5)*100)
            #time.sleep(1)
        #If not voltage was read or it errored
        except:
            print("")
    #checkValue of the percentage bounds and than return it
    return checkValueBounds(percent)

#-------------------------------------------------------------------------------
def checkValueBounds(percent):
	'''
		Description:
			Checks to make sure that the percentage that was calculated is 
			between 0 and 100
		Parameters:
			Not applicable
		Return:
			percent : int - returns the percentage of the sensor
	'''
    if percent > 100:
        percent = 100
    if percent < 0:
        percent = 0
    return percent
    
def soundTheAlarm(state):
	'''
		Description:
			Recieves the voltage input from the DACQ board to determine if the	
			alarm needs to go on or off.
		Parameters:
			state : char - 'c' for Cancel alarm, or 's' Sound alarm
		Return:
			percent : int - returns the percentage of the sensor
	'''
    #try to get a reading, and get the voltage input from the daqc board
    try:
        #Allows voltage to go through to turn off the alarm
        if state == 'c':
            DAQC.clrDOUTbit(0, 0)
		#Allows voltage to go through to turn on the alarm
        if state == 's':
            DAQC.setDOUTbit(0, 0)
    #If not voltage was read or it errored
    except:
        print("")
#checkValue of the percentage bounds and than return it