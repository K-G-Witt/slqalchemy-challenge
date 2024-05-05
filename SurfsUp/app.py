# Import the dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with = engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
# Create an app, being sure to pass __name)__
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# Homepage:
@app.route("/")
def homepage():
    return (f"Welcome to my sqlalchemy-challenge API homepage!<br/>"
            f"Available routes:<br/>"
            f"Data on precipitation (mm): /api/v1.0/precipitation<br/>"
            f"List of stations: /api/v1.0/stations<br/>"
            f"Temperature observations for the most active station: /api/v1.0/tobs<br/>"
            f"Start date(yyyy-mm-dd): /api/v1.0/<start><br/>"
            f"Start-End date(yyyy-mm-dd) to date(yyyy-mm-dd): /api/v1.0/<start>/<end>")

# Precipitation:
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()
    all_precipitation_data = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation_data.append(precipitation_dict)

    return jsonify(all_precipitation_data)
   
# Stations:
@app.route("/api/v1.0/stations")  
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()

    session.close()
    all_station_data = list(np.ravel(results))
    return jsonify(all_station_data)

# TOBS for most active station over past 12 months:
@app.route("/api/v1.0/tobs") 
def tobs():
    session = Session(engine)
    most_active_station_id = session.query(Measurement.station).\
                                group_by(Measurement.station).\
                                order_by(func.count().desc()).\
                                first()[0]

    results = session.query(Measurement.date, Measurement.tobs).\
                        filter(Measurement.date >= "2016-08-24").\
                        filter(Measurement.date <= "2017-08-23").\
                        filter(Measurement.station == most_active_station_id).all()

    session.close()
    most_active_station_tobs_data = list(np.ravel(results))
    return jsonify(most_active_station_tobs_data)

# Start Date:
@app.route("/api/v1.0/<start_date>") 
def start_date(start_date):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))

    session.close()
    start_date_tobs = []
    for min, avg, max in results:
        start_date_tobs_dict = {}
        start_date_tobs_dict["min"] = min
        start_date_tobs_dict["avg"] = avg
        start_date_tobs_dict["max"] = max
        start_date_tobs.append(start_date_tobs_dict)

    return jsonify(start_date_tobs)

# Start-End Date Range:
@app.route("/api/v1.0/<start_date>/<end_date>") 
def start_end_date(start_date, end_date):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()
    start_end_date_tobs = []
    for min, avg, max in results:
        start_end_date_tobs_dict = {}
        start_end_date_tobs_dict["min"] = min
        start_end_date_tobs_dict["avg"] = avg
        start_end_date_tobs_dict["max"] = max
        start_end_date_tobs.append(start_end_date_tobs_dict)

    return jsonify(start_end_date_tobs)

           
#################################################
# Run
#################################################
if __name__ == "__main__":
    app.run(debug=True)