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
    return f"Available Routes:<br/>" f"/api/v1.0/precipitation<br/>" f"/api/v1.0/stations</br>"f"/api/v1.0/tobs</br>"


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


@app.route("/api/v1.0/stations")
def stations():
    """Return a list of active Stations in Hawaii"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    stations_query = session.query(Station.name, Station.station)
    stations = pd.read_sql(stations_query.statement, stations_query.session.bind)
    return jsonify(stations.to_dict())
    

   
    # Query all passengers
  

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)


if __name__ == "__main__":
    app.run(debug=True)
