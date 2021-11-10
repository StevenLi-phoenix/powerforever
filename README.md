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


## Project tree
.
|____.DS_Store
|____analysisDifferatialSolarAndPowerSupply.ipynb
|____plot
| |____imfs_auto_8.png
| |____SortedOfMaxPerDayPlot.png
| |____SmoothedMaxPerhalfMouthPlot.png
| |____SmoothedMaxPermouthPlot.png
| |____imfs_auto_9.png
| |____.DS_Store
| |____relationshipBetweenNopowerCountAndCap.png
| |____boxplotEachseason.png
| |____SortedOfMaxPermouthPlot.png
| |____Electric_decline_plots
| | |____Electric_decline12600_PRR_3000_7.png
| | |____Electric_decline12700_PRR_2300_5.png
| | |____Electric_decline13000_PRR_2700_4.png
| | |____Electric_decline14900_PRR_2200_2.png
| | |____Electric_decline12600_PRR_3000_6.png
| | |____Electric_decline15000_PRR_2150_3.png
| | |____Electric_decline17100_PRR_2150_2.png
| | |____Electric_decline16400_PRR_2700_1.png
| | |____Electric_decline12600_PRR_2170_8.png
| | |____Electric_decline14300_PRR_2800_2.png
| | |____Electric_decline12600_PRR_9000_7.png
| | |____Electric_decline12600_PRR_8000_7.png
| | |____Electric_decline12700_PRR_2300_6.png
| | |____Electric_decline13900_PRR_2800_3.png
| | |____Electric_decline12500_PRR_10000_10.png
| | |____Electric_decline13000_PRR_2130_6.png
| | |____Electric_decline12600_PRR_2900_7.png
| | |____Electric_decline13900_PRR_2120_4.png
| | |____Electric_decline12600_PRR_2900_6.png
| | |____Electric_decline12500_PRR_2800_9.png
| | |____Electric_decline13000_PRR_2130_7.png
| | |____Electric_decline12600_PRR_2500_8.png
| | |____Electric_decline12500_PRR_2170_10.png
| | |____Electric_decline12600_PRR_8000_6.png
| | |____Electric_decline12600_PRR_9000_6.png
| | |____Electric_decline12600_PRR_2150_10.png
| | |____Electric_decline12600_PRR_2170_9.png
| | |____Electric_decline12500_PRR_2800_10.png
| | |____Electric_decline12500_PRR_2900_10.png
| | |____Electric_decline12600_PRR_2190_8.png
| | |____Electric_decline13900_PRR_2100_5.png
| | |____Electric_decline13900_PRR_8000_3.png
| | |____Electric_decline13900_PRR_9000_3.png
| | |____Electric_decline12600_PRR_2800_7.png
| | |____Electric_decline12500_PRR_6000_10.png
| | |____Electric_decline17200_PRR_2100_3.png
| | |____Electric_decline13900_PRR_2900_3.png
| | |____Electric_decline16800_PRR_2300_1.png
| | |____Electric_decline13900_PRR_10000_3.png
| | |____Electric_decline12700_PRR_2200_6.png
| | |____Electric_decline12600_PRR_2150_8.png
| | |____Electric_decline12600_PRR_2150_9.png
| | |____Electric_decline12500_PRR_9000_9.png
| | |____Electric_decline12500_PRR_8000_9.png
| | |____Electric_decline12600_PRR_2400_8.png
| | |____Electric_decline12600_PRR_2800_6.png
| | |____Electric_decline12500_PRR_2900_9.png
| | |____Electric_decline12600_PRR_2140_10.png
| | |____Electric_decline13000_PRR_2110_7.png
| | |____Electric_decline12600_PRR_2190_9.png
| | |____Electric_decline12700_PRR_5000_5.png
| | |____Electric_decline12600_PRR_7000_8.png
| | |____Electric_decline12700_PRR_4000_5.png
| | |____Electric_decline12600_PRR_6000_8.png
| | |____Electric_decline13900_PRR_3000_3.png
| | |____Electric_decline15000_PRR_2170_2.png
| | |____Electric_decline12800_PRR_2180_6.png
| | |____Electric_decline14900_PRR_2180_2.png
| | |____Electric_decline12500_PRR_2200_10.png
| | |____Electric_decline12500_PRR_2300_10.png
| | |____Electric_decline20000_PRR_2150_1.png
| | |____Electric_decline13000_PRR_2600_4.png
| | |____Electric_decline14500_PRR_2600_2.png
| | |____Electric_decline20000_PRR_2000_8.png
| | |____Electric_decline12500_PRR_3000_9.png
| | |____Electric_decline14400_PRR_2700_2.png
| | |____Electric_decline13900_PRR_2140_4.png
| | |____Electric_decline12700_PRR_8000_5.png
| | |____Electric_decline12600_PRR_2110_9.png
| | |____Electric_decline12700_PRR_9000_5.png
| | |____Electric_decline12900_PRR_2160_7.png
| | |____Electric_decline13000_PRR_7000_4.png
| | |____Electric_decline12700_PRR_2900_5.png
| | |____Electric_decline13000_PRR_6000_4.png
| | |____Electric_decline12700_PRR_10000_5.png
| | |____Electric_decline12600_PRR_2160_10.png
| | |____Electric_decline15200_PRR_2000_10.png
| | |____Electric_decline12600_PRR_2110_8.png
| | |____Electric_decline13100_PRR_2130_5.png
| | |____Electric_decline12600_PRR_2600_8.png
| | |____Electric_decline13000_PRR_2150_6.png
| | |____Electric_decline13900_PRR_5000_3.png
| | |____Electric_decline13900_PRR_4000_3.png
| | |____Electric_decline12700_PRR_3000_5.png
| | |____Electric_decline12600_PRR_2300_7.png
| | |____Electric_decline12500_PRR_2500_10.png
| | |____Electric_decline12500_PRR_2400_10.png
| | |____Electric_decline17000_PRR_2190_1.png
| | |____Electric_decline17100_PRR_2130_2.png
| | |____Electric_decline15000_PRR_2130_3.png
| | |____Electric_decline13900_PRR_2200_3.png
| | |____Electric_decline12900_PRR_2200_5.png
| | |____Electric_decline13000_PRR_2190_4.png
| | |____Electric_decline20000_PRR_2110_1.png
| | |____Electric_decline13000_PRR_2100_8.png
| | |____Electric_decline12600_PRR_2180_7.png
| | |____Electric_decline12500_PRR_4000_9.png
| | |____Electric_decline12500_PRR_5000_9.png
| | |____Electric_decline13000_PRR_2150_5.png
| | |____Electric_decline13000_PRR_2400_4.png
| | |____Electric_decline16400_PRR_6000_1.png
| | |____Electric_decline16400_PRR_7000_1.png
| | |____Electric_decline15000_PRR_2110_3.png
| | |____Electric_decline20000_PRR_2130_1.png
| | |____Electric_decline12600_PRR_4000_7.png
| | |____Electric_decline12600_PRR_5000_7.png
| | |____Electric_decline12500_PRR_7000_10.png
| | |____Electric_decline14100_PRR_10000_2.png
| | |____Electric_decline17400_PRR_2000_9.png
| | |____Electric_decline13900_PRR_2300_3.png
| | |____Electric_decline17000_PRR_2170_1.png
| | |____Electric_decline12600_PRR_2200_7.png
| | |____Electric_decline13000_PRR_2170_4.png
| | |____Electric_decline13000_PRR_2170_5.png
| | |____Electric_decline13900_PRR_2180_3.png
| | |____Electric_decline13000_PRR_2500_4.png
| | |____Electric_decline16500_PRR_2600_1.png
| | |____Electric_decline13100_PRR_2110_6.png
| | |____Electric_decline12600_PRR_5000_6.png
| | |____Electric_decline12600_PRR_4000_6.png
| | |____Electric_decline14200_PRR_2900_2.png
| | |____Electric_decline12600_PRR_2130_9.png
| | |____Electric_decline12700_PRR_2800_5.png
| | |____Electric_decline13900_PRR_2160_4.png
| | |____Electric_decline14800_PRR_2300_2.png
| | |____Electric_decline12600_PRR_10000_7.png
| | |____Electric_decline12600_PRR_10000_6.png
| | |____Electric_decline14100_PRR_7000_2.png
| | |____Electric_decline14100_PRR_6000_2.png
| | |____Electric_decline12600_PRR_2130_8.png
| | |____Electric_decline13100_PRR_2110_5.png
| | |____Electric_decline12600_PRR_2700_8.png
| | |____Electric_decline12600_PRR_4000_8.png
| | |____Electric_decline13000_PRR_2900_4.png
| | |____Electric_decline12700_PRR_6000_5.png
| | |____Electric_decline12600_PRR_5000_8.png
| | |____Electric_decline13000_PRR_2120_7.png
| | |____Electric_decline12700_PRR_7000_5.png
| | |____Electric_decline13000_PRR_9000_4.png
| | |____Electric_decline13000_PRR_8000_4.png
| | |____Electric_decline12600_PRR_2120_10.png
| | |____Electric_decline13900_PRR_2130_4.png
| | |____Electric_decline12600_PRR_2160_9.png
| | |____Electric_decline12600_PRR_2200_8.png
| | |____Electric_decline12600_PRR_2200_9.png
| | |____Electric_decline12600_PRR_2160_8.png
| | |____Electric_decline16400_PRR_3000_1.png
| | |____Electric_decline13000_PRR_2120_6.png
| | |____Electric_decline12600_PRR_2700_6.png
| | |____Electric_decline12500_PRR_2600_9.png
| | |____Electric_decline12500_PRR_2190_10.png
| | |____Electric_decline16700_PRR_2400_1.png
| | |____Electric_decline13000_PRR_3000_4.png
| | |____Electric_decline15000_PRR_2140_3.png
| | |____Electric_decline17100_PRR_2140_2.png
| | |____Electric_decline20000_PRR_2160_1.png
| | |____Electric_decline12600_PRR_10000_8.png
| | |____Electric_decline16400_PRR_2900_1.png
| | |____Electric_decline12700_PRR_2400_5.png
| | |____Electric_decline16400_PRR_8000_1.png
| | |____Electric_decline16400_PRR_9000_1.png
| | |____Electric_decline13900_PRR_2600_3.png
| | |____Electric_decline12800_PRR_2170_6.png
| | |____Electric_decline12600_PRR_2700_7.png
| | |____Electric_decline17100_PRR_2160_2.png
| | |____Electric_decline12500_PRR_2180_10.png
| | |____Electric_decline15000_PRR_2160_3.png
| | |____Electric_decline20000_PRR_2140_1.png
| | |____Electric_decline12600_PRR_2600_6.png
| | |____Electric_decline12500_PRR_2700_9.png
| | |____Electric_decline14100_PRR_3000_2.png
| | |____Electric_decline16400_PRR_2800_1.png
| | |____Electric_decline12700_PRR_2500_5.png
| | |____Electric_decline12500_PRR_4000_10.png
| | |____Electric_decline12600_PRR_2600_7.png
| | |____Electric_decline14900_PRR_2190_2.png
| | |____Electric_decline13900_PRR_2700_3.png
| | |____Electric_decline12800_PRR_2190_6.png
| | |____Electric_decline12600_PRR_2130_10.png
| | |____Electric_decline16400_PRR_10000_1.png
| | |____Electric_decline12600_PRR_2140_9.png
| | |____Electric_decline17200_PRR_2110_2.png
| | |____Electric_decline13000_PRR_2800_4.png
| | |____Electric_decline12600_PRR_2300_8.png
| | |____Electric_decline13900_PRR_2110_4.png
| | |____Electric_decline12600_PRR_2180_9.png
| | |____Electric_decline14600_PRR_2500_2.png
| | |____Electric_decline12600_PRR_2180_8.png
| | |____Electric_decline12600_PRR_2300_9.png
| | |____Electric_decline12600_PRR_2140_8.png
| | |____Electric_decline12500_PRR_9000_10.png
| | |____Electric_decline14100_PRR_9000_2.png
| | |____Electric_decline14100_PRR_8000_2.png
| | |____Electric_decline12600_PRR_2190_7.png
| | |____Electric_decline13900_PRR_2170_3.png
| | |____Electric_decline20000_PRR_2000_5.png
| | |____Electric_decline13000_PRR_2300_4.png
| | |____Electric_decline12500_PRR_3000_10.png
| | |____Electric_decline13000_PRR_2180_5.png
| | |____Electric_decline13000_PRR_2140_5.png
| | |____Electric_decline14700_PRR_2400_2.png
| | |____Electric_decline12600_PRR_2800_8.png
| | |____Electric_decline12500_PRR_2500_9.png
| | |____Electric_decline12600_PRR_2400_6.png
| | |____Electric_decline12600_PRR_2400_7.png
| | |____Electric_decline14100_PRR_4000_2.png
| | |____Electric_decline13900_PRR_2500_3.png
| | |____Electric_decline14100_PRR_5000_2.png
| | |____Electric_decline13000_PRR_2180_4.png
| | |____Electric_decline20000_PRR_2100_1.png
| | |____Electric_decline17100_PRR_2120_2.png
| | |____Electric_decline15000_PRR_2120_3.png
| | |____Electric_decline12700_PRR_2700_5.png
| | |____Electric_decline20000_PRR_2000_4.png
| | |____Electric_decline17000_PRR_2180_1.png
| | |____Electric_decline12600_PRR_7000_7.png
| | |____Electric_decline13100_PRR_2120_5.png
| | |____Electric_decline12600_PRR_6000_7.png
| | |____Electric_decline20000_PRR_2000_6.png
| | |____Electric_decline15000_PRR_2100_4.png
| | |____Electric_decline13000_PRR_2140_6.png
| | |____Electric_decline12600_PRR_2110_10.png
| | |____Electric_decline13900_PRR_2150_4.png
| | |____Electric_decline13000_PRR_2140_7.png
| | |____Electric_decline20000_PRR_2100_2.png
| | |____Electric_decline12600_PRR_2100_9.png
| | |____Electric_decline20000_PRR_2000_7.png
| | |____Electric_decline12600_PRR_6000_6.png
| | |____Electric_decline12600_PRR_7000_6.png
| | |____Electric_decline13900_PRR_6000_3.png
| | |____Electric_decline13900_PRR_7000_3.png
| | |____Electric_decline20000_PRR_2000_3.png
| | |____Electric_decline12600_PRR_3000_8.png
| | |____Electric_decline13000_PRR_2160_6.png
| | |____Electric_decline12500_PRR_2600_10.png
| | |____Electric_decline12500_PRR_2700_10.png
| | |____Electric_decline12600_PRR_2120_8.png
| | |____Electric_decline12600_PRR_2100_10.png
| | |____Electric_decline12900_PRR_2150_7.png
| | |____Electric_decline12500_PRR_5000_10.png
| | |____Electric_decline16600_PRR_2500_1.png
| | |____Electric_decline12600_PRR_2120_9.png
| | |____Electric_decline12500_PRR_7000_9.png
| | |____Electric_decline12500_PRR_6000_9.png
| | |____Electric_decline16400_PRR_5000_1.png
| | |____Electric_decline16400_PRR_4000_1.png
| | |____Electric_decline20000_PRR_2000_2.png
| | |____Electric_decline13000_PRR_2200_4.png
| | |____Electric_decline12900_PRR_2190_5.png
| | |____Electric_decline12600_PRR_2170_7.png
| | |____Electric_decline13900_PRR_2190_3.png
| | |____Electric_decline17000_PRR_2200_1.png
| | |____Electric_decline13000_PRR_2160_5.png
| | |____Electric_decline12600_PRR_9000_8.png
| | |____Electric_decline12600_PRR_8000_8.png
| | |____Electric_decline12500_PRR_2400_9.png
| | |____Electric_decline12600_PRR_2500_6.png
| | |____Electric_decline13100_PRR_2100_6.png
| | |____Electric_decline12600_PRR_2900_8.png
| | |____Electric_decline13000_PRR_4000_4.png
| | |____Electric_decline13000_PRR_5000_4.png
| | |____Electric_decline13900_PRR_2400_3.png
| | |____Electric_decline13100_PRR_2100_7.png
| | |____Electric_decline12500_PRR_10000_9.png
| | |____Electric_decline12500_PRR_8000_10.png
| | |____Electric_decline12600_PRR_2500_7.png
| | |____Electric_decline20000_PRR_2120_1.png
| | |____Electric_decline12700_PRR_2600_5.png
| | |____Electric_decline13000_PRR_10000_4.png
| | |____Electric_decline20000_PRR_2000_1.png
| |____imfs_auto_10.png
| |____imfs_auto_11.png
| |____imfs_auto_13.png
| |____SortedOfMaxPerHourPlot.png
| |____imfs_auto_12.png
| |____imfs_auto_16.png
| |____MaxPerHourPlot.png
| |____imfs_auto_17.png
| |____imfs_auto_15.png
| |____SortedOfMaxPerhalfMouthPlot.png
| |____imfs_auto_14.png
| |____MaxPerDayPlot.png
| |____SolarRadiationRankingTable.png
| |____imfs_auto_19.png
| |____winter24.png
| |____imfs_auto_18.png
| |____lastElectric.png
| |____compareRelationship_2110.png
| |____compareRelationship.png
| |____compareRelationship_2100.png
| |____relationShip.png
| |____imfs_auto_22.png
| |____imfs_auto_20.png
| |____MaxPerhalfMouthPlot.png
| |____imfs_auto_21.png
| |____imfs_auto_2.png
| |____solarData.png
| |____spring24.png
| |____imfs_auto_3.png
| |____imfs_auto_1.png
| |____autumn24.png
| |____imfs_auto_4.png
| |____MaxPermouthPlot.png
| |____imfs_auto_5.png
| |____imfs_auto_7.png
| |____summer24.png
| |____imfs_auto_6.png
|____solarDataAnalysis.ipynb
|____progress_analysis.ipynb
|____battery.py
|____xunlian.csv
|______pycache__
| |____battery.cpython-37.pyc
|____README.md
|____loadFromTrainSet.csv
|____dailyElectricEstimate.ipynb
