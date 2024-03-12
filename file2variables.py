'''
a,b=c=7,8
print(a)
print(b)
print(c)
'''

'''
a=b, c=4,2
print(a, b, c)
'''

#swapping of variables --->

a = 7
b = 5
'''
#Eg :1
temp = a #temp=7 #Its a duplicate variable used to swap the variable
a = b #a=5
b = temp #b=7

print(a, b)
'''
'''
#Eg : 2

a=a+b #a=12
b=a-b #b=12-7=5
a=a-b #a=12-5=7

print(a, b)
'''

'''
#Eg:3

a, b=b, a
print(a, b)
'''

'''
#Eg: 4

a=a*b #a=35
b=a/b #b=37/7 = 5
a=a/b #a=35/5 = 7
print(int(a), int(b))
'''

#Eg:4
#id() ---> used to find the memory address of the variable
'''
a = 7
print(id(a))
'''

#---> keywords
# keywords are reserved words which provides speacial meaning to compiler or intrerpretor
#Eg:5
'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(type(keyword.kwlist))
'''

#To check if the string is keyword or not
#print(keyword.iskeyword("hv")) #output=false
'''
if = 8
print(if) #output = error as the "if" is a keyword
'''

#---->literals
#Literal is the constant value assigned to a variable
# A variable is considered to be constant when it is defines in caps
'''
a= 78 # a is variable
A=78 # A is constant

L1 = [9,8,0]
print(type(L1))
l1 = [6, 7, 8, 0]

l1 = 89
'''

#hash() ---> it creates a hash value for constant datatypes and provides error for non constant datatypes
'''
n1 = 89.78
print(hash(n1))

n1=89+7j
print(hash(n1))

f1=[7,8,9]
#print(hash(f1)) #output = error ---> list is non-constant or mutable datatype
'''

'''
a=9
b=9
print(id(a))
print(id(a))
'''
'''
a=9
b=90
print(id(a))
print(id(b))
'''

#!---> Operator
#operators are symbols which is used to perform various operations between 2 or more operands

#Arithmatic
#Logical
#Relational or comparison
#Bitwise
#Identity
#Membership


# todo ----> Arithmatic ---> +, -, *, /, %, //, **
#Eg : 1
'''
a = 8
b = 6
c = 9
print(a+b+c)
'''

#Eg :2
'''
a = 45
b = 24
c = 34
print(a-b-c)
'''

#input()--> used to get the runtime input
'''
n1 = input("enter the value: ")
print(type(n1))
n1 = int(input("enter the value: "))
print(type(n1))
#eval()---> used to get the runtime values of all the datatypes
n1 = eval(input("enter the value: "))
print(type(n1))
'''
'''
a = 4
b = 2
print(a/b) # is used to get the quotient value
print(a%b) #is used to get the remainder value
'''

# //---> floor divison

'''
a = 76543
b = 19

print(a/b)
print(a//b) #--> the output will be an integer & the output will be based on floor value
'''


# **---> used for power number
'''
print(2**4) #--->16
'''

# Assignment ---> +-=, -=, /=, *=, //=, **=, &=, |=
'''
a= 8
a+=2
print(a)

a=30
a-=5
print(a)
'''

# comparison ---> ==, >, <, !=, <=, >=
'''
a=8
b=9
print(a<b) # output = True

a=9
b=5
print(a==b) # output = False
'''

# Bitwise operator ---> &, |, ^, ~, <<, >>
'''
a=7
b=4
print(a&b)
'''

# AND
# A B A&B
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

#OR
# A B A&B
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

#XOR
# A B A^B
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

# 31 16 8 4 2 1
# 0  0  1 0 1 0 #--> 10
# 1  0  0 1 1 0 #--> 38
#_______________
# 1

'''
print(10^38)
'''

'''
#2^4 2^3 2^2 2^1 2^0
#8   4   2   1

#0   1   0   0    #--> 7
#0   1   1   1    #--> 6 &
#
#0   1   1   1 #--> 7
'''

# 256 128 64 32 16 8 4 2 1
# 0   0   0  0  0  1 0 0 
# 
# 

'''
a=678
print(~a) #output = -679
'''

'''
a=9
print(~a+1) # output = -9
'''

# a = 9
# 128 64 32 16 8 4 2 1
#  0   0  0  0 1 0 0 1 # -->9

#  1   1  1  1 0 1 1 0 #--> -10

# 0  0  0  0  1  0 1 0 -->10

# 1  1  1  1  0  1 0 1--> 1s a compliment of 10
                   #1 --> 2s compliment
#
#  1 1 1 1 1 # 1 1 0 --> -10

# 256 128 64 32 16 8 4 2 1
# 0   0   0  0  0  0 1 0 1 --> 3
# 0   0   0     0  1 0 0 0 --> 40
# 107

# <<, >>
'''
print(5<<3) # output = 40
print(5>>1) # output = 2
#16>4
'''

# ---> Logical---> used to compare the expressions
# and, or, not
'''
a=6
print(a>3 and a<10) # output = True
print(a>7 or a<30) # output = True
print(not(a>8 and a<10)) # output = True
'''

#Identity operator
# is, is not
#a=8
#b=8
'''
print(a is b) # output = True
print(a==b) # output = True
print(a is not b) # output = False

a=[1, 2, 3]
b=[1, 2, 3]

print(a is b) # output = False

a=(1, 2, 3)
b=(1, 2, 3)
print(a is b) # output = True
'''

# Membership operator
# in, not in
'''
L1 = [7, 8, 9, 0, 6, 5]
num=55
print(num in L1)
print(num not in L1)

num = 678
print(8 in num)#error
'''

# conditional statement
#if, elif, else

#Eg:1
#---> C syntax
'''
if (condition:){
    statement;
    statement;
    statement;
}
#Python syntax
if condition:
    statement
    statement
    statement
    statement
'''

#Eg:1
'''
a=6
if a:
    print("hello") #ouput = hello
'''
#Eg:2
'''
a=6
if a>3:
    print("hey")
else:
    print("no")
'''
#Eg:3
'''
if 7>8:
    print("jashu")
else:
    print("sarsarle eneno anukuntam")
'''
#Eg:4
'''
a=0
a=None
a=False
a=""
if a:
    print("yes")
else:
    print("no")
'''

#a number is even or odd
'''
n=int(input("enter the number: "))
if n %2==0:
    print(n, "is even")
else:
    print(n,"is odd")
'''

#name, age, nationality
# 18 above, Indian

name = input("enter the name: ")
age = int(input("enter the age: "))
nationality=input("enter the nation: ")

if age>18 and nationality=="indian":
    print("elgible for vote")
else:
    print("not elgible for vote")


        
    
