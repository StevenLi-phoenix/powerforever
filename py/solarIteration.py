#!/usr/bin/env python
# coding: utf-8

# In[38]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import itertools as it
import csv


# In[39]:


batteryConfig = pd.read_csv("BatteriesCSV.csv")
batteryConfig


# In[45]:


iteration = []
with open("iter.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(batteryConfig.keys())
    for i in range(1,len(batteryConfig)+1):
        for e in it.combinations_with_replacement(batteryConfig.values, i):
            if len(e) == 1:
                writer.writerows(e)
            else:
                writer.writerow(np.sum(e, axis=0))


# In[44]:


9*8*7*6*5*4*3*2


# In[ ]:




