#!/usr/bin/env python
# coding: utf-8

# In[12]:


base = "/Users/lishuyu/Downloads/flowchart/"
with open(f"{base}battery.py", "r") as f:
    file = f.read()


# In[13]:


file


# In[15]:


import pyflowchart as fc


# In[31]:


print(fc.Flowchart.from_code(file,field='',inner=True).flowchart())


# In[ ]:




