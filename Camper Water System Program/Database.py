import mysql.connector

def input(freshWater, greyWater, blackWater, battery):
    db = mysql.connector.connect(
    host='localhost',    
     user='root',         
     passwd='raspberry',  
     db='CamperWaterDB') 

    cur = db.cursor()

    sqlStat = "INSERT INTO CamperWaterDB.usageData (Fresh_Water, Grey_Water, Black_Water, Battery) VALUES (%s, %s, %s, %s)"
    val = (freshWater, greyWater, blackWater, battery)
    cur.execute(sqlStat, val)
    db.commit()
    print(cur.rowcount, "record inserted.")
