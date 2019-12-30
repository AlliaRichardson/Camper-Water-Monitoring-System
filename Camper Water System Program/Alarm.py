import Database

alarmWindow = False
alarmState = False

def getAlarmState(alarm):
    global alarmWindow
    global alarmState
    if alarm and not(alarmWindow):
        alarmWindow = True
        alarmState = True
    elif alarm and alarmWindow:
        alarmState = False
    return alarmState

def toString():
    freshWaterStr = ""
    greyWaterStr = ""
    blackWaterStr = ""
    batteryStr = ""
    freshWaterVal,  greyWaterVal,  blackWaterVal,  batteryVal = \
        Database.lastInput()
    if freshWaterVal <=20:
        freshWaterStr = "The fresh water tank is low at " + str(freshWaterVal) + "%.\n"
    if greyWaterVal >=80:
        greyWaterStr = "The grey water tank is high at " + str(greyWaterVal) + "%.\n"
    if blackWaterVal >=80:
        blackWaterStr = "The shitter's full at " + str(blackWaterVal) + "%.\n"
    if batteryVal <=60:
        batteryStr = "Battery is running low at " + str(batteryVal) + "%.\n"

    return freshWaterStr + greyWaterStr + blackWaterStr + batteryStr

def alarmActivation():
    alarmActivate = False
    alarmChange = False
    if freshWaterVal <=20:
        if 
    if greyWaterVal >=80:
    if blackWaterVal >=80:
    if batteryVal <=60:
    if alarmChange == True:
        alarmActive = True

    return AlarmActive

def resetWindow():
    global alarmWindow
    alarmWindow = False
