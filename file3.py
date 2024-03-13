# Eg: 3
# Take the value of length and breadth of a from user and check if it is square or not
'''
length = int(input())
breadth = int(input())
if length==breadth:
    print("its a square")
else:
    print("its not a square")
'''
# Eg:4
# Python programming to check whether the given integer is a multiple of both 5 and 7
'''
n=int(input("enter the number"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
'''
#Eg:5
# Write a program to accept the cost price of a bike and display the road tax to be paid
# according to the following criteria:

#    cost price( in Rs)             Tax
#   > 100000                        15 % + discount 6%
#   > 50000 and <= 100000           10%
#   <= 50000                        5%
'''
price = int(input("enter the price"))
amount = 0
if price>= 100000:
    discount = price*(6/100)
    value = price-discount
    amount=value*(15/100)
    print(value+amount)
'''
#Eg:6
# Write a program to accept the cost price of a bike and display the road tax to be paid
# according to the following criteria:

#    cost price( in Rs)             Tax
#   > 100000                        15 % + discount 6%
#   < 100000                        5%
'''
price=int(input("enter the value: "))
total=0
if price>=100000:
          discount = price*(6/100)
          value = price  + discount
          tax=value*(15/100)
          total=value+tax
else:
    tax=price*(5/100)
    total=price+tax
print("the onroad cost of bike is: ",total)
'''
#if elif
#Eg:1
'''
a=7
b=9
c=3

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("c is grater")
'''
#Eg:2
#A school has following rules for grading system:
#a. Below 25-F
#b. 25 to 45-E
#c. 45 to 50-D
#d. 50 to 60-C
#e. 60 to 80-B
#f. Above 80-A
# Ask user to enter marks and print the corresponding grade.
'''
mark=int(input("enter the mark"))
if mark>=80 and mark<=100:
    print("A")
elif mark>=69 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("Fail")
'''

# --- >short hand if else
#Eg:1
'''
a=9
b=60
if a>b:
    print("A")
else:
    print("b")
'''
#---> using short hand if else
# rules
#1.) statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) Always it have to end with else
'''
print("A") if a>b else print("B")
'''

#code to check the give char is vowel or constant
'''
char= input("enter the number")
if char=="a" or char=="e" or char=="1" or char=="0" or char=="u":
    print("is a vowel")
else:
    print("its constant")
'''
#or
'''
char  = input("Enter the value: ")
str1= "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("constant")
'''

#short hand if else
'''
char=input("enter the value: ")
str1="aeiouAEIOU"
print("vowels") if char in str1 else print("constant")
'''

#--> elif ladder using short hand if else
#Eg:1
#Find the greater than among 3 variables using short hand if else
'''
a=8
b=5
c=6

print("A is greater") if a>b and b>c else print("B is greater") if b>a and b>c else print("c is greater")
'''

#----> looping
# looping can be implemented using
# for loop
# while loop

#--> for loop
# for loop is used for iteartion, if we know the number of times the loop have to run
# It is used to itreate the iterables egg(string, tuples, list, etc...)

#to do ---> syntax for loop

#for syntax in c
#for(i;i<10,i++){
#    print("hello");
#}

# for syntax in python
#for userdefined_variable in range (start, end, step): default step value is 1
#    statement
#    statement
#    statement

#Eg:1
# To print the value from 1 to 10 using loop
'''
for i in range(0,144): #n, n-1
    #print(i)
    print("jashu")
'''
#Eg:2
'''
for val in range(1,10,2):
    print(val)
'''
#Eg:3
# to decrement the value
'''
for val in range(10,0,-1):
    print(val)
'''
'''
for val in range(10,0,-2):
    print(val)
'''
#Eg:4
# print the ouput of 7th multiplication table from 21 to 43

#for i in range(21, 43+1):
    #print("the value is", i*7 )
    #print('7', 'x', i, '=',i*7)-->method:1
    #ans="7x{}={}" #---> method:2
    #print(ans.format(i, i*7))
#method:3
   #'''print(f"7 x {i}={i*7}")'''

#break---> used to terminate the loop
#Eg:5
'''for val in range(0,10):
    if val==9:
        break
    print(val)'''
#Eg:6
'''for val in range(1,10):
    print(val)
    if val==9:
        break'''
#Eg:7
'''for val in range(1,10):
    if val==9:
        print(val)
        break'''
# continue
#Eg:1
'''for val in range(1,10):
    if val==6:
        continue
    print(val)'''

# Practice problems
#print the even number between 20 to 40
'''for i in range(20,41,2):
    print(i)'''
'''for i in range(20,41):
    if i %2==0:
        print(i)'''

#----> while loop
# while is used when the number of times the loop have to run to iterate the non iterable elements while loop is used

#to do syntax
#intialisation
#while condition:
#    statement
#   incre or decre

#Eg:1
# to iterate number from 1 to 10

i=0
#while i<11:
#    print(i)
#    i=i+1 #i+=1

#Eg=2
#10,1
'''i=10
while i>0:
    print(i)
    i-=1'''

#---> 1-4+9-16+25=15
'''n=int(input("enter number: "))
for val in range(1, n+1):
    print(val)'''


'''n=int(input("enter number: "))
sum=0
for val in range(1, n+1):
    sq=val*val
    if val %2==0:
        sum=sum+val
    else:
        sum=sum-sq
print(sum)'''

'''i=0
for val in range(1,6):
    i=val+i
    print(val+1)'''
    

#for loop practise
#write a program to display sum of odd numbers and even
#numbers that fall between
#12 and 37(including both numbers)

#Assesment
#1.)cats and mouse:hacker rank
#2.)Print the factorla of 8 using for loop
#3.)Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)
#4.)write code to print the sum of numbers using while loop n1=123-->1+2+3=6
#5.)prine the reverse of given number ---> n1=1234 o/p-->432
