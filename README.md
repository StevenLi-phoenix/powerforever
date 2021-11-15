# solarPowerEstimate


### <center>Team control number</center>

# <center>11691</center>

### <center>Problem Chosen</center>

# <center>A</center>

### <center>2021 HiMCM Program Part</center>

author: Stevenli

time: 2021.11.7

revise: 2021.11.15

### Abstract:
#### Power forever, Electricity wherever
With the continuous development of photovoltaic power generation technology, the construction of off- grid photovoltaic microgrid systems for households in remote areas has become an extremely attractive solution. However, photovoltaic power generation is subject to certain randomness and intermittentness due to meteorological factors. In order to improve the power supply reliability of photovoltaic off-grid homes, a reasonable configuration of energy storage systems is essential.

In order to solve the above problems, we mainly adopt the following steps:
First, we establish a local photovoltaic output model by analyzing factors such as the user's location, meteorological conditions, and residential area. Meanwhile, we establish a user's household load power consumption model by analyzing the individual user's household load type, power, use time, and use period. Considering that the model maintains a certain generality, we evaluate the user's household load power model by introducing a normal distribution, and analyze the influence of different seasons and different time periods on the user's household power load model.

Secondly, we determine the number of annual power outages of users as the primary technical indicator of power supply reliability. By combining the photovoltaic output model and the household electric load model, the minimum capacity and power of the energy storage battery system that the household needs to configure within a given range of power outages are solved.

Further, taking the minimum capacity and power of the storage battery system and the cost acceptable to the user as constraints, we construct an storage battery library and select the main technical indicators that users are more concerned about, including cost per kilowatt-hour, power density, energy density, price, efficiency and life span, etc., and comprehensively consider setting weighting factors according to the actual needs of users, establish a comprehensive system evaluation function, and obtain the optimal configuration of storage batteries: when the user's cost is constrained to less than 8,000 US dollars, no matter how the energy storage battery is configured, it cannot guarantee that the number of power outages in a year is less than 5; when the user cost increases to 10,000 US dollars, one can be configured A Tesla Powerwall+ battery and a FREEDOH Battery to make the number of power outages for users less than 2 times per year; when the user's cost increases to 15,000 US dollars, you can configure a RIYIFER Battery, an Ultimate Battery and a Tesla Powerwall+ battery to keep users being powered for the whole year.

Finally, we further investigated a more environmentally friendly emerging technology-cement battery. Compared with chemical batteries, cement energy storage batteries use fewer precious metals, and can be produced and used on a larger scale, which is more in line with the development direction of large-scale energy storage battery applications. Although the technology is still immature, but its environmental protection, large-scale construction and other characteristics meet the needs of environmental protection and future sustainable development, so it has great development potential.

<h4>Keywords:</h4> Optimized design of ESS, power supply reliability, evaluation function, customization.

### [A letter to Off-Grid Photovoltaic Families](letter.md)

## Requirements:
    pandas
    numpy
    matplotlib.pyplot


## Battery component：
battery.py
batteryModel.py

## Main File:

[analysisDifferatialSolarAndPowerSupply.ipynb](analysisDifferatialSolarAndPowerSupply.ipynb): Minum capacity in average situation.

[batterAnalysis.ipynb](batterAnalysis.ipynb): Abandon

[batterChoiceEvaluation.py](batterChoiceEvaluation.py): Final version of enumeration result

[battery.py](battery.py): first version of battery component.

[batteryChoiceEvaluation.ipynb](batteryChoiceEvaluation.ipynb):same as [batterChoiceEvaluation.py](batterChoiceEvaluation.py): jupyter version of [batterChoiceEvaluation.py](batterChoiceEvaluation.py).

[BatteryChoiceFinal.ipynb](BatteryChoiceFinal.ipynb):Enumeration statistics and analysis, output battery selection final version.

[batteryModel.py](batteryModel.py):Improved version of [battery.py](battery.py).

[dailyElectricEstimate.ipynb](dailyElectricEstimate.ipynb):Daily power estimate and output NPY document.

[differenceSolarConsume.py](differenceSolarConsume.py):Estimate the maximum and minimum charge of the battery V1 version.

[flowChart.ipynb](flowChart.ipynb):flow chart, abandon.

[MouthlyAnalysis.ipynb](MouthlyAnalysis.ipynb):Monthly electricity consumption and electricity generation comparison chart

[progress_analysis-probability_base.ipynb](progress_analysis-probability_base.ipynb):Second version of maximum battery estimation based on probability data

[progress_analysis.ipynb](progress_analysis.ipynb):Second version of maximum battery estimation

[read_data_try.ipynb](read_data_try.ipynb):attemp reading data, use [BatteryChoiceFinal.ipynb](BatteryChoiceFinal.ipynb) instead.

[solarDataAnalysis.ipynb](solarDataAnalysis.ipynb):Daily and other time frame generation

[solarIteration.ipynb](solarIteration.ipynb):Battery type arrangement and combination, output CSV arrangement, 1/1-10/10 full sort, abandon.


## Main folder

[npy](./npy/): All NPY documents, abandon imfs.

[plot](./plot/): All picture output, Some images need to be output at higher DPI

[py](./py/): Convert All *.ipynb files to *.py files

[other](./other/): Preparation and other reference stuff

--------------------------------------------
[original version (ZH)](README_original.md)

--------------------------------------------
