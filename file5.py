#-----> common functions for list
#l1=[6,7,8,9,0]
#print(len(l1))
'''
print(max(l1))
print(min(l1))'''

#l1=[6,8,9,"p","u"]
'''print(max(l1)) #---> error coz its a combination int and string'''

#undex ()----> to get index value of specific element
#l1=[6,7,8,9,0,8.89,-5,0.78]
'''print(l1.index(9))'''

#count---> how many num of times an element is repeated
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
'''print(l1.count(6))'''

# some functions which is specifically used for list

#To add element inside
#insert()---> to add element at specific index position
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#l1.insert(2,"cars")
'''print(l1)'''

#---> to delete elements from list
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
'''l1.pop() #---> pop()-- to delete last element
print(l1)'''

'''pop(index_value) #----> to delete specific position value
l1.pop(4)
print(l1)'''

#remove(element)---> used to delete element directly
'''l1.remove(8.89)
print(l1)'''

#clear()--->to complete the delete all elemnts on list
'''l1.clear()
print(l1)'''

#del--> to delete the list
'''del l1
print(l1)'''

#---> join 2 lists
#l1=[9,0,8]
#l2=["p","o","t",34]
'''print(l1+l2)'''

#or
#extend()---> to combine 2 lists
'''l1.extend(l2)
print(l1)'''

#--->copy()
#l1=[6,7,8,9,3]
#l1.copy()
#l2=l1.copy()
'''print(l2)
print(l1)'''

'''print(id(l1))
print(id(l2))'''

#--->diff between shallow copy and deep copy
#shallow copy
#import copy
'''l1 = [8,9,0,[5,6],[3,2,1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)'''

#deep copy---> used to copy the list with nested list
#import copy
'''l1 = [8,9,0,[5,6],[3,2,1]]
print(l1[-1][1]) #---> to index nested list
l2 = copy.copy(l1)
l1.append(890)
print(l1)'''

#sort---> used to arrange elements in liast in ascending order or descending order
#l1=[9,7,45,0,-6,5,12]
'''l1.sort()# to arrange in ascending order
print(l1)
l1.sort(reverse=True)# to sort in descending order
print(l1)'''

#l1=["i","o","p"]
'''l1.sort()
print(l1)'''

#l1[:z","i","o","p", 9]
'''l1.sort()
print(l1)''' #error

#list in contrutor
#lsit()--> to conver other collection datatype in list
#l3=((8,9,0))
'''print(list(l1))'''

'''l4=(8,9)
print(list(l4))'''

#---> nested list
#l1=[8,9,[0,8,7],["p","O,","y"],[8,"t"]]
'''print(l1[-2][1])#output-->o
print(l1[3])'''

#print(l1[1:4])
#print(l1[1:-1])

# to delete "t" form l1
'''l1[-1].remove("t")
print(l1)'''

# combine these ["p","o,"y"],[8,"t"] lists in l1 to["p","o","y",8,"t"]
'''l1=["p","o","y"]
l2=[8,"t"]
l1.extend(l2)
print(l1)'''

'''l1[-2].extend(l1[-1])
l1.pop[-1]
print(l1)'''

#Tuple--->
#char of tuple
#1.) Tuple have to be surrounded by()
#2.) The elements inside tuple are not changable
#3.) The element inside are indexed
#4.) The element will execute in order
#5.) It is heterogenous
#6.) It will allow duplicate elements

#Eg:1
'''t1=(8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))
'''

#--->indexing,slicing are all same as list
# ways to create tuple
#l1=(8)
'''print(type(l1)) #int'''

#l1=(8,)
'''print(type(l1))#tuple'''

#t1=8,
'''print(type(t1))#tuple'''

#t2=8,9
'''print(type(t2)) #tuple'''

#len(),min(),index(),count()---> all same as list

# To add elements inside tuple ---> cannot add
# cannot delete any element from tuple
''' join 2 tuples
t1=(8,9,0)
t2=(6,7,8)
print(t1+t2)
'''


# To add all element inside list and tuple
'''sum()
l1 = (8, 9, 7, 6)
print(l1)'''

# sort tuple
'''t1=(8,9,0,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1,reverse=True)))'''

#Iterate list and tuple

#Iterate based on elements
'''l1=[9,8,0,6,5]
for i in l1:
    print(i)'''

#Iterate basesd on index value
'''l1=[9,8,0,6,5]
for i in range(0,5):
    print(l1[i])
print(l1[4])'''

'''s1="0"
print(type(s1))
'''

#s1="hello world"
# To access string
'''print(s1)'''

#indexing and slicing---> same as list and tuple
#print(s1[0:5])

#--->common functions

#len(),min(),max(),index(),count()
'''s1="hello world" 
#print(len(s1))
#print(max(s1))
#print(min(s1))
'''

#ord()---> used to find the ASCII value of a character
'''s1="u"
print(ord(s1))'''


# Functions of string
'''s1="hello world"'''

# to convert all characters to upper case
'''print(s1.upper())'''

# To convert to lower case
'''s1="JASHU"
print(s1.lower())'''

#strip()---> to skip or eliminate the space r-right side, l-leftside(lstrip)
'''s1="Where are you"
print(s1.lstrip())'''

s1="hey there dont sleep"
i=7
#print(s1.lstrip())
#print(s1.rstrip())
#print(s1,strip())


# split()--> To split the words in string based on a character
'''s1="Where are you"
print(s1.split(" "))
print(s1.split("r"))

print(s1.count("e"))'''


# replace()---> To replace specific characters in the string
'''s1="hey there dont sleep"
print(s1.replace("r","&&"))'''

#swapcase()---> To convert capital to small and small to capital at a time
'''s1="HEY there"
print(s1.swapcase())'''

#title()---> It will convert the characters to title form
'''s1="never giveup"
print(s1.title())'''

#capitalize()
'''s1="never giveUP"
print(s1.capitalize())'''

# JOin the strings
'''s1="hello"
s2="world"
print(s1+s2)'''

#s1=
'''how are you
i am fine
hey there
'''

#splitline()-->used to split the string based line
#print(s1.splitline())

#find()--> to find the index based on a character
#s1="hello world"
'''print(s1.find("h"))
print(s1.index("z"))'''

# joint()--> 
'''l1=["hey", "there"]
print(" ".join(l1))
print("$".join(l1))'''

'''s1="welcome to all"
print(s1.endswith("l"))
print(s1.startswith("w"))'''

'''s1="67"
print(type(s1))
print(s1.isdigit())'''

# Print the string in reverse manner
#s1="Welcome to all"
'''print(s1[::-1])'''

#Eg:1
'''s1="HEY there you aRE"
count=0
for i in s1:
    if i.islower():
        count+=1 
print("the total num of lower case letters:",count)
'''

#Eg:2 r--->$
'''s1="restarter"
s1="IMAGIN"
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst,"$")
print(fst+txt)'''

#str1="bbbbbbbbyyyybbbbaaaioo"
#str2="%"

#Eg:3
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop "
s2=s1.strip()
#characters=len(s1)
#print(characters)

'''words=s1.split(" ")
print(words)
print(len(words))'''

'''sentences = s1.split(" ")
for val in sentences:
    if val==" ":
        index=sentences.index("")
        sentences.pop(index)
print(len(sentences))'''

space=0
for val in s1:
    if val==" ":
        space==space+1
print(space)
