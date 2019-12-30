#   Alarm.py
#   
#   Description
#       A class that determines whether or not the sensors are in the "danger 
#   zone". A sensor is in the danger zone when the battery and/or freshWater) is
#   low or  when grey water and/or black water tanks are almost full.

#--------------------------GlobalVariables--------------------------------------
alarmWindow = False
freshWtrState = False
greyWtrState = False
blackWtrState = False
batteryState = False
changeState = False

#-------------------------------------------------------------------------------
#   Method - getAlarmState
#
#    Description:
#       Determines if the alarm pop-up window is allowed.
#    Parameter:
#       Boolean alarm - if the alarm is on
#    Return:
#       Boolean turnOnWindow - if true if an alarm pop-up is allowed
def getAlarmState(alarm):
    #gets global variable
    global alarmWindow
    global changeState
 
    #initializes turnOnWindow variable
    turnOnWindow = False

    #if the alarm pop-up wind isn not open
    if not(alarmWindow):
        #if alarm is on and change state is true allow alarm window
        if alarm and changeState:
            alarmWindow = True
            turnOnWindow = True

    #return if the alarm pop-up window is allowed
    return turnOnWindow

#-------------------------------------------------------------------------------
#   Method - toString
#
#    Description:
#        Gets the string for the alram message pop-up window.
#    Parameter:
#        int freshWtrVal - fresh water percent value
#        int greyWtrVal - grey water percent value
#        int blackWtrVal - black water percent value
#        int battery - battery percent value
#    Return:
#        String freshWtrStr - a String message for fresh water
#        String greyWtrStr - a String message for grey water
#        String blackWtrStr - a String message for black water
#        String batteryStr  - a String message for battery
def toString( freshWtrVal,  greyWtrVal,  blackWtrVal,  batteryVal ):
    #initializes string variables
    freshWtrStr = ""
    greyWtrStr = ""
    blackWtrStr = ""
    batteryStr = ""

    print (freshWtrVal)
    print(greyWtrVal)
    print(blackWtrVal)
    print(batteryVal)
    #if any of the sensors are in the danger zone set sensor string
    if freshWtrVal <=20:
        freshWtrStr = "The fresh water tank is low at " + \
        str(freshWtrVal) + "%.\n"
    if greyWtrVal >=80:
       greyWtrStr= "The grey water tank is high at " + \
        str(greyWtrVal) + "%.\n"
    if blackWtrVal >=80:
        blackWtrStr = "The shitter's full at " + \
        str(blackWtrVal) + "%.\n"
    if batteryVal <=60:
        batteryStr = "Battery is running low at " \
        + str(batteryVal) + "%.\n"

    #return list of warning strings
    return freshWtrStr + greyWtrStr + blackWtrStr + batteryStr

#-------------------------------------------------------------------------------
#   Method - alarmActivation
#
#    Description:
#       Checks if any of the sensors are low. If the sensors have not changed
#       from their previous state they won't trigger the alarm pop-up window.
#    Parameter:
#        int freshWtrVal - fresh water percent value
#        int greyWtrVal - grey water percent value
#        int blackWtrVal - black water percent value
#        int battery - battery percent value
#    Return:
#        boolean - changeState - True if another sensor was activated
def alarmActivation(freshWtrVal,  greyWtrVal,  blackWtrVal,  batteryVal):
    #gets global variables
    global freshWtrState
    global greyWtrState
    global blackWtrState
    global batteryState
    global changeState

    #initializes variables
    freshWtr = False
    greyWtr = False
    blackWtr = False
    battery = False
    
    #Checks if any of the sensors are in their danger zone
    if freshWtrVal <=20:
        freshWtr = True
    if greyWtrVal >=80:
        greyWtr = True
    if blackWtrVal >=80:
        blackWtr = True
    if batteryVal <=60:
        battery = True

    #Checks if there has been a change in sensor states
    if not(freshWtrState == freshWtr) or not(greyWtrState == greyWtr) or \
        not(blackWtrState == blackWtr) or not(batteryState == battery):
             changeState = True
    #if sensors are all reading within good range resets alarm and change state
    if not(freshWtr) and not(greyWtr) and not(blackWtr) and not(battery):
        resetAlarm()
        changeState = False

    #sets the sensor states

    freshWtrState = freshWtr
    greyWtrState = greyWtr
    blackWtrState = blackWtr
    batteryState = battery

    #returnes change state
    return changeState

#-------------------------------------------------------------------------------
#   Method - resetAlarm
#
#    Description:
#       Resets the sensor and change state if all the sensors are okay.
#    Parameter:
#       Not Applicable
#    Return:
#       Not applicable  
def resetAlarm ():
    #gets global variables
    global freshWtrState
    global greyWtrState
    global blackWtrState
    global batteryState
    global changeState

    #sets all global to false    
    freshWtrState = False
    greyWtrState = False
    blackWtrState = False
    batteryState = False
    changeState = False

#-------------------------------------------------------------------------------
#   Method - resetWindow
#
#    Description:
#       Sets the alarmWindow to false, meaning the pop up window was closed.
#    Parameter:
#       Not applicable 
#    Return:
#        Not applicable  
def resetWindow():
    global alarmWindow
    alarmWindow = False
    
#-------------------------------------------------------------------------------
#   Method - getWindowState
#
#    Description:
#       Sends back if the alarm window is still open or closed
#    Parameter:
#       Not applicable 
#    Return:
#        boolean alarmWindow - returns true if alarm window is open   
def getWindowState():
    global alarmWindow
    return alarmWindow
