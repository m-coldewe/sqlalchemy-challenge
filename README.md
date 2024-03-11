# sqlalchemy-challenge
Climate analysis of Honolulu, Hawaii.

# Climate Analysis of Honolulu, Hawaii

## Overview

This project performs a basic climate analysis and sets up a Flask API based on the queries. Utilizes SQLAlchemy, Pandas, Matplotlib, and Flask.

## Purpose

The first part of this project performs basic climate analysis within Jupyter Notebook using Pandas and SQLAlchemy. The analysis starts with the most recent date in the sqlite database, which is used as the anchor to collect a year's worth of data. That data is then used to look at the precipitation by date across all locations, and to look at the summary statistics. 

From there, we pivot to analysis by station. From the list of stations, the code grabs the most active station, and uses that station's data to find the lowest temperature, the highest temperature, and the average for that station. 

The second part of the project creates a Flask API using the data queried in the first part. The APi consists of six routes: home, precpitation, stations, temperature for the most active station for the previous year, an route that let the user search either by start date, or by start date and end date. 

## Result

![app_homepage](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/aa6a52a5-31a8-4e2b-87ee-c61bee80b2ed)

![precipitation](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/ca03009b-a7e7-4cfc-a7fd-ea8ae82bb3be)

![tobs](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/2207656e-6a0f-43c1-bb66-ae46ba5b7d20)



## Summary
Conclusions of analysis and final words.
