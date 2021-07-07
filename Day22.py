#1. Read a jpeg image and print the image file
from PIL import Image
img = Image.open("pyimage.jpg")
print(img.format)

import matplotlib.pyplot as plt
plt.imshow(img)

#2.	Merge two pdf files using python script

import PyPDF2
pdf1 = PyPDF2.PdfFileReader(open('sample1.pdf','rb'))
pdf2 = PyPDF2.PdfFileReader(open('sample2.pdf','rb'))
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdf1.numPages):
    pageObj = pdf1.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf1.numPages):
    pageObj = pdf1.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile = open('MergedFiles.pdf', 'wb')
with open('C:\\Users\\Bhuvanesh waran\\Downloads\\Merged_output.pdf', 'wb') as file:
    pdfWriter.write(file)



#3.Scrape a website and store the data into DB.


import mysql.connector
import requests as requests
from bs4 import BeautifulSoup

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhuv@n@123",
    database="scrape"
)
dbse = mydb.cursor()
url_to_scrape = 'https://news.ycombinator.com/news'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, "html.parser")
print(soup.prettify())


#4.Write queries to filter the data in db

import mysql.connector

mydb = mysql.connector.connect(
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
