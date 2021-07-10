from datetime import datetime, date,timedelta


#1. str to date time

strtodatetime = datetime.strptime('Jul 9 2021 7:54PM', '%b %d %Y %I:%M%p')
print(strtodatetime)

print('-'*50)

#2.subtract five days

tdy = date.today()
minus_5_days = timedelta(5)
date = tdy - minus_5_days
print('Current Date :', tdy)
print('after subtracting 5 days  :', date)

print('-'*50)

#3.date to datetime


tdy1 = date.today()
print(datetime.combine(tdy1, datetime.min.time()))
print('-'*50)
#4.nxt 7 days from tdy
import datetime
tdy2 = datetime.datetime.today()
for day in range(0, 7):
      print(tdy2 + datetime.timedelta(days=day))

print('-'*50)