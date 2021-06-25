import re


# 1.check string contains only certain set of characters

print(bool(re.match('^[0-9]+$','123')))
print(bool(re.match('^[a-z]+$','abc')))
print(bool(re.match('^[A-Z]+$','ABC')))

print("*"*20)

print(bool(re.match('^[0-9]+$','123a')))
print(bool(re.match('^[a-z]+$','abcA')))
print(bool(re.match('^[A-Z]+$','ABCa')))

#--------------------------------------------------------------------

# 2.matches 'ab'

print(bool(re.search('\w*ab.\w*','abcde')))
print(bool(re.search('\w*ab.\w*','cde')))

#--------------------------------------------------------------------

# 3.check number at the end of senetnce

print(bool(re.compile(r".*[0-9]$").match('ABCa1')))

print(bool(re.compile(r".*[0-9]$").match('ABCa')))

#--------------------------------------------------------------------

# 4.search  the number of length between 1 to 3 in string

search1 = re.finditer(r'([0-9]{1-3})','exercise  numbers are 1,9,11,222 ,13,345 ')
print("length 1 to 3 is ")
for n in search1:
    print(n.group(0))

#--------------------------------------------------------------------

# 5.match uppercase only

print(bool(re.search('^[A-Z]+$','ABCabc')))
print(bool(re.search('^[A-Z]+$','ABC')))