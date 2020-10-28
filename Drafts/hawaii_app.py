# Importing the flask modue
from flask import Flask, jsonify

# Importing other relevant modules
import numpy as np
import datetime as dt

# Importing SQL Alchemy Modules
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, select

#################################################
# Database Setup
#################################################
engine = create_engine('sqlite:///../Resources/hawaii.sqlite')

# Relfecting an existing database into a new model
Base = automap_base()

# Table Reflection
Base.prepare(engine, reflect=True)

# Setting up the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Creating the Index Route
@app.route("/")
def home():
    return (
        f'Welcome to the Climate Exploration Module, please choose from the following links</br></br>'
        f'Available Routes:<br/>'
        f'/api/v1.0/Tables_columns_in_Data_sets<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/start_date<br/>'
        f'/api/v1.0/Start_End_Date<br/>'
        )

@app.route('/api/v1.0/Tables_columns_in_Data_sets')
def tables_columns():
    # Creating an inspector to explore columns in tables
    inspector = inspect(engine)

    # Columns in Measurement Table
    Measurement_columns = inspector.get_columns('Measurement')

    Station_columns = inspector.get_columns('Station')

    #inspector.close()

    Measurement_columns_names = []
    Station_columns_names = []

    for c in Measurement_columns:
        c_dict = {}
        c_dict['Columns'] = c['name']
        c_dict['Table'] = 'Measurement'
        Measurement_columns_names.append(c_dict)

    
    for s in Station_columns:
        s_dict = {}
        s_dict['Table'] = 'Station'
        s_dict['Columns'] = s['name']
        Station_columns_names.append(s_dict)
    
    
    return jsonify(Measurement_columns_names,Station_columns_names)

 
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Creating a session link to the Database
    session = Session(engine)

    # Querying the Date and Precipitation
    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    # A dictionary is being created in which to append the data from the rows into the
    # precipitation data
    precipitation_data = []
    for date, prcp in results:
        date_prcp_dict = {}
        date_prcp_dict['Date'] = date
        date_prcp_dict['Precipitation'] = prcp
        precipitation_data.append(date_prcp_dict)
    return jsonify(precipitation_data)


@app.route('/api/v1.0/stations')
def stations():
    # Creating a session link to the database
    session = Session(engine)

    # Querying the database for all radio stations
    results_station = session.query(Station.name, Station.station, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    station_lists = []
    
    # Creating a dictionary to append all the details for the Station 
    for stat_name, station, latitude, longitude, elevation in results_station:
        name_stat = {}
        name_stat['Name'] = stat_name
        name_stat['Station'] = station
        name_stat['Latitude'] = latitude
        name_stat['Longitude'] = longitude
        name_stat['Elevation'] = elevation
        station_lists.append(name_stat)
    
    return jsonify(station_lists)

@app.route('/api/v1.0/tobs')
def tobs():
    # Creating a Session Link to the DB from Python
    session = Session(engine)
    
    # Querying the Database
    #### 1 Year worth of Data
    last_date = session.query(Measurement.date).\
        order_by(Measurement.date.desc()).\
            first()
    last_date_dt = dt.datetime.strptime(last_date[0],'%Y-%m-%d')
    query_date = dt.date(last_date_dt.year -1, last_date_dt.month, last_date_dt.day)
    
    #### Querying Data on the Most Active Station
    active_station = session.query(Measurement.station,func.count(Measurement.station)).\
        group_by(Measurement.station).\
            order_by(func.count(Measurement.station).desc()).first()
    # Query the last 12 months of temperature observation data for this station and plot the results as a histogram
    station_top_obs = session.query(Measurement.date,Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= query_date).all()
    
    # Creating a dictionary to append all the data based on the Weather Station with the most observations
    top_weather_station = []

    for date, temp in station_top_obs:
        date_temp_dict = {}
        date_temp_dict['Station'] = active_station[0]
        date_temp_dict['Date'] = date
        date_temp_dict['Temperature'] = temp
        top_weather_station.append(date_temp_dict)
    
    
    return jsonify(top_weather_station)

@app.route('/api/v1.0/start_date')
def startdate():
    # Create a session link from Python to the Database
    session = Session(engine)

    # Selecting a random start date
    random_start_date = session.query(Measurement.date).\
        order_by(func.random()).first()
    
    formatted_random_start_date = dt.datetime.strptime(random_start_date[0],'%Y-%m-%d')
    
    # Querying all the Data from the time of the selected random date
    weather_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= formatted_random_start_date).all()
    session.close()

    # Creating a Dictionary to present weather data from a randomly selected date
    weather_data_list = []

    for minimum, maximum, average in weather_data:
        wdl_dict = {}
        wdl_dict['A Random Start Date'] = str(random_start_date[0])
        wdl_dict['Min Temp'] = minimum
        wdl_dict['Max Temp'] = maximum
        wdl_dict['Average'] = average
        
        weather_data_list.append(wdl_dict)


    return jsonify(weather_data_list)


@app.route('/api/v1.0/Start_End_Date')
def start_end():
     # Create a session link from Python to the Database
    session = Session(engine)

    # Last date
    last_date = session.query(Measurement.date).\
    order_by(Measurement.date.desc()).\
        first()
    
    last_date_dt = dt.datetime.strptime(last_date[0],'%Y-%m-%d')

    # Selecting a random start date
    random_start_date = session.query(Measurement.date).\
        order_by(func.random()).first()
    
    formatted_random_start_date = dt.datetime.strptime(random_start_date[0],'%Y-%m-%d')

    # Using an interval of five years
    query_date = dt.date(formatted_random_start_date.year + 5, formatted_random_start_date.month, formatted_random_start_date.day)

    # Querying all the Data for a five year interval starting from random start date
    fy_weather_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= formatted_random_start_date).\
            filter(Measurement.date <= query_date).all()
    
    session.close()

    # Creating a dictionary to present the data
    five_year_weather_data = []

    for minimum, maximum, average in fy_weather_data:
        fywdl_dict = {}
        fywdl_dict['A Random Start Date'] = str(random_start_date[0])
        fywdl_dict['A Random End Date'] = str(query_date)
        fywdl_dict['Min Temp'] = minimum
        fywdl_dict['Max Temp'] = maximum
        fywdl_dict['Average'] = average
        
        five_year_weather_data.append(fywdl_dict)
        
        return jsonify(five_year_weather_data)


if __name__ == '__main__':
    app.run(debug=True)
