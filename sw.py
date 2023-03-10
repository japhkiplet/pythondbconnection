import mysql.connector
# connecting to the database
dataBase = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "",
database = "SOFTWARE" )
# preparing a cursor object
cursorObject = dataBase.cursor()
# creating table
studentRecord = """CREATE TABLE EMPLOYEE (
ID INT NOT NULL,
NAME VARCHAR(60) NOT NULL,
AGE INT NOT NULL,
ADDRESS VARCHAR(60) NOT NULL,
SALARY DOUBLE NOT NULL,
PRIMARY KEY(ID)
)"""
# table created
cursorObject.execute(studentRecord)
# disconnecting from server
dataBase.close()
print("EMPLOYEE Table is Created in the Database")