# Intruder: a real time data pipeline to detect oil well interference


## Motivation:

   An oil well on average costs about ~ 8-10 million dollar to start producing. Sometimes the fractures of well drilled on the same pad, adjacent to each other might start interacting with each other. In this case, one of the well will suck the pressure of another well leading to depletion of pressure and eventually oil production of an well.
   Determining well interference at early stage will let you to take corrective action immediately, which in turn will save lot of money for the company.

## Pipeline:

![architecture](https://github.com/rohanguuds/Insight_DE_Project/blob/master/DataPipeline.png)

   I have simulated sensor data coming from oilfield sensors flowing into Kafka. The sensor data is coming from 4 different oil wells. Batch processing will be done on first 3 wells to calculate 90 day cumulative oil production and pressure profiles of this wells. This computing will help to identify if all the wells are running normally. Next, pressure profiles of all the 4 wells are plotted in real time. If there is increase in pressure of any of the well, and decrease in pressuren of well 4 or vice versa, then this would be a classic case of well interference.

## External links:
[Slides](http://bit.ly/Intruder-slides)

[Video](ddddddddd)





