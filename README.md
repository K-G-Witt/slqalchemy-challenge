# slqalchemy-challenge
Data on rainfall precipitation (in mm) and daily temperatures (in Celsius) from nine different weather observation stations in the state of Hawaii (HI), USA between 2010-01-01 and 2017-08-23 (i.e., the most recent date for which data are available) were combined to create an API to enable estimation of average precipitation between two user-specified dates.


## Project Description:
This program consists of two separate .csv files that have been combined into one sqlite database, named **hawaii.sqlite**:

1. **hawaii_measurements.csv:** daily precipitation (in mm) and temperature (in Celsius), and;
2. **hawaii_stations.csv:** name, latitude, longitude, and elevation (in m) for each of the nine observation stations.


## Installation and Run Instructions:
Executing the script provided in the **climate_starter.ipynb** file, located in the **SurfsUp** subfolder, will output the following:
1. Histogram of the total daily precipitation (in mm) recorded by the nine weather observation stations between 2016-08-24 amd 2017-08-23;
2. Historgram of the maximum daily temperature (in Celisus) for the most active of the nine weather observation stations between these same dates.


Executing the script provided in the **app.py** file, located in this same subfolder, will launch an API on which users can output the following information in json format:
1. Dictionary of the daily precipitation (in mm) data between 010-01-01 and 2017-08-23;
2. List of the nine weather observation stations;
3. List of temperature (in Celsius) observations for the year between 2016-08-24 amd 2017-08-23 for the most active weather observation station;
4. List of the minimum, average, and maximum temperatures (in Celsius) for any user-specified date (input in YYYY-MM-DD format);
5. List of the minimum, average, and maximum temperatures (in Celsius) between any two user-specified dates (input in YYYY-MM-DD format).


## Credits:
This code was compiled and written by me for the pymaceuticals challenge class homework in the 2024 Data Analytics Boot Camp hosted by Monash University. 
