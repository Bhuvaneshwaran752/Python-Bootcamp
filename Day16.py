# LAMBDA

# 1.count even number

a=[1,2,3,4,5,6,7,8,9,10]
print(a)
even=list(filter(lambda x:(x%2==0),a))
print(len(even))


#2.divisible by 9

a=[1,2,3,4,5,6,7,8,9,10,18,27]

nine=list(filter(lambda x:(x%9==0),a))
print("divisible by 9 are {0}".format(nine))

# 3. multiply each number with gn number

a=[1,2,3,4,5,6,7,8,9,10]
num=int(input("enter number to multiply : "))
multiply=list(map(lambda n:n*num,a))
print(multiply)

# # 4.fibonacci

def fibonacci(count):
    a=[0,1]
    any(map(lambda _:a.append(sum(a[-2:])),range(2,count)))
    return a[:count]
print(fibonacci(5))

# 5.multiplie argumrnt x and y

mul=lambda x,y:x*y
print(mul(5,5))

