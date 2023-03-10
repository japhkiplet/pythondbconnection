import mysql.connector
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = "SOFTWARE"
)
mycursor = mydb.cursor()
sql = "INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) VALUES (%s, %s, %s, %s,%s)"

val = [("100", "Joy","23" , "Nakuru", "98000"),
("101", "Wanyonyi", "34", "Busia", "70000"),
("102", "Oletutu", "52","Kajiado", "34600"),
("103", "Akinyi", "40", "Nakuru","74900"),
("104", "Salat", "29", "Garissa", "84200"),
("105", "Wanjiru", "25", "Njoro", "97400")]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "details inserted")
# disconnecting from server
mydb.close()