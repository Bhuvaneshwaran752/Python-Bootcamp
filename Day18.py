#1.	Create a DB with doctor and doctor ID & patients visited

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhuv@n@123",
  database="mydatabase"


)
dbse=mydb.cursor()
dbse.execute("CREATE TABLE Doctor (Doctor_name VARCHAR(255),Doctor_ID VARCHAR(255),Patients_visited VARCHAR(255))")

mycursor = mydb.cursor()

sql = "INSERT INTO Doctor (Doctor_name,Doctor_ID,Patients_visited) VALUES (%s,%s,%s)"
val = [
  ('ragnar lothbrok','12345', '6'),
  ('walter white','23456', '0'),
  ('jaime lanister','34567', '4'),
  ('pablo escobar','45678', '9'),
  ('harshad mehta','56789', '0'),
  ('jessie pinkman','67890', '4'),
  ('micheal scofield','78901', '0'),
  ('lincoln burrows','78902', '0'),
  ('sucre','78903', '3'),
  ('jon snow','78904', '7')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctor")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#2.	Get the doctor(s) who have more than 5 patients visited

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhuv@n@123",
  database="mydatabase"


)
mycursor = mydb.cursor()
mycursor.execute("SELECT Doctor_name FROM Doctor WHERE Patients_visited >= 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#3.	Get the doctors with no patients visit

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhuv@n@123",
  database="mydatabase"


)
mycursor = mydb.cursor()
mycursor.execute("SELECT Doctor_name FROM Doctor WHERE Patients_visited = 0")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)