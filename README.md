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

Output for precipitation by date:
![precipitation](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/ca03009b-a7e7-4cfc-a7fd-ea8ae82bb3be)

Judging visually, Honolulu appears to get the most rain in September, followed by late April or early May, and February. 

Histogram  for temperature for the past 12 months:
![tobs](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/2207656e-6a0f-43c1-bb66-ae46ba5b7d20)

Within the past twelve months, the temperature falls most frequently between 75 and 80.

The homepage provides the routes needed to pull the corresponding data.
![app_homepage](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/db3f0ccc-afe5-4d24-af41-88817ab02bf0)


Here's an example of the data returned by the precipitation route:
![precipitation_route](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/7568bab0-41ce-4cf0-aaf8-c07431e9bc2a)


An example of the data returned by the date search route, using a start date and end date.
![tstats](https://github.com/m-coldewe/sqlalchemy-challenge/assets/152045367/21d37c56-b40e-4075-943e-fa8037d53a78)


## Summary

Looking at the data, we can see that Honolulu has generally pleasant temperatures and regular rainfall. To avoid the rainest times of the year, it would be best to visit during the month of October, the month of March, and June. 
