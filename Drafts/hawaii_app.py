# Importing the flask modue
from flask import Flask, jsonify

# Importing other relevant modules
import numpy as np

# Importing SQL Alchemy Modules
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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

# Creating the Index Route
@app.route("/")
def home():
    return (
        f'Welcome to the Climate Exploration Module, please choose from the following links'
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start><br/>'
        f'/api/v1.0/<start>/<end>'
    )

if __name__ == '__main__':
    app.run(debug=True)
