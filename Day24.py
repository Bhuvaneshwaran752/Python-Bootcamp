#json data
import json
json_list_of_transactions = [
    {'amount': '0.05900000', 'date': '1521806276', 'tid': '59790535', 'type': '0', 'price': '8509.96'},
    {'amount': '0.04400000', 'date': '1521806270', 'tid': '59790528', 'type': '1', 'price': '8512.08'},
    {'amount': '0.03730108', 'date': '1521806268', 'tid': '59790527', 'type': '1', 'price': '8514.21'}]

json_list_of_transactions_dump=json.dumps(json_list_of_transactions)



#creating seperate database

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


#create seperate json table

import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhuv@n@123",
    database="json_records"

)
dbse=mydb.cursor()
dbse.execute("CREATE TABLE json3 (amount VARCHAR(255),date VARCHAR(255), tid VARCHAR(255), type VARCHAR(255), price VARCHAR(255))")

dbse=mydb.cursor()
dbse.execute("SHOW TABLES")
for entry in dbse:
    print(entry)

dbse = mydb.cursor()
dbse.execute("SHOW COLUMNS FROM json")
for entry in dbse:
  print(entry)


#import the JSON into a SQL Database


import mysql.connector as mysql
import json

json_list_of_transactions = [
    {'amount': '0.05900000', 'date': '1521806276', 'tid': '59790535', 'type': '0', 'price': '8509.96'},
    {'amount': '0.04400000', 'date': '1521806270', 'tid': '59790528', 'type': '1', 'price': '8512.08'},
    {'amount': '0.03730108', 'date': '1521806268', 'tid': '59790527', 'type': '1', 'price': '8514.21'}]
json_list_of_transactions_dump=json.dumps(json_list_of_transactions)
db = mysql.connect(
    user='root',
    password='Bhuv@n@123',
    host='localhost',
    database='json_records')

cursor = db.cursor()


transaction_sql = (
    "insert into json3"
    "(amount, date, tid, type, price)"
    "values (%(amount)s, %(date)s, %(tid)s, %(type)s, %(price)s)")

for transaction in json_list_of_transactions:
    cursor.execute(transaction_sql, transaction)


db.commit()

cursor.close()
db.close()



