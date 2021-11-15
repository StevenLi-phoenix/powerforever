#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import json
import csv


# In[6]:


data = pd.read_csv("battery_evaluate_ouput.csv")


# In[7]:


data


# In[66]:


data.sort_values(by=["max_cap"])


# In[19]:


below2_1k = []
below2_2k = []
below2_3k = []
other2 = []
below5_1k = []
below5_2k = []
below5_3k = []
other5 = []
below10_1k = []
below10_2k = []
below10_3k = []
other10 = []
other = []

bound = [30000, 60000, 90000]

min_cost = 100000
for i in data.sort_values(by=["max_nopower_count"]).T:
    k = json.loads(data.values[i][4])
    cost = sum([c["cost"] for c in k])
    if data.values[i][0] <= 2:
        if cost <= bound[0]:
            below2_1k.append(data.values[i])
        elif bound[0]<cost<=bound[1]:
            below2_2k.append(data.values[i])
        elif bound[1]<cost<=bound[2]:
            below2_3k.append(data.values[i])
        else:
            other2.append(data.values[i])
    elif 2< data.values[i][0] <= 5:
        if cost <= bound[0]:
            below5_1k.append(data.values[i])
        elif bound[0]<cost<=bound[1]:
            below5_2k.append(data.values[i])
        elif bound[1]<cost<=bound[2]:
            below5_3k.append(data.values[i])
        else:
            other5.append(data.values[i])
    elif 5< data.values[i][0] <= 10:
        if cost <= bound[0]:
            below10_1k.append(data.values[i])
        elif bound[0]<cost<=bound[1]:
            below10_2k.append(data.values[i])
        elif bound[1]<cost<=bound[2]:
            below10_3k.append(data.values[i])
        else:
            other10.append(data.values[i])
    else:
        other.append(data.values[i])


# In[41]:


base = "/Users/lishuyu/Downloads/"
with open(f"{base}10_3.txt", "w") as f:
    f.write(str(below10_3k))


# In[45]:


below2_1k = []
below2_2k = []
below2_3k = []
other2 = []
below5_1k = []
below5_2k = []
below5_3k = []
other5 = []
below10_1k = []
below10_2k = []
below10_3k = []
other10 = []
other = []

bound = [30000, 60000, 90000]

min_cost = 100000
count = 0
max_length = len(data)
for i in data.sort_values(by=["max_nopower_count"]).T:
    count += 1
    data_cache = data.values[i]
    k = json.loads(data_cache[4])
    cost = sum([c["cost"] for c in k])
    if data_cache[0] <= 2:
        if cost <= bound[0]:
            below2_1k.append(data_cache[2])
        elif bound[0]<cost<=bound[1]:
            below2_2k.append(data_cache[2])
        elif bound[1]<cost<=bound[2]:
            below2_3k.append(data_cache[2])
        else:
            other2.append(data_cache[2])
    elif 2< data_cache[0] <= 5:
        if cost <= bound[0]:
            below5_1k.append(data_cache[2])
        elif bound[0]<cost<=bound[1]:
            below5_2k.append(data_cache[2])
        elif bound[1]<cost<=bound[2]:
            below5_3k.append(data_cache[2])
        else:
            other5.append(data_cache[2])
    elif 5< data_cache[0] <= 10:
        if cost <= bound[0]:
            below10_1k.append(data_cache[2])
        elif bound[0]<cost<=bound[1]:
            below10_2k.append(data_cache[2])
        elif bound[1]<cost<=bound[2]:
            below10_3k.append(data_cache[2])
        else:
            other10.append(data_cache[2])
    else:
        other.append(data_cache[2])
    if count % 100 == 0:
        print(count/max_length, "%")


# In[47]:


base = "/Users/lishuyu/Downloads/"
with open(f"{base}2_1_name.txt", "w") as f:
    f.write(str("\n".join(below2_1k)))
with open(f"{base}2_2_name.txt", "w") as f:
    f.write(str("\n".join(below2_2k)))
with open(f"{base}2_3_name.txt", "w") as f:
    f.write(str("\n".join(below2_3k)))
with open(f"{base}5_1_name.txt", "w") as f:
    f.write(str("\n".join(below5_1k)))
with open(f"{base}5_2_name.txt", "w") as f:
    f.write(str("\n".join(below5_2k)))
with open(f"{base}5_3_name.txt", "w") as f:
    f.write(str("\n".join(below5_3k)))
with open(f"{base}10_1_name.txt", "w") as f:
    f.write(str("\n".join(below10_1k)))
with open(f"{base}10_2_name.txt", "w") as f:
    f.write(str("\n".join(below10_2k)))
with open(f"{base}10_3_name.txt", "w") as f:
    f.write(str("\n".join(below10_3k)))


# In[48]:


import pyperclip


# In[61]:


pyperclip.copy(str(below10_3k))


# In[68]:


len(below10_2k)


# In[ ]:


cost = []
for i in dic:
    cost.append(i["cost"])


# In[ ]:


sum(cost)


# In[ ]:




