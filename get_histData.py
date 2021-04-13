# set environment
from datetime import date
import pandas as pd
import json
import requests

from sqlalchemy import create_engine, insert
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from config import username
from config import password

# define our current grade data url
grade_url = "https://admin.beachreportcard.org/api/locations"

# read JSON data from web
gr = requests.get(grade_url)

#print(gr.json())
# create list of column names
key_list = ["title", "name1", "geo", "address", "city", "state", "zip", "county"]

# create empty beach dict
beach_data = {}


# loop through all the beaches we scraped
for beach in gr.json():
    # we only want cali data
    if beach["_source"]["state"] == "CA":
        
        # add dictionary entry, key = id, value = {}
        beach_data[beach["_source"]["id"]] = {}

        # loop through the list of keys we want to pull from this dataset
        for key in key_list:
               
            # check for data associated with this key
            if key in beach["_source"]:
                    
                if key == "geo":
                    # separate coordinates
                    beach_data[beach["_source"]["id"]]["latitude"] = beach["_source"][key][0]
                    beach_data[beach["_source"]["id"]]["longitude"] = beach["_source"][key][1]
                else:
                    # we have data in this field, add it to our array
                    beach_data[beach["_source"]["id"]][key] = beach["_source"][key]
            else:
                # no data found for this column name --
                # set to empty string
                beach_data[beach["_source"]["id"]][key] = ""
                
#print(beach_data)
        
# define our historical data URL
hist_url = "https://admin.beachreportcard.org/api/grades"

# read JSON data from web
hist = requests.get(hist_url)

#print(len(hist.json()))

# connect to SQL database
engine = create_engine(f"postgresql://{username}:{password}@ec2-54-87-34-201.compute-1.amazonaws.com:5432/ddh5sm9o0kv98b")
connection = engine.connect()

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# create references to our tables
Grade_data = Base.classes.grade_data

# initiate a database session
session = Session(connection)

# clear database before dump
session.query(Grade_data).delete()
session.commit()

# loop through the array of historical entries,
# populate missing data with data from current grade data

for row in hist.json():
    if row["_source"]["LocationId"] in beach_data:

        new_grade = Grade_data(json_id = row["_source"]["LocationId"], \
                                name1 = beach_data[row["_source"]["LocationId"]]["name1"], \
                                latitude = beach_data[row["_source"]["LocationId"]]["latitude"], \
                                longitude = beach_data[row["_source"]["LocationId"]]["longitude"], \
                                address = beach_data[row["_source"]["LocationId"]]["address"],\
                                city = beach_data[row["_source"]["LocationId"]]["city"], \
                                state = beach_data[row["_source"]["LocationId"]]["state"], \
                                zip = beach_data[row["_source"]["LocationId"]]["zip"], \
                                county = beach_data[row["_source"]["LocationId"]]["county"], \
                                grade_updated = row["_source"]["GradeDate"], \
                                dry_grade = row["_source"]["DryGrade"], \
                                wet_grade = row["_source"]["WetGrade"], \
                                active = "", annual_summer_dry = "", annual_year_wet = "", annual_winter_dry = "", \
                                annual_year = "", grade_created = row["_source"]["GradeDate"])
        session.add(new_grade)

session.commit()

session.close()