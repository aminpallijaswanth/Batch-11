# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

#Eg:3
'''
def profile(name,age,place):
txt="My name is{}. Iam {} years old. Iam from{}"
    print(txt.format(name,age,place))
print("jash",21,"cbe")
'''

#Eg:4
#Function with return statement


#--->return
#1.) A variable declared inside the function can be accessed outside the function using return
#2.) Return does not print anything
#3.) We cannot write any code below return statement


'''
def f1():
    a=8
f1()
print(z) #error ---> cannot use outside the function
'''

'''
def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)
'''

# 123

'''
def palindrome(n):
    string=str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print(n,"Not palindrome")
a=int(input("enter the value: "))
palindrome(a)
'''


# BAsed ont he declaratiion of parameter and args
# Function are divided into 5 categories

# Positional args
# Keyword args
# Default args
# Variable args
# Keyword variable length args

# ----> Positional args
# The position of parameters have to be same as postion as arguments
#Eg:1

'''
def profile(name,phone,mark):
    txt="My name is {}.My phone number is{}. I got{}marks"
    print(txt.format(name,phone,mark))

profile(8555945167, "jashu", 100) #---> unexpected output
'''

# Keyword args
#Eg:2
#To overcome the disadvantage of position args, we used keyword args
# It is the process of initialising the parameter with the args while calling the function

''' 
def profile(name,phone,mark):
    txt="My name is {}.My phone number is {}. I got {} marks"
    print(txt.format(name,phone,mark))

profile(name = "jashu",mark = 96,phone = 8555945167)
'''

# todo---> Exception of keyword args function

'''
def profile(name,phone,mark):
    txt="My name is {}.My phone number is{}. I got{}marks"
    print(txt.format(name,phone,mark))

#print(name="sid", 123456789, mark=100) #output---> error -->positional args follow keyword args
#print(123456789, name="sid", mark=100) #output--->error-->has multiple values
profile("jashu", mark=98, phone=1234556678) #ouput---> My name is jashu.My phone number is1234556678. I got98marks
'''

# Default args
# The method of assigning the argument to the parameter while declaring the function
#Eg:1

'''
def profile(name,phone,place="kadapa"):
    txt="My name is {}.My phone number is {}. I am from {}"
    print(txt.format(name,phone,mark))

profile("sid", 123456789, "kadapa")
'''

#Eg:2

'''
def profile(name,phone,place="kadapa"):
    if place=="Kadapa" or place=="KADAPA" or place=="kadapa":
        txt="My name is {}.My phone number is{}. I am from {}"
        print(txt.format(name,phone,place))
    else:
        print("You are not elgible to signup")
profile("jashu", 123456789, "Guntur")
'''

#--> Exception

'''
def profile(name,phone,place="KADAPA",phone): #error--> coz default args should not follow positional param
    if place=="Kadapa" or place=="KADAPA" or place=="kadapa":
        txt="My name is {}.My phone number is{}. I am from {}"
        print(txt.format(name,phone,place))
    else:
        print("You are not elgible to signup")
file("jashu", 123456789)
'''

# Variable length params
# To pass more than 1 arg to a parameter means we use varaible length args
# TO convert normal parameters to variable length param, add * to their prefix of param
#Eg:1

'''
def profile(*name):
    print("My name is", name)
profile("sid",'name2','name3')
'''

'''
name="sid", "name1", "name2"
def profile(*name):
    for val in name:
        print("My name is", val)
profile("sid","name2","name3")
'''


'''
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal
'''

#Eg:2

'''
def profile(*name,age):
    for val in name:
        print("My name is",val, "my age is", age)
profile("jash", "name2", "name3", 28) #error--> age has no args
'''

'''
def profile(age,*name):
    for val in name:
        print("My name is",val, "my age is", age)
profile(28, "jash", "name2", "name3")
'''


# Keywords variable length args
# Kwargs ---> which is used to provide the args in the form of key value pair
#Eg:1

'''
def price(**price_list):
    print(price_list)

print(shirt=100, iphone=100000)
'''

#n=5
#{1:1,2:4,3:9,4:16,5:25}

'''
n=int(input("Enter the number:"))
d1={}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)
'''    

'''
def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val]=val**2
    print(d1)
dict1(5)
'''

#---> Object oriented programming
# The paradigms of objects oriented programming are
#1.) Class
#2.) objects
#3.) inheritence
#4.) polymorphism
#5.) abstraction
#6.) encapsulation


# class is a blue print of an object

#l1 = [1,2,3,4,5,6]

#Eg:1

'''
class c1():
    name1="lucifer"
    print(name1)
'''

#Eg:2

'''
class person:
    name="lucifer"

c=person() #c as object
# The process of creation of an object is known as instantiation
print(c.name)
'''

#Eg:3
#creation of a method
# When the function is created with a class as method

# Method without parameter
'''
class person:
    def display(person): #It is a method
        print("Hello welcome to classes")
        
p = person()
p.display()
'''

#Eg:4

# Method without parameter
'''
class person:
    def display(person, name, age): #It is a method
        print(name,age)
        
p = person()
p.display()
'''

#Eg:5

'''
class person1:
    fname="lucifer" #attribute or static variable
    lname="T"
    
    def first_name(self):
        print(self.fname)

    def full_name(self):
        print(self.fname+" "+self.lname)
        

p=person1()
p.first_name()
p.full_name()
'''


#Eg:6
# COnstructor---> __init__()
# This is a special method which has the ability to execute itself without calling it manually through the process of instantiation 

class profile:
    def __init__(self): #constructor method
        print("hey")

p=profile() # elecution of constructor through this process
p.__init__()    





'''
#d1={"a":100, "b":200, "c":300}
d1=dict(a=100, b=200,c=300)
print(d1)
'''

