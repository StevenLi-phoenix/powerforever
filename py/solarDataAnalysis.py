#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.interpolate
import random

plot = "plot/"
npy = "npy/"


# In[ ]:


solar_rad = pd.read_csv("xunlian.csv")
solar_rad


# In[ ]:


solar_rad_array = np.array(solar_rad)
solar_rad_value_array = np.array(solar_rad_array[:,2], dtype=int)/max(solar_rad_array[:,2])*20000


# In[ ]:


max_per_hour = []
for value in range(len(solar_rad_value_array)//60):
    max_per_hour.append(list(solar_rad_value_array[60*value:60*value+60]))
data = np.max(max_per_hour, axis=1)
color = np.array(data, dtype=int)
plt.scatter(np.arange(len(data)), data, c=np.array(data), s=0.4)
plt.title("MaxPerHourPlot")
plt.savefig(f"{plot}MaxPerHourPlot.png",format='jpg', dpi=2400)
plt.show()
plt.scatter(np.arange(len(data)), np.sort(data), c=np.sort(np.array(data)), s=0.1)
plt.title(f"{plot}SortedOfMaxPerHourPlot")
plt.savefig(f"{plot}SortedOfMaxPerHourPlot.png",format='jpg', dpi=2400)
plt.show()


# In[ ]:


max_per_day = []
for value in range(len(solar_rad_value_array)//(60*24)):
    max_per_day.append(list(solar_rad_value_array[(60*24)*value:(60*24)*value+(60*24)]))
data = np.max(max_per_day, axis=1)
color = np.array(data, dtype=int)
plt.scatter(np.arange(len(data)), data, c=np.array(data), s=4)
plt.title("MaxPerDayPlot")
plt.savefig(f"{plot}MaxPerDayPlot.png")
plt.show()
plt.scatter(np.arange(len(data)), np.sort(data), c=np.sort(np.array(data)), s=2)
plt.title("SortedOfMaxPerDayPlot")
plt.savefig(f"{plot}SortedOfMaxPerDayPlot.png")
plt.show()


# In[ ]:


max_per_mouth = []
for value in range(len(solar_rad_value_array)//(60*24*30)):
    max_per_mouth.append(list(solar_rad_value_array[(60*24*30)*value:(60*24*30)*value+(60*24*30)]))
data = np.max(max_per_mouth, axis=1)
color = np.array(data, dtype=int)
plt.plot(data)
plt.title("MaxPermouthPlot")
plt.savefig(f"{plot}MaxPermouthPlot.png",format='jpg', dpi=2400)
plt.show()
plt.plot(np.sort(data))
plt.title("SortedOfMaxPermouthPlot")
plt.savefig(f"{plot}SortedOfMaxPermouthPlot.png",format='jpg', dpi=2400)
plt.show()
x_new = np.linspace(0, len(data), 300)
a_BSpline = scipy.interpolate.make_interp_spline(np.arange(len(data)), data)
y_new = a_BSpline(x_new)
plt.plot(x_new, y_new)
plt.savefig(f"{plot}SmoothedMaxPermouthPlot.png",format='jpg', dpi=2400)
plt.show()


# In[ ]:


color = np.array(solar_rad.values[:,2]/max(solar_rad.values[:,2])*1000, dtype=int)
plt.scatter(np.arange(len(solar_rad)), np.sort(np.array(solar_rad.values[:,2]), -1), c=np.sort(color, -1), s=0.1)
plt.title("Solar radiation ranking table")
plt.savefig(f"{plot}SolarRadiationRankingTable.png",format='jpg', dpi=2400)
plt.show()


# In[ ]:


max_per_halfMouth = []
for value in range(len(solar_rad_value_array)//(60*24*10)):
    max_per_halfMouth.append(list(solar_rad_value_array[(60*24*10)*value:(60*24*10)*value+(60*24*10)]))
data = np.max(np.array(max_per_halfMouth), axis=1)
color = np.array(data, dtype=int)
plt.plot(data)
plt.title("MaxPerhalfMouthPlot")
plt.savefig(f"{plot}MaxPerhalfMouthPlot.png",format='jpg', dpi=2400)
plt.show()
plt.plot(np.sort(data))
plt.title("SortedOfMaxPerhalfMouthPlot")
plt.savefig(f"{plot}SortedOfMaxPerhalfMouthPlot.png",format='jpg', dpi=2400)
plt.show()
x_new = np.linspace(0, len(data), 300)
a_BSpline = scipy.interpolate.make_interp_spline(np.arange(len(data)), data)
y_new = a_BSpline(x_new)
plt.plot(x_new, y_new)
plt.savefig(f"{plot}SmoothedMaxPerhalfMouthPlot.png",format='jpg', dpi=2400)
plt.show()


# In[ ]:


"""import PyEMD
import uuid
emd_obj = PyEMD.EMD()
imfs = emd_obj.emd(np.array(solar_rad_value_array), max_imf=5)
np.save(f"{npy}imfs{uuid.uuid4()}.png", imfs)
count = 0
for imf in imfs:
    count+=1
    plt.plot(imf)
    plt.title(f"emd-{count}")
    plt.savefig(f"{plot}imfs_auto_{count}.png")
    plt.show()
"""


# In[ ]:


sum_per_Mouth = []
for value in range(len(solar_rad_value_array)//(60*24*10)):
    sum_per_Mouth.append(list(solar_rad_value_array[(60*24*10)*value:(60*24*10)*value+(60*24*10)]))
data = np.sum(np.array(sum_per_Mouth), axis=1)
color = np.array(data, dtype=int)
plt.plot(data)
plt.title("SumPer10daysPlot")
plt.savefig(f"{plot}SumPer10daysPlot.png",format='png', dpi=6000)
plt.show()
plt.plot(np.sort(data))
plt.title("SortedOfSumPer10daysPlot")
plt.savefig(f"{plot}SortedOfSumPer10daysPlot.png",format='png', dpi=6000)
plt.show()
x_new = np.linspace(0, len(data), 300)
a_BSpline = scipy.interpolate.make_interp_spline(np.arange(len(data)), data)
y_new = a_BSpline(x_new)
plt.plot(x_new, y_new)
plt.savefig(f"{plot}SmoothedSumPer10daysPlot.png",format='png', dpi=6000)
plt.show()


# In[ ]:


sum_per_mouth = []
for value in range(len(solar_rad_value_array)//(60*24*30)):
    sum_per_mouth.append(list(solar_rad_value_array[(60*24*30)*value:(60*24*30)*value+(60*24*30)]))
data = np.sum(sum_per_mouth, axis=1)
color = np.array(data, dtype=int)
plt.plot(data)
plt.title("sumPermouthPlot")
plt.savefig(f"{plot}sumPermouthPlot.jpg",format='jpg', dpi=2400)
plt.show()
plt.plot(np.sort(data))
plt.title("SortedOfsumPermouthPlot")
plt.savefig(f"{plot}SortedOfsumPermouthPlot.jpg",format='jpg', dpi=2400)
plt.show()
x_new = np.linspace(0, len(data), 300)
a_BSpline = scipy.interpolate.make_interp_spline(np.arange(len(data)), data)
y_new = a_BSpline(x_new)
plt.plot(x_new, y_new)
plt.title("SmoothedsumPermouthPlot")
plt.savefig(f"{plot}SmoothedsumPermouthPlot.jpg",format='jpg', dpi=2400)
plt.show()


# In[ ]:


sum_per_day = []
for value in range(len(solar_rad_value_array)//(60)):
    sum_per_day.append(list(solar_rad_value_array[(60)*value:(60)*value+(60)]))
data = np.sum(sum_per_day, axis=1)
solar_rad_value_array = data/max(data)*20000


# In[ ]:


choice = random.randint(0, len(data)//24)*24
data = data/max(data)*20000
day_data = data[choice:choice+24]

plt.plot(day_data)
plt.title("sumOnedayPlot")
plt.savefig(f"{plot}sumOnedayPlot.jpg",format='jpg', dpi=2400)
plt.show()
plt.plot(np.sort(day_data))
plt.title("SortedOfsumOnedayPlot")
plt.savefig(f"{plot}SortedOfsumOnedayPlot.jpg",format='jpg', dpi=2400)
plt.show()
x_new = np.linspace(0, len(day_data), 300)
a_BSpline = scipy.interpolate.make_interp_spline(np.arange(len(data)), data)
y_new = a_BSpline(x_new)
plt.plot(x_new, y_new)
plt.title("SmoothedsumOnedayPlot")
plt.savefig(f"{plot}SmoothedsumOnedayPlot.jpg",format='jpg', dpi=2400)
plt.show()


# In[ ]:




