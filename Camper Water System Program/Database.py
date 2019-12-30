#-----------------------------imports-------------------------------------------
import mysql.connector
from mysql.connector import Error
from datetime import datetime
#-------------------------------------------------------------------------------
#   Method input
#    Description:
#        Inputs fresh water, grey water, black water, and battery into the 
#        database.
#    Parameters:
#        int freshWater - fresh water percent value
#        int freshWater - fresh water percent value
#        int freshWater - fresh water percent value
#        int freshWater - fresh water percent value
#    Return:
#        Not Applicable
def input(freshWater, greyWater, blackWater, battery):
    #get the current time
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #try to make a connection
    try:
        #connects to the mySQL database
        myConnection = mysql.connector.connect(
        host='localhost',    
         user='root',         
         passwd='raspberry',  
         db='CamperWaterDB') 

        #creates cursor
        cur = myConnection.cursor()
        #creates query
        query = "INSERT INTO CamperWaterDB.usageData" \
                "(DateTime, Fresh_Water, Grey_Water, Black_Water, Battery)" \
                "VALUES (%s, %s, %s, %s, %s)"
        #vals to be inserted
        val = (timestamp, freshWater, greyWater, blackWater, battery)
        #execute query
        cur.execute(query, val)
        #commit changes to query
        myConnection.commit()

    #connection failed
    except Error as e :
        print ("Error while connecting to MySQL", e)
    #Closes the database
    finally:
        #closing database connection.
        if(myConnection.is_connected()):
            myConnection.close()


#-------------------------------------------------------------------------------
#   Method getWaterUsage
#    Description:
#        Determines what percent of the sensor that was used, which
#        indicates the percentage in the tanks.
#    Parameters:
#        int freshWater - fresh water percent value
#        int freshWater - fresh water percent value
#        int freshWater - fresh water percent value
#        int freshWater - fresh water percent value
#    Return:
#       int usageIdArr - an array of the id for tuple
#       datetime dateTimeArr - array of dateTimeArr
#       int freshWaterArr - an array of fresh water data
#       int greyWaterArr - an array of grey water data
#       int blackWaterArr - an array of black water data
#       int batteryArr - an array of battery data
def sensorData():
    #Initialize variables as empty arrays
    usageIdArr = []
    dateTimeArr = []
    freshWaterArr = []
    greyWaterArr = [] 
    blackWaterArr = []
    batteryArr = []

    #try to connect to database
    try:
        myConnection = mysql.connector.connect(
            host='localhost',    
            user='root',         
            passwd='raspberry',  
            db='CamperWaterDB') 

        #what will be queried in the database
        query = "select * from CamperWaterDB.usageData ORDER BY " + \
            "usageDataID DESC"
        #buffered=True to avoid MySQL Unread result error
        cursor = myConnection.cursor(buffered=True) 
        cursor.execute(query)       #execute query
        fetching_size = 100         #number of tuple back
        #array of getched records
        records = cursor.fetchmany(fetching_size)
        
        i = 0   #initialize index incrementor  
        for row in records:
            #set index 1 as a datetime object
            dt_obj = datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
            #set arrays to the appropriate values
            usageIdArr.insert(i, row[0])
            dateTimeArr.insert(i,  dt_obj)
            freshWaterArr.insert(i, row[2])
            greyWaterArr.insert(i, row[3])
            blackWaterArr.insert(i, row[4])
            batteryArr.insert(i, row[5])
            i = i + 1  #increment index number      
        cursor.close()
    
    #connection failed
    except Error as e :
        print ("Error while connecting to MySQL", e)

    #Closes the database
    finally:
        #closing database connection.
        if(myConnection.is_connected()):
            myConnection.close()
            print("connection is closed")

    #returns the reverse of all arrays for graphing
    return usageIdArr[::-1], dateTimeArr[::-1], freshWaterArr[::-1], \
        greyWaterArr[::-1], blackWaterArr[::-1], batteryArr[::-1]



#-------------------------------------------------------------------------------
def lastInput (freshWaterVa,  greyWaterVal,  blackWaterVal,  batteryVal):
    return freshWaterVa,  greyWaterVal,  blackWaterVal,  batteryVal
