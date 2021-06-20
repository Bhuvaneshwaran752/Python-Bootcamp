#1. add and divide

a=int(input("enter number : "))
b=int(input("enter number : "))
c=int(input("enter number : "))
s=a+b+c
d=int(input("Enter number to divide : "))
print("the result is ", s/d)

if s%d == 0 :
    print("the number is divided")
else:
    print("the number is not divided")

# ------------------------------------------------------------------------------

# 2 .capitalize

a=input("Enter the string : ")
print(a.capitalize())

# ------------------------------------------------------------------------------
# 3. converting binary

def decoct(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")

decoct(188)

# ----------------------------------------------------------------------------

# 4.dictionary key and sort the lsit

# without function

dict1={'whalter white':[12,13,21,16],'jesse pinkman':[12,67,54,43],'loki':[34,87,88,98],'sucre':[33,66,55,44]}
result={k:sorted(dict1[k]) for k in sorted(dict1)}
print(result)

# with function

def function1(dict1):
    res = dict()
    for key in sorted(dict1):
        res[key] = sorted(dict1[key])
    return res

# ----------------------------------------------------------------------------

# 5. descending to ascending and set

list1=[2,3,4,5,6,7,1,2,3,43,12,14]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
set1=set(list1) 
print(set1)

# ----------------------------------------------------------------------------

# 6. frst occurences


def fun():
    user=input("Enter the string :")
    word="String is given by user  "
    return user+word[6:]
fun()

# ----------------------------------------------------------------------------


# 7.mean median mode

#mean
a=[20,30,40]
print((sum(a)/len(a)))

#median
a.sort()
l=len(a)

if l%2==0:
    m1=a[n//2]
    m2=a[n//2-1]
    m=(m1+m2)/2

else:
    m=a[l//2]

print("meadian is : "+ str(m))

# mode
import counter 

data = Counter(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        get_mode = "No mode "
    else:
        get_mode = "Mode  are: " + ', '.join(map(str, mode))
    print(get_mode)

# ----------------------------------------------------------------------------


# 8.merge dict


dict1={1:'a',2:'b',3:'c',4:'d'}
dict2={5:'e',6:'f',7:'g'}
print(dict2)
dict2.update(dict1)
print(dict1)
print(dict3)
print(dict2)

# ----------------------------------------------------------------------------


# 9.repeated list

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))

# ----------------------------------------------------------------------------


#10. swapcase

a= "Bhuvanesh waran"
swap = a.swapcase()
print(swap)

# ----------------------------------------------------------------------------
