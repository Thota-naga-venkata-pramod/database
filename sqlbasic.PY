import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="pramod", passwd="Mysql_password4",auth_plugin="mysql_native_password",database="demo")
print(mydb)
mycursor=mydb.cursor()



mycursor.execute("CREATE DATABASE first")                                                       #for creating database
mycursor.execute("SHOW DATABASES")                                                              #command for showing all the databases
for x in mycursor:                                                                              #printing all the databases one by one
   print(x)

    
    
mycursor.execute("CREATE TABLE DATA(name varchar(25),address varchar(25))")                     #creating  a table "data"
mycursor.execute("SHOW TABLES")                                                                 #command for showing all the tables
for x in mycursor:                                                                              #printing all the tables
   print(x)


    
x="INSERT INTO DATA(name,address)VALUES(%s,%s)"                                                 #inserting the column names to the table of a database
details=("pramod","vijayawada")                                                                 #inserting values for a particular columns
mycursor.execute(x,details)




mycursor.execute("SELECT* FROM DATA")                                                           #command used to select the table
result=mycursor.fetchall()                                                                      #fetching all the values in a particular table
for x in result:
     print(x)


    
y="SELECT* FROM DATA WHERE address='vijayawada'"                                                #selecting a particular values(or)rows where the address is vijayawada
mydb.commit()



y="UPDATE DATA SET address='chennai' WHERE address='vijayawada'"  #upadating the values
mycursor.execute(y)
mydb.commit()

