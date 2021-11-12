# solarPowerEstimate
author: 李树雨<br>time: 2021.11.7

<img src="85402455_p0.jpeg" >
# 说明文档

## Requirements:
    pandas
    numpy
    matplotlib.pyplot
    PyEMD


## 一个写好的类
Battery

## 主要文件

[solarDataAnalysis.ipynb](./solarDataAnalysis.ipynb)

[progress_analysis.ipynb](./progress_analysis.ipynb)

[analysisDifferatialSolarAndPowerSupply.ipynb](./analysisDifferatialSolarAndPowerSupply.ipynb)

[dailyElectricEstimate.ipynb](./dailyElectricEstimate.ipynb)

battery.py

differenceSolarConsume.py


## 主要文件夹

[npy](./npy/)

[plot](./plot/)

### plot 图片文件说明
[autumn24](plot/autumn24.png)：秋季24h的电量消耗量，其他季节同上说明

[boxplotEachseason](plot/boxplotEachseason.png)：每季度的能量使用时间bixplot

[compareRelationship_2100](plot/compareRelationship_2100.png)：横轴最大可接受断电次数，纵轴电池容量，label：电池充电速率，其他类似的图同上说明

[compareRelationship](plot/compareRelationship.png)：横轴最大可接受断电次数，纵轴电池容量，label：电池充电速率

[imfs_auto_1](plot/imfs_auto_1.png)：emd分解后的图，编号为轨道号

[MaxPerDayPlot](plot/MaxPerDayPlot.png)：每天最大太阳能图

[MaxPerhalfMouthPlot](plot/MaxPerhalfMouthPlot.png)：每月最大太阳能图

[lastElectric](plot/lastElectric.png)：废弃

[relationshipBetweenNopowerCountAndCap](plot/relationshipBetweenNopowerCountAndCap.png)和[relationShip](plot/relationShip.png)：同[compareRelationship_2100](plot/compareRelationship_2100.png)

[SmoothedMaxPerhalfMouthPlot](plot/SmoothedMaxPerhalfMouthPlot.png):
[MaxPerhalfMouthPlot](plot/MaxPerhalfMouthPlot.png)的平滑版本

[SolarRadiationRankingTable](plot/SolarRadiationRankingTable.png)和[SortedOfMaxPerHourPlot](plot/SortedOfMaxPerHourPlot.png)：[MaxPerhalfMouthPlot](plot/MaxPerhalfMouthPlot.png)及其他的平滑版本

[plot/Electric_decline_plots](plot/Electric_decline_plots): 文件夹下的所有内容为不同阶段的没电的最后24h
