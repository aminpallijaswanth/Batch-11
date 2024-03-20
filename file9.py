# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#2.)Find the uncommon words from 2 strings

'''
s1 = "Hello how are you"
s2 = "Hello how is"

s1=s1.split(" ")
s2=s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
'''


#3.)Write a code print the 8th fibanochi number
# 0, 1, 1, 2, 3, 5, 8

'''
n1=0
n2=1
ans=0+1 #---> 1

n1=1
n2=1
ans=1+1 #==>2

n1=1
n2=2
ans=1+2==>3

n1=2
n2=3
ans=2+3=5
'''

# Find the 8th fibnochi number

'''
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)
'''

#---> constructors
#Eg:2
# unparametarised constructor
'''
class profile:
    def __init__(self):
        print("hello world")

obj=profile()
obj.__init__()
'''

#Eg:3
#parametarised constructor

'''
class profile:
    def __init__(self, id, name,age):
        print(id, name, age)

obj = profile(1, "lucifer", 21)
'''

#Eg:4

'''
class c1:
    name="lucifer"
    place="usa"
    
    def m1(self):
        print(self.name, self.place)

object = c1()
object.m1()
'''

'''
class c1:
    email="lucifer@gmail.com"
    
    def m1(self):
         name="lucifer"
         place="usa"
         print(name, place)
         print(self.email)

object = c1()
object.m1()
'''

#Eg:5


'''
class c1:
    email="jashu@gmail.com"
    def m1(self):
        name="jashu"
        age=21
        return name, age

    def display(self):
        #print(name,age)-->error
        #print(self.age, self.name)-->error
        
        print(self.m1())
            
object = c1()
object.display()
'''

#Eg:6
# To use the variable inside the constructor in another methods

'''
class class1:
    def __init__(self):
        self.name = "jashu" -----> # instance variable
        self.email = "jashu@gmail.com" ----> # static variable
        #return name, email #error ---> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()
'''

# ----> Inheritance
#1.) The process of utilising the methods and attributes of parant class
#2.) Throught the object of child class it is called as inheritence 

# ----> 5 types of inheritence

#1.) Single Inheritence
#2.) Multilevel Inheritence
#3.) Multiple Inheritence
#4.) Hybrid Inheritence
#5.) Hierarichal Inheritence

#---> 1.) Single Inheritence
# It has only one parant class and only one child class

# Eg:1
'''
class parent:
    def m1():
        print("I am parent class")

parent.m1()

class child:
    def m2():
        print("I am child class")

child.m2()
'''

'''
class parent:
    def m1(self):
        print("I am parent class")

class child(parent):
    def m2(self):
        print("I am child class")
        
obj=child()
obj.m1()
'''

''' # ---> error
class parent(child):
    def m1(self):
        print("I am parent class")

class child:
    def m2(self):
        print("I am child class")
        
p=parent
p.m2()
obj=child()
obj.m1()
'''

# Eg:2

'''
class c1:
    def __init__(self):
        print("I am constructor from parent class")

class child1(c1):
    pass

obj = child1()
'''


# Eg:3

'''
class parent:
    name = "jashu"

class child(parent):
    name="name1"

    def display(self):
        print(self.name)

d = child()
d.display()
'''

#2.) Multilevel Inheritence

# Eg:1

'''
class voice:
    def sound(self):
        print("All the animals have thier own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("Meow")
        
class parrot(cat):
    def parrot_voice(Self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''


# Eg:2

'''
class honda_city:
    def engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(self, cc, hp, torque, fuel_type, num_of_piston)

        def body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class amaze:
        def amaze_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def amaze_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class civic(amaze):
        def civic_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def civic_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class honda:
    pass

honda= honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")
'''

#3.) Multiple Inheritence
# -> It has multiple parent and 1 child

'''
class while_petrol:
    def function_w(self):
        print("used to Airplans")

class organic_petrol:
    def function_o(self):
        print("used for bike, cars")

class premium_petrol:
    def function_p(self):
        print("sports car, bikes")

class petrol(while_petrol, organic_petrol, premium_petrol):
    def defanition(self):
        print("petrols type")

p=petrol()
p.defanition()
p.function_o()
'''

# Eg:2
# MRO---> Method resolution order

'''
class addition:
    def add(Self, a,b):
        print(a+b)

    def mul(self, a, b):
        print(a%b) 

class subtract:
    def sub(self, a, b):
        print(a-b)

class multiply:
    def mul(self, a, b):
        print(a*b)

class division(addition, subtract, multiply):
    def div(self, a, b):
        print(a/b)

calc=division()
calc.add(3,4)
calc.mul(5,2)
'''

#5.) Hierarichal Inheritence
# The one parent claas will be act as parent for all the child classes

'''
class catagory:
    def weight(self, weight):
        print(weight)

    def display(self, color, taste):
        print(color, taste)

class tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste="neutral taste"
        self.display(color, taste)

class carrot(catagory):
    def carrot_specs(self):
        color="green"
        taste="sweet"
        self.display(color, taste)

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = tomato()
t.tomato_specs()
t.weight("50gms")
'''

#4.) Hybrid Inheritence
# -> The combination of above 4 inheritence is called Hybrid inheritence

'''
class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")
        
class c3(c2):
    def m3(self):
        print("class3")

class c4(c3):
    def m4(self):
        print("class4")

    def m3(self):
        print("iam m3 form c4")    

class c5(c4):
    def m5(self):
        print("class4")

class c6(c5, c3):
    def m6(self):
        print("class4")

obj = c6()
obj.m3()
'''

# ----> Polymorphism
#poly-many, morph-->form
# A function which has the ability to perform more than 1 functionality
#then it is considered to be as polymorphism

# Polymorphism in bultin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

# polymorphism in operators
# +

'''
print(8+8)
print("k"+"1")
print([1,2,3]+[5,6])
'''

# *
'''
print(6*7)
l1={1,2,3,4,5,6}
print(*l1)
def f1(*args)
'''

'''
l1=[1,2,3,4]
print(l1*10)
'''

    
# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading ---> It is not possible in python
# 2.) Method overriding

# ---> Tasks

#d1 = {"shirt":100, "pant":1500, "shoes":900, "handkey":30}
# 1.) Find the min ans max priced product
# 2.) Find the product starts with "s" and "S"

# 2.) Find the n=67, is strong number or not

# 3.) l1=[1,2,3,4,5,6]
# n=2 ---> [5,6,1,2,3,4]
# n=3 ---> [4,5,6,1,2,3]















'''
Problem Statement -: A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

The Matrix is filled with cells,and each cell will have an initial value as follows:

A value greater than or equal to zero represents a path.
A value equal to 1 represents a passenger.
A value equal to -
'''

