#creationg a databse employee management

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhuv@n@123",

)
mycursor=mydb.cursor()
print(mydb)

dbse=mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)

#creating a table employee in employee_management database

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhuv@n@123",
    database="employee_management"

)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE employee1 (Employee_id VARCHAR(255), Employee_name VARCHAR(255) ,Employee_salary VARCHAR(255))")


dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for entry in dbse:
    print(entry)

#inserting values in employee table

dbse = mydb.cursor()

sql = "INSERT INTO Employee1 (emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
('1001', 'DUSTIN', '10000.0'),
    ('1002', 'STEVE', '15000.0'),
    ('1003', 'JON', '70800.0'),
    ('1004', 'BARGHAV', '80000.0'),
    ('1005', 'ROLLO', '89000.0'),
    ('1006', 'FLOKI', '50000.0'),
    ('1007', 'JORAH', '56000.0'),
    ('1008', 'DANEYREUS', '47000.0'),
    ('1009', 'CERSEI', '26000.0'),
    ('1010', 'JAMIE', '15000.0'),
    ('1011', 'TRIYION', '50500.0'),
    ('1012', 'MICHEAL', '40500.0'),
    ('1013', 'SCOFEILD', '25000.0'),
    ('1014', 'SARA', '20500.0'),
    ('1015', 'HANNAH', '100600.0')

]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "records were inserted.")

#a. Write a query to get the maximum and minimum salary from employees table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhuv@n@123",
    database="employee_management"
)


dbse = mydb.cursor()

dbse.execute("SELECT EMP_NAME, EMP_SALARY FROM Employee1 where EMP_SALARY = (select max(EMP_SALARY) from Employee1)")

myresult = dbse.fetchall()

for i in myresult:
    print(i)

dbse = mydb.cursor()

dbse.execute("SELECT EMP_NAME,EMP_SALARY FROM Employee1 where EMP_SALARY = (select min(EMP_SALARY) from Employee1)")

myresult = dbse.fetchall()

for i in myresult:
    print(i)


#b. Write a query to get the number of employees working with the company

dbse = mydb.cursor()

dbse.execute("SELECT COUNT(*) from Employee1")

myresult = dbse.fetchall()

for i in myresult:
    print(i)

#c. Write a query to get the first 3 characters of first name from employees table

dbse=mydb.cursor()
dbse.execute("SELECT * FROM Employee1 WHERE EMP_NAME LIKE('TRI%')")
myresult = dbse.fetchall()

for i in myresult:
    print(i)



