#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# ### Functions, Conditionals & Iterations
# Function in python is defined using keyword 'def'. range function defines the list of numbers exclusive of the parameter number.

# In[4]:


def CheckXY(x, y):
    if(x<y):
        print("x = {} is smaller than y = {} ".format(x, y))
    elif(x==y):
        print("x = {} is equal to y = {} ".format(x, y))
    else:
        print("x = {} is greater than y = {} ".format(x, y))
for i in range(3): #This acts as a list [0,1,2]
    CheckXY(i,1)


# In[6]:


for i in range(2,11,2): #start=2 stop=11 steps=2
    print("I am number {}".format(i))
    if(i<10):
        print("Taking 2 steps")


# In[12]:


a = range(3,7)
for i,e in enumerate(a):
    print("Index {} was :{}".format(i,e))


# ### Datatypes

# In[15]:


print("Datatype of a is ",type(a))
print("Data type of CheckXY is",type(CheckXY))

