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

# define our base URL
base_url = "https://admin.beachreportcard.org/api/locations"

# read JSON data from web
gr = requests.get(base_url)

# create empty list of column names
title_list = []

# loop through water quality data
for row in gr.json():
    # grab all the keys from the source dict
    key_list = row["_source"].keys()
    
    # if we find a key we haven't seen
    # before, add it to out list
    for key in key_list:
        if key not in title_list:
            title_list.append(key)
            
#print(title_list)
    
# create empty beach dict
beach_data = []

#print(beach_data)

# loop through all the beaches we scraped
for beach in gr.json():
    # we only want cali data
    if beach["_source"]["state"] == "CA":
        
        curr_beach = {}

        # no date associated -- don't want it
        if "grade_updated" not in beach["_source"]:
            continue

        for title in title_list:

            # check for data in associated with this key
            if title in beach["_source"]:
                # skip if alerts, we got it from currentAlert
                if title == "alerts":
                    continue
                    
                if title == "geo":
                    # separate coordinates
                    curr_beach["latitude"] = beach["_source"][title][0]
                    curr_beach["longitude"] = beach["_source"][title][1]
                else:
                    # we have data in this field, add it to our array
                    curr_beach[title] = beach["_source"][title]
            else:
                # no data found for this column name --
                # set to null
                curr_beach[title] = ""
                
        beach_data.append(curr_beach)
        

#print(beach_data)

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

for beach in beach_data:
    
    # check database for existence of grade data
    # based on id and grade updated
    result = session.query(Grade_data.id).filter(Grade_data.json_id == beach["id"]) \
                                         .filter(Grade_data.grade_updated == beach["grade_updated"]).first()
    if result is None:
        # new grade data, so insert
        new_grade = Grade_data(json_id = beach["id"], name1 = beach["name1"], \
                                latitude = beach["latitude"], longitude = beach["longitude"], \
                                address = beach["address"],city = beach["city"], state = beach["state"], \
                                zip = beach["zip"], county = beach["county"], \
                                grade_updated = beach["grade_updated"], \
                                dry_grade = beach["dry_grade"], wet_grade = beach["wet_grade"], \
                                active = beach["active"], annual_summer_dry = beach["annual_summer_dry"], \
                                annual_year_wet = beach["annual_year_wet"], \
                                annual_winter_dry = beach["annual_winter_dry"], annual_year = beach["annual_year"], \
                                grade_created = beach["grade_created"])
                
        session.add(new_grade)

session.commit()

session.close()