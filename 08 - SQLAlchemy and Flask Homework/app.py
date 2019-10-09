import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (f"Available Routes:<br/>"
    f"<br/>"
    f"<br/>"
    f"/api/v1.0/precipitation<br/>"
    f" - List of previous year's rainfall by date"
    f"<br/>" 
    f"<br/>"
    f"/api/v1.0/stations</br>"
    f" - List of Stations in Hawaii"
    f"<br/>"
    f"<br/>" 
    f"/api/v1.0/tobs</br>"
    f" - List of previous year's temperatures in Hawaii by date "
    f"<br/>"
    f"<br/>"
    f"/api/v1.0/start</br>"
    f" - Provides low, average, and high temperature of dates before and including the given date('YY-MM-DD' format)"
    f"<br/>"
    f"<br/>"
    f"/api/v1.0/start/end</br>"
    f" -  Provides low, average, and high temperature of date range provided<br/>")

###############################################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of rain fall for prior year"""
    session = Session(engine)
    
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    date_last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= date_last_year).order_by(Measurement.date).all()
   
    
    precipitation_total = []
    for result in precipitation:
        row = {}
        row["date"] = precipitation[0]
        row["prcp"] = precipitation[1]
        precipitation_total.append(row)
    return jsonify(precipitation_total)
    
########################################################################

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of active Stations in Hawaii"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    stations_query = session.query(Station.name, Station.station)
    stations = pd.read_sql(stations_query.statement, stations_query.session.bind)
    return jsonify(stations.to_dict())
######################################################################################
@app.route("/api/v1.0/tobs")
def tobs():
    """Return temperature observations a year from August 23, 2017"""
    session = Session(engine)
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    date_last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_query = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date >= date_last_year).order_by(Measurement.date).all()
    
    temperature_ly = []
    for result in tobs_query:
       row = {}
       row["date"] = tobs_query[0]
       row["tobs"] = tobs_query[1]
       temperature_ly.append(row)
    return jsonify(temperature_ly)

######################################################################################################

@app.route("/api/v1.0/<start>")
def tripA(start):
    """Return low, average, and high temperature of a year from start date"""
    session = Session(engine)
    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    last_year = dt.timedelta(days=365)
    start = start_date-last_year
    end =  dt.date(2017, 8, 23)

    trip_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    trip = list(np.ravel(trip_data))
    return jsonify(trip)

#############################################################

@app.route("/api/v1.0/<start>/<end>")
def tripB(start,end):
    """Return low, average, and high temperature of a year from date range given"""
    session = Session (engine)
    start_date= dt.datetime.strptime(start, '%Y-%m-%d')
    end_date= dt.datetime.strptime(end,'%Y-%m-%d')
    last_year = dt.timedelta(days=365)
    start = start_date-last_year
    end = end_date-last_year
    trip_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    trip = list(np.ravel(trip_data))
    return jsonify(trip)


if __name__ == "__main__":
    app.run(debug=True)
