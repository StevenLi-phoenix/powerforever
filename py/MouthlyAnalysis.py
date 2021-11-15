#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.interpolate
import random

plot = "plot/"
npy = "npy/"

solar_rad = pd.read_csv("xunlian.csv")
solar_rad


# In[36]:


# chage value to standard
data_min = solar_rad.values[:, 2]
saved = None
saved_index = 0
hour = []
toArry = solar_rad.values
for i in range(len(solar_rad)):
    time_alpha = toArry[i,1].split(":")[0]
    if time_alpha != saved:
        saved = time_alpha
        hour.append(sum(toArry[saved_index:i,2]))
        saved_index = i
    if i % 1000 == 0:print(i)
hour.append(sum(toArry[saved_index:i,2]))


# In[37]:


hour = np.array(hour)/max(hour)*20


# In[38]:


plt.plot(hour)


# In[23]:


24*30*12


# In[24]:


len(hour)


# In[40]:


# chage value to standard
data_min = solar_rad.values[:, 2]
saved = None
saved_index = 0
week = []
toArry = solar_rad.values
for i in range(len(solar_rad)):
    time_alpha = toArry[i,0].split("/")[1]
    if time_alpha != saved:
        saved = time_alpha
        week.append(sum(toArry[saved_index:i,2]))
        saved_index = i
    if i % 1000 == 0:print(i)
week.append(sum(toArry[saved_index:i,2]))


# In[42]:


plt.plot(week)
plt.title("Mouthly photovoltaic power generation")
plt.grid()


# In[43]:


import csv

# open the file in the write mode
f = open('Mouth_data.csv', 'w')
# create the csv writer
writer = csv.writer(f)
# write a row to the csv file
writer.writerow(week)
# close the file
f.close()


# In[44]:


len(week)


# In[45]:


week[0]


# In[ ]:




