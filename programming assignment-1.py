#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##1. Write a Python program to print "Hello Python"?


# In[1]:


print("Hello Python")


# In[ ]:


##2. Write a Python program to do arithmetical operations addition and division.?


# In[4]:


a=int(input("enter a value :"))
b=int(input("enter b value :"))
c=a+b
print("addition of a anb b is :",c)
d=a*b
print("multiplication of a and b is :",d)


# In[ ]:


##3. Write a Python program to find the area of a triangle?


# In[6]:


a=float(input("enter a value"))
b=float(input("enter b value"))
c=float(input("enter c value"))
s=(a+b+c)/2
area=0.5*(s*(s-a)*(s-b)*(s-c))
print("area of triangle is :",area)


# In[7]:


##2.method:when base and height are given,area of triangle =(b*h)/2
b=float(input("enter base"))
h=float(input("enter height"))
area=(b*h)/2
print("area of triangle is :",area)


# In[ ]:


##4. Write a Python program to swap two variables?


# In[8]:


a=int(input("enter a value :"))
b=int(input("enter b value :"))
temp=a
a=b
b=temp

print("value of a :",a)
print("value of b :",b)


# In[ ]:


##5. Write a Python program to generate a random number?


# In[9]:


import random
x=random.randint(1,65)
print(x)


# In[10]:


import random
x=random.randint(1,65)
print(x)


# In[11]:


import random
x=random.randint(1,65)
print(x)

