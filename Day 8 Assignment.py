#!/usr/bin/env python
# coding: utf-8

# Assignment 1

# In[2]:


def fib(self, N):
    """
    :type N: int
    :rtype: int
    """
    cache = {}
    def recur_fib(N):
        if N in cache:
            return cache[N]

        if N < 2:
            result = N
        else:
            result = recur_fib(N-1) + recur_fib(N-2)

       
        cache[N] = result
        return result

    return recur_fib(N)


# Assignment 2

# In[1]:


import sys

try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))
   
except ValueError:
    print("No valid integer in line.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# In[ ]:




