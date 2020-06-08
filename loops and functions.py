#!/usr/bin/env python
# coding: utf-8

# In[2]:


#for loop 

for i in range(10):
    print("hello world")


# In[3]:


# for loop to print all numbers between 10 and 50

for i in range(11,50):
    print(i)
    


# In[4]:


# odd numbers between 10 and 50 

for i in range(11,50,2):
    print(i)


# In[6]:


#greater of two numbers

def compare(a,b):
    if(a>b):
        greater=a
    else:
        greater=b
    return greater

compare(20,30)
compare(100,50)


# In[ ]:




