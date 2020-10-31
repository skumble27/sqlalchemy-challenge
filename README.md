# SQLAlchemy-Challenge

##### Sumukh Kumble

## Planning the Trip

A good vacation is more or less predicated on the weather events that will occur on the planned date. As such, the purpose of this Data Analytics Project is to make reasonable predictions on the weather events that will occur for the trip that is planned to occur on the 1st of July, 2017 and end on the 31st of July, 2017. Therefore, a series of queries using the SQLAlchemy and Pandas Python modules were used to study weather patterns that occurred in the previous year of the planned date in order to gauge what could possibly be expected during the trip.



## Exploratory Data Analysis

#### Precipitation rates from 2016 to 2017

![Precipitation Analysis](https://raw.githubusercontent.com/skumble27/sqlalchemy-challenge/main/Images/precipitation.png)

Based on the previous twelve months of Data from 2016 until 2017, there overall precipitation appears to be quite evenly distributed throughout the year without any indications for specific months or season in which rainfall is the greatest. 

#### Temperature Observations

Within the Dataset, there were 9 stations involved in recording climate events. Base on the analyses, the station with the most activity in data aquisition was **Station USC00519281** with a total observation count of ***<u>2772</u>***.  Within this dataset, the following observations were noted, namely:

1. Lowest recorded temperature was 54.0 °F
2. Highest recorded temperature was 85 °F
3. A temperature average of 71.66 °F

A further observation of the temperature frequencies at this station were noted and plotted below:

![Temp Obs](https://raw.githubusercontent.com/skumble27/sqlalchemy-challenge/main/Images/temperature_at_USC00519523.png)



## Further Analyses on Temperatures (Bonus)

### Temperature Analysis I

A comparison was undertaken to determine if there were significant differences in the average temperature within the month of June as compared to December, which in turn, can provide opportunities to plan the vacation accordingly. From the time of data recording till the last year of 2017, the temperature observations for the entire month of June and December, for all years, were collated and analysed using the unpaired t-test. 

The Mean average temperature for June from 2010 to 2017 was **74.94 °F** whilst the mean temperature average for December, from 2010 to 2017, was **71.04 °F**. Taking these into consideration, the unpaired t-test was applied as the purpose was to examine the temperatures for two different events, namely, the time period. With a P-value significantly less than the designated alpha value of 0.05, we can deduce that there is statistically significant differences between the mean temperatures in June compared to December.

### Temperature Analysis II

Based on the previous years data for the planned vacation in Hawaii, the temperature averages have been calculated and plotted as a bar graph, as shown below:

![Trip Temp Average](https://raw.githubusercontent.com/skumble27/sqlalchemy-challenge/main/Images/Trip_average_temp.png)

In anticipation of the trip being undertaken, the normal temperature seen everyday in the previous year from the 1st of July to the 31st has been analysed and plotted below. This graph in turn, can provide an idea of what kind of weather to expect during the trip in 2017.

![Temp Daily Normal](https://raw.githubusercontent.com/skumble27/sqlalchemy-challenge/main/Images/daily_normals.png)







