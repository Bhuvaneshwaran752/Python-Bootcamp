#1. Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

def merge(a,b):
    merged_list=list(zip(a,b))
    return merged_list

list1=["ragnar","micheal","walter"]
list2=["lothbrok","scofeild","white"]
print(merge(list1,list2))

#2. First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples

range=[1,2,3,4,5,6,7,8,9]
list=[9,8,7,6,5,4,3,2,1]
z=tuple(zip(range,list))
print(z)

#3.	Using sorted() function, sort the list in ascending order.

unsorted=[21,33,45,1,2,55,89,103,9,55]
sorted_list=sorted(unsorted)
print(sorted_list)

#4.	Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

def filter_even_number(n):
    if n%2 == 0:
        return False
    else:
        return True
num=[1,2,3,4,5,6,7,8,9,23,45,66,78,79,97]
odd_number = list(filter(filter_even_number,num))
print(odd_number)