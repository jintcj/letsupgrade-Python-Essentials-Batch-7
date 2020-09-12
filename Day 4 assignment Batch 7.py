#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for num in range( 1042000,702648265):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        order =tempt % 10
        sum += digit**order
        temp//=10
    if num == sum:
        break
print("The first Armstrong Number is ",i)


# In[ ]:




