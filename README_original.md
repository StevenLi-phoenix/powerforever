# solarPowerEstimate
author: 李树雨

time: 2021.11.7

revise: 2021.11.13

<img src="85402455_p0.jpeg" >

# 说明文档

## Requirements:
    pandas
    numpy
    matplotlib.pyplot
### optional:
    PyEMD


## 写好的类
battery.py
batteryModel.py

## 主要文件

[analysisDifferatialSolarAndPowerSupply.ipynb](analysisDifferatialSolarAndPowerSupply.ipynb): 计算在平均条件下（ps：春季电量消耗下）最小电池容量

[batterAnalysis.ipynb](batterAnalysis.ipynb): 空单元格（我：？？？

[batterChoiceEvaluation.py](batterChoiceEvaluation.py): 最终所有可能的电池组合枚举输出，最后版本

[battery.py](battery.py): 电池的类，第一代，不包含名字价格等

[batteryChoiceEvaluation.ipynb](batteryChoiceEvaluation.ipynb):同[batterChoiceEvaluation.py](batterChoiceEvaluation.py)， [它](batterChoiceEvaluation.py)的jupyter notebook版本

[BatteryChoiceFinal.ipynb](BatteryChoiceFinal.ipynb):枚举后统计并分析，输出电池选择最终版本

[batteryModel.py](batteryModel.py):[battery.py](battery.py)电池的类，第二代，迭代版本

[dailyElectricEstimate.ipynb](dailyElectricEstimate.ipynb):每日电量估计，并输出npy文档

[differenceSolarConsume.py](differenceSolarConsume.py):电池最大电量的V1版本

[flowChart.ipynb](flowChart.ipynb):流程图，弃用

[MouthlyAnalysis.ipynb](MouthlyAnalysis.ipynb):每月的电量消耗和电量产生对比图

[progress_analysis-probability_base.ipynb](progress_analysis-probability_base.ipynb):电池最大电量的V2版本的概率充电版

[progress_analysis.ipynb](progress_analysis.ipynb):电池最大电量的V2版本

[read_data_try.ipynb](read_data_try.ipynb):尝试读取数据，弃用，由[BatteryChoiceFinal.ipynb](BatteryChoiceFinal.ipynb)替代

[solarDataAnalysis.ipynb](solarDataAnalysis.ipynb):每日及其他时间段的图片生成

[solarIteration.ipynb](solarIteration.ipynb):电池类型排列组合，输出csv排列，1/1 - 10/10全排序


## 主要文件夹

[npy](./npy/)： 所有npy文档，imfs弃用

[plot](./plot/)：所有绘图（基本上，部分dpi需要重新生成

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

[plot/Electric_power_capacity_plots](plot/Electric_power_capacity_plots):文件夹下的所有内容为概率电量消耗下的不同阶段的没电的最后24h
