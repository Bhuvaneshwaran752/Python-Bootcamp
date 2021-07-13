from threading import Thread,active_count
from time import sleep
from datetime import date
class t1(Thread):
    def run(self):
        print(date.today())
        sleep(0.2)

class t2(Thread):
    def run(self):
        print(date.today())
        sleep(1)


a = t1()
a.start()
b=t2()
b.start()


print()
print("number of active threads : ",active_count())
