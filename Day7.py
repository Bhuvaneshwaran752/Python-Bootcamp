# frst exercise
def add(x,y):
    return x+y

def sub(x,y):
    return x-y
    
def mul(x,y):
    return x*y
    
def div(x,y):
    return x/y

frst = int(input("enter 1st number : "))
sec = int(input("enter 2nd number : "))

addition = add(frst,sec)
substraction = sub(frst,sec)
multiplication = mul(frst,sec)
division = div(frst,sec)

print("{0} + {1} is equal to {2}".format(frst,sec,addition))
print("{0} - {1} is equal to {2}".format(frst,sec,substraction))
print("{0} * {1} is equal to {2}".format(frst,sec,multiplication))
print("{0} / {1} is equal to {2}".format(frst,sec,division))


# ----------------------------------------------------------------
# second exercise

patient_name = input("enter name : ")
temperature = int(input("whats your body temperature : ")) 
temp = 98
def covid():    
    if (temperature==temp):
        print("{0} ! , you're in...".format(patient_name))
    else:
        print("{0} ! , Sorry you're out...".format(patient_name))
print(covid())

# ----------------------------------------------------------------