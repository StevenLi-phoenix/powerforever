#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv("iter.csv")
data_values = data.values
data


# In[3]:


data_values[1000, 0].split(";")[:-1]


# In[4]:


# Usabe Capacity(kWh)
data_values[0, 6]


# In[5]:


# Cost($)
data_values[0, 7]


# In[6]:


battery_data = pd.read_csv("BatteriesCSV2.csv")
battery_data_value = battery_data.values
battery_data_Tdict = dict(battery_data.T)
battery_data


# In[7]:


battery_data_NameDic = {}
for i in battery_data_value:
    battery_data_NameDic[i[0]] = i[1:]


# In[8]:


battery_data_NameDic


# In[9]:


for i in data_values[1000, 0].split(";")[:-1]:
    obj = battery_data_NameDic[i]
    capacity = obj[5]
    cost = obj[6]
    efficiency = obj[4]
    power = obj[7]
    print(capacity, power, efficiency, cost)
    


# In[10]:


from batteryModel import battery, logger
bats = []
for i in data_values[1000, 0].split(";")[:-1]:
    obj = battery_data_NameDic[i]
    capacity = obj[5]
    cost = obj[6]
    efficiency = obj[4]
    power = obj[7]
    bats.append(battery(capacity, power, efficiency, cost))


# In[13]:


bats[0].cost


# In[ ]:




