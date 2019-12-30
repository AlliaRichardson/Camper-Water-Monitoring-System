import mysql.connector
from mysql.connector import Error
from datetime import datetime

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

    #exception handling
    except Error as e :
        print ("Error while connecting to MySQL", e)
    #Closes the database
    finally:
        #closing database connection.
        if(myConnection.is_connected()):
            myConnection.close()


def sensorData():

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    usageIdArr = []
    dateTimeArr = []
    freshWaterArr = []
    greyWaterArr = [] 
    blackWaterArr = []
    batteryArr = []

    try:
        myConnection = mysql.connector.connect(
            host='localhost',    
            user='root',         
            passwd='raspberry',  
            db='CamperWaterDB') 

        sql_select_Query = "select * from CamperWaterDB.usageData ORDER BY usageDataID DESC"
        cursor = myConnection.cursor(buffered=True) #need to set buffered=True to avoid MySQL Unread result error
        cursor.execute(sql_select_Query)
        fetching_size = 100
        records = cursor.fetchmany(fetching_size)
        print("Total number of rows in python_developers is - ", cursor.rowcount)
        print ("Printing ", fetching_size, " developer record using cursor.fetchmany")
        i = 0    
        for row in records:
            date_str = row[1]
            dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            usageIdArr.insert(i, row[0])
            dateTimeArr.insert(i,  dt_obj)
            freshWaterArr.insert(i, row[2])
            greyWaterArr.insert(i, row[3])
            blackWaterArr.insert(i, row[4])
            batteryArr.insert(i, row[5])
            i = i + 1        
        cursor.close()
    
    #exception handling
    except Error as e :
        print ("Error while connecting to MySQL", e)

    #Closes the database
    finally:
        #closing database connection.
        if(myConnection.is_connected()):
            myConnection.close()
            print("connection is closed")

    #returns the reverse of all arrays for graphing
    return usageIdArr[::-1], dateTimeArr[::-1], freshWaterArr[::-1], greyWaterArr[::-1], blackWaterArr[::-1], batteryArr[::-1]


def lastInput (freshWaterVa,  greyWaterVal,  blackWaterVal,  batteryVal):
    return freshWaterVa,  greyWaterVal,  blackWaterVal,  batteryVal
