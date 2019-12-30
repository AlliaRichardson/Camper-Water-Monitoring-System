'''	Database.py
	
	Description:
		Stores the sensor's information into CamperWaterDB. It also returns 
		information about the stored information in the CamperWaterDB.
'''
#-----------------------------imports-------------------------------------------
import mysql.connector
from mysql.connector import Error
from datetime import datetime
#-------------------------------------------------------------------------------
def input(freshWater, greyWater, blackWater, battery):
	'''
		Description:
			Inputs fresh water, grey water, black water, and battery into the 
			database.
		Parameters:
			int freshWater - fresh water percent value
			int greyWater - grey water percent value
			int blackWater - black water percent value
			int battery - battery percent value
		Return:
			Not Applicable
	'''

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
        cursor = myConnection.cursor()
        #creates query
        query = "INSERT INTO CamperWaterDB.usageData" \
                "(DateTime, Fresh_Water, Grey_Water, Black_Water, Battery)" \
                "VALUES (%s, %s, %s, %s, %s)"
        #vals to be inserted
        val = (timestamp, freshWater, greyWater, blackWater, battery)
        #execute query
        cursor.execute(query, val)
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
def getGraphData():
	'''
		Description:
			Determines what percent of the sensor that was used, which
			indicates the percentage in the tanks.
		Parameters:
			freshWater : int - fresh water percent value
			greyWater : int - grey water percent value
			blackWater : int - black water percent value
			battery : int - battery percent value
		Return:
		   dateTimeArr : datetime - array of dateTimeArr
		   freshWaterArr : int - an array of fresh water data
		   greyWaterArr : int - an array of grey water data
		   blackWaterArr : int - an array of black water data
		   batteryArr : int - an array of battery data
	'''

    #Initialize variables as empty arrays
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
            "DateTime DESC"
        #buffered=True to avoid MySQL Unread result error
        cursor = myConnection.cursor(buffered=True) 
        cursor.execute(query)       #execute query
        fetching_size = 100         #number of tuple back
        #array of getched records
        records = cursor.fetchmany(fetching_size)
        
        i = 0   #initialize index incrementor  
        for row in records:
            #set index 1 as a datetime object
            dt_obj = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
            #set arrays to the appropriate values
            dateTimeArr.insert(i,  dt_obj)
            freshWaterArr.insert(i, row[1])
            greyWaterArr.insert(i, row[2])
            blackWaterArr.insert(i, row[3])
            batteryArr.insert(i, row[4])
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

    #returns the reverse of all arrays for graphing
    return dateTimeArr[::-1], freshWaterArr[::-1], \
        greyWaterArr[::-1], blackWaterArr[::-1], batteryArr[::-1]
