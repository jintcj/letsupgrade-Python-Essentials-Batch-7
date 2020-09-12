#!/usr/bin/env python
# coding: utf-8

# Assignment 2
# 

# In[2]:


def primeNumber(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

num = filter(primeNumber, range(2501))
print ('Prime numbers between 1-2500:', list(num))


# Assignment 1
# 

# In[5]:


def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                if n == len(s):
                    sub_set = True
    return sub_set

a = [1,5,6,4,1,2,3,5]
b = [1,5,6]
c = [1,1,6]
print(is_Sublist(a, b))
print(is_Sublist(a, c))


# Assignment 3
# 

# In[ ]:


lst = input("Enter ")
lst_new = map(lambda n: n.capitalize(), lst)
list(lst_new)

