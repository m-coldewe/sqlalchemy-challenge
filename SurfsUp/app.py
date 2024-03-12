# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes"""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&ltstart&gt<br/>"
        f"/api/v1.0/&ltstart&gt/&ltend&gt"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of the last 12 months of precipitation data"""
    # Create session link
    session = Session(engine)

    # Query precipitation data
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=366)
    results = session.query(Measurement.date, Measurement.prcp).\
        where(Measurement.date > query_date).\
    all()

    session.close()

    year_precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = prcp
        year_precipitation.append(precipitation_dict)
    
    return jsonify(year_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
    # Create session link
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()

    session.close()
    
    # Convert results into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations"""
    # Create session link
    session = Session(engine)

    # Grab the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    # Set the date range
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=366)
    
    # Query the station data
    results = session.query(Measurement.date, Measurement.tobs, Measurement.station).\
        where(Measurement.date > query_date, Measurement.station == most_active_station).\
    all()

    session.close()

    temperature_observations = []
    for date, tobs, stations in results:
        temperature_dict = {}
        temperature_dict["date"] = date
        temperature_dict["temp"] = tobs
        temperature_observations.append(temperature_dict)

    return jsonify(temperature_observations)

@app.route("/api/v1.0/<start>")
def tstats_start(start):
    
    # Create session link
    session = Session(engine)

    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        group_by(Measurement.date).all()

    session.close()

    tstats_results = []
    for date, tmin, tavg, tmax in results:
        tstats_dict = {}
        tstats_dict["date"] = date
        tstats_dict["tmin"] = tmin
        tstats_dict["tavg"] = tavg
        tstats_dict["tmax"] = tmax
        tstats_results.append(tstats_dict)
    
    return jsonify(tstats_results)

@app.route("/api/v1.0/<start>/<end>")
def tstats(start, end="2017-08-23"):
    
    # Create session link
    session = Session(engine)

    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).\
        group_by(Measurement.date).all()

    session.close()

    tstats_results = []
    for date, tmin, tavg, tmax in results:
        tstats_dict = {}
        tstats_dict["date"] = date
        tstats_dict["tmin"] = tmin
        tstats_dict["tavg"] = tavg
        tstats_dict["tmax"] = tmax
        tstats_results.append(tstats_dict)
    
    return jsonify(tstats_results)


if __name__ == '__main__':
    app.run(debug=True)


