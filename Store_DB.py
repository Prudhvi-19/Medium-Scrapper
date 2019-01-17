"""Store_DB takes values from Scrape and Stores them in Database"""

#importing required libraries to connect python with database
import mysql.connector

def store_db(title,subtitle,content,s,claps,author,author_bio,post_date,read_time):

    #Connecting to Database
    mydb = mysql.connector.connect(host='127.0.0.1',user="root",passwd="root",database="MEDS")

    mycursor = mydb.cursor()

    #Getting Already Stored Values to check whether article already exist or not
    sql_query = "SELECT * FROM Article"
    mycursor.execute(sql_query)
    records = mycursor.fetchall()

    flagdata = 0
    
    #Checking if database exist in Data Base so that we can Update
    for row in records:
        if row[1] == title:
            flagdata = 1
            break

    #If flagdata is 0 it means we got new url we need to insert data in to Data Base
    if (flagdata == 0):
        sql = "INSERT INTO Article (Title,Subtitle,Content,Image_links,Claps,Author,Author_bio,Post_created,Avg_Read_Time)" "VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )"
        val = (title,subtitle,content,s,claps,author,author_bio,post_date,read_time)
    
    #If flagdata is 1 it means article already exist and link is given again to update Data Base
    if (flagdata == 1):
        sql = """UPDATE Article 
                SET Title = %s,Subtitle= %s,Content=%s,Image_links=%s,Claps=%s,Author=%s,Author_bio=%s,Post_created=%s,Avg_Read_Time=%s 
                WHERE Title = %s"""
        val = (title,subtitle,content,s,claps,author,author_bio,post_date,read_time,title)
    
    #Commiting and Closing Connection with Data Base
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
