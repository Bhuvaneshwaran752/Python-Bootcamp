class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("user details")
        print(self.name)
        print(self.age)
        print(self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0

    def Deposit(self):
        amount=float(input("enter the amount to be deposited : "))
        self.balance=self.balance + amount
        print("amount has been updated",self.balance)

    def withdrawal(self):
        amount=float(input("enter the amount to be withdraw : "))
        if amount > self.balance:
            print("Insufficient funds |  Current Balance : ",self.balance)
        else:
            self.balance=self.balance - amount
            print("available balance : ",self.balance)


    def view_balance(self):
        self.show_details()
        print("available balance : ", self.balance)


s=Bank("Bhuvanesh waran",20,"Male")
s.view_balance()
s.Deposit()
s.withdrawal()





