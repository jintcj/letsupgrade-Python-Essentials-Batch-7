#!/usr/bin/env python
# coding: utf-8

# Assignment 1

# In[2]:


get_ipython().run_cell_magic('writefile', 'findPrime.py', 'def get_Prime(num):\n    if (n == 1):\n        return False\n    elif (n==2):\n        return True;\n    else:\n        for x in range(2,n):\n            if(n % x==0):\n                return False\n        return True             \nprint(test_prime(3))')


# Assignment 2

# In[4]:



lst = list(range(1000))


# In[12]:


def getAmstrongNumberGen(lst):
    for num in lst:
        
        order = len(str(num))
        sum = 0
        temp = num
        while temp>0:
            digit = temp % 10
            sum += digit ** order
            temp//= 10
            
        if num == sum:
            yield num


# In[13]:


list(getAmstrongNumberGen(lst))


# In[ ]:




