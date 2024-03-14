#---> while loop
#---> Break using while loop

#Eg:1
#1.)iterate from 20 t0 30 and break the loop in 27
''''
i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1
'''
#2.)                      
'''i=20
while i<31:
    print(i)
    i+=1
    
    if i==27:
        break'''
#3.)
'''i=20
while i<31:
    print(i)
    
    if i==27:
        break
    i+=1'''
#4.)
'''i=20
while i<31:
    if i==27:
        print(i)
        break
    i+=1'''

#---> continue
#Eg:1
'''i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1'''
#2.)
'''i=20
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)'''
#Eg:5
# while to iterate from 12 to 22
#find sum of all numbers
'''i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
    print(sum)'''
#Eg:6
#Find the avg of value from 20 to 25
'''i=20
sum=0
count=0
while i<=25:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)'''
#Find the avg of value from 20 to 30
'''i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)'''

#--->nested for loop
#Eg:1
'''
for row in range(1,3+1):
    for col in range(1,4+1):
        print(row,col)'''
#Eg:2
# * * * *
# * * * *
# * * * *
# * * * *
'''for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()'''
        
#print(1,end=" ")
#print(2)
'''row=int(input("enter the number"))
col=int(input("enter the number"))
for row in range(row):
    for col in range(col):
        print(row, end=" ")
    print()'''

'''sum=0
for row in range(5):
    for col in range(5):
        print(row, end=" ")
    print()'''

# To print stars in right angled triangle
'''
for row in range(0,6):
    for col in range(0,row):
        print("*", end=" ")
    print()'''

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

'''for row in range(0,6+1):
    for col in range(row+1,6+1):
        print("*", end=" ")
    print()'''

'''for row in range(0,6,-1):
    for col in range(0,row):
        print("*", end=" ")
    print()'''

#* * * * *
#*       *
#*       *
#*       *
#* * * * *
'''
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''

#      *
#    * * *
#   * * * *
#  * * * * *

'''for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *

'''for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()'''

#----> List

#---> Datatypes
# Primary

# Number---> int,float,complex
# string
# Boolean
# none

# Collection
# List
# tuple
# set
# dictionary

#---> List

#1.) If the collection of elements are surrounded by square brackets, it is considered to be list
##Eg:1
   #l1 = [4, 7, 9, 89, "hello", 7+9], [8,9,0]

#characteristics of list
#1.)list have to surrounded by[]
#2.)It is mutable ( the elements in the list are changable)
#3.)Every element inside list in indexed
#4.)The elements inside list will be ordered format
#5.)It can hold duplicate values
#6.)it is heterogenous

# TO access the elements in list
lst1=[1,4,1,7,89.7,5,"p","i",5,2,20]
#print(l1)

#--->Indexing
#The collection datatypes like list, tuple, string, the elements will be alloted with predefined unique value called index value

#We have 2 types of indexing
#positive indexing --> starts with 0 from left hand side
#Negative indexing --> starts with -1 from right hand side

#--->Positive indexing
'''print(lst1[0])
print(lst1[4])
print(lst1[10])
print(lst1[20])''' #--->error

#---> Negative indexing
'''lst1=[1,4,1,7,89.7,5,"p","i",5,2,20]
print(lst1[-1])
print(lst1[-4])'''

#--->slicing
#lst1=[1,4,1,7,89.7,5,"p","i",5,2,20]
#lst1[start_index:end_index:step]

#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])

'''print(lst1[0:7:1])''' #lst1[0:7]---> both are same actually
'''print(lst1[0:7:2])'''

#trail=int(input())

lst1=[1,4,1,7,89.7,5,"p","i",5,2]
#print(lst1[-4:-1])
#print(lst1[-1:-4])--->[]
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

# TO insert ot add element inside list

#append()
lst1=[9,8,0,6]
lst1.append("car")
print(lst1)
