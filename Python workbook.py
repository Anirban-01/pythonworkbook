#!/usr/bin/env python
# coding: utf-8

# In[6]:


def my_function(): #defining of fuction call my_function with block of indention
    a=1
    return(a)
print(my_function())


# In[7]:


x = [1,2,3]
print(x)


# In[8]:


x = [1,2,[3,4],5] #Nested list of objects
print(x[2])


# In[5]:


x=[1,2,3,4] #In python object can be modified
x[1]=5
print(x)


# In[13]:


a=1
b=2

if a > b:
    print (a)
else:
    print (b)


# In[16]:


def my_function(): #When function return nothing need to use pass.
    pass


# In[2]:


print(4)


# In[3]:


type(4)


# In[4]:


type('4')


# In[7]:


message='Im anirban sen' #assignment statement
print(message)


# In[11]:


import keyword #list of keyword used in python programming
print(keyword.kwlist)


# In[12]:


x = 1
print (x)


# In[13]:


1+1


# In[1]:


minute = 60
minute/60


# In[3]:


minute = 59
if minute > 60:
    print(minute)
else:
    print (60)


# In[5]:


i = 2*(3+4)# python follow rule of prcedence(PEMDAS)
print (i)


# In[12]:


Name = 'Anirban Sen is ' #concatenate on two different strings
Age = 'Twenty Eight'
print (Name + Age)


# In[1]:


Name = "123"
print(Name)


# In[2]:


type("12")


# In[3]:


Name = type(1) #Examples of function calls
print(Name)


# In[15]:


id(2)


# In[16]:


num = 2


# In[17]:


id(num)


# In[18]:


id(3)


# In[19]:


num = 3


# In[20]:


id(num)


# In[23]:


int(2.3) #type conversion from float to interger using int() function


# In[24]:


str("Anirban")


# In[26]:


str(1)


# In[30]:


num = 1 #Using type coercion means to convert from one data type to another automatically
num + 1.2


# In[31]:


num =60


# In[32]:


num / 60.0


# In[6]:


import math
decibel = math.log10(17)
angle = 1.5
math.sin(angle)


# In[7]:


math.sqrt(angle)


# In[15]:


import math
decibel = math.log(17.1)


# In[20]:


import math
degrees = 90
radians = math.radians(degrees)
angle = math.sin(radians)
print(angle)


# In[22]:


import math
degrees = 45
radius = math.radians(degrees)
angle = math.cos(radius)
print(angle)


# In[33]:


def my_function():
    print("Anirban Sen")
my_function() #---> This is where function gets call.


# In[50]:


def my_function(name):
    print("My name is : " + name)
my_function("Anirban")#----> This is calling function with argument.


# In[7]:


import math
x=math.exp(math.log(10))
print(x)


# In[6]:


import math
x = math.exp(math.log10(1))
print(x)


# In[13]:


"""Write the correct keyword to make the variable x belong to the global scope."""

def my_function():
    global x
    x = "Example" #----Answer global


# In[15]:


"""The following code example would print the data type of x, what data type would that be? """

x = ["apple", "banana", "cherry"]


# In[16]:


print(type(x))


# In[17]:


"""The following code example would print the data type of x, what data type would that be? """
x = ("apple", "banana", "cherry")


# In[18]:


print(type(x))


# In[19]:


"""The following code example would print the data type of x, what data type would that be?"""
x = {"name" : "John", "age" : 36}
print(type(x))


# In[24]:


def name():
    print("Anirban")

name()


# In[42]:


"""Write a function called ninelines that uses threeLines to print nine blank lines. How would you print twenty seven new line"""
def nineLines():
    print ("threeLines")
   
nineLines()
nineLines()
nineLines()
nineLines()
nineLines()
nineLines()
nineLines()
nineLines()
nineLines()


# In[54]:


def my_name(firstname, secondname): """Function having two parameters within parenthises."""
    print(firstname + secondname)

my_name("Anirban ","Sen")


# In[19]:


def threeLines():
    newline()
    newline()
    newline()


# In[20]:


print("firstline")
newline()
print("secondline")


# In[21]:


import math
degrees = 90
angle = degrees*2*math.pi/360.0
math.sin(angle)


# In[22]:


import math
degrees =90
radians = math.radians(degrees)
angle = math.sin(math.radians(degrees))
print(angle)


# In[25]:


def printname(bruce): """python built-in function with arguments"""
    print('bruce'*4)
    
printname('bruce'*4)


# In[26]:


def name(pavitra):
    print('pavitra'*2)

name("pavitra")


# In[46]:


def printTwice(spam):
   print('spam'*4)
    
printTwice('spam') 


# In[29]:


def my_function(name, age):
    info = name + age
    return info

my_function('Anirban ','28')


# In[49]:


def my_function(name,age):
    info = ("Anirban"+"28") #<----------creating local variable inside the function and then print the variable---->
    print(info)
    
my_function("name","age")


# In[55]:


def my_data(name,age,color):
    info =('Anirban'+'28'+'fair')
    print(info)

my_data('name','age','color')


# In[58]:


def my_function():
    print()
    
my_function()


# In[61]:


def my_data(name1):
    print(name1 + "sen")
my_data('Anirban')


# In[79]:


def my_friend(frd1,frd2,frd3):
    print(frd1,frd2,frd3)

my_friend('Anirban','Pavitra','Manohara')


# In[85]:


def my_data(Firstname,lastname):
    print(Firstname + lastname)
    
my_data('Anirban ','Sen')


# In[89]:


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# In[88]:


def my_data(fname,lname):
    print(fname,lname)

my_data('Emil','Refsnes')


# In[90]:


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# In[92]:


def my_youngchild(*kids):
    print('My youngest child is:'+ kids[1])

my_youngchild('sita','gita')


# In[ ]:




