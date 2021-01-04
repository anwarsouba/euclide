#!/usr/bin/env python
# coding: utf-8

# In[21]:


def pgcd(dividende,diviseur):
    reste=dividende%diviseur
    while reste!=0:
        dividende=diviseur
        diviseur=reste
        reste=dividende%diviseur
    if reste==0:
        return diviseur
pgcd(1001,700)


# In[19]:


dividende=173
diviseur=18
reste=dividende%diviseur
reste1=dividende%diviseur
quotion=dividende//diviseur
while reste!=0:
    dividende=diviseur
    diviseur=reste
    reste=dividende%diviseur
    quotion=dividende//diviseur
    print(pgcd(dividende,diviseur),"=",dividende ,"-",diviseur,"x",quotion)

