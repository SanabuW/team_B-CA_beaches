# set environment
from datetime import date
import pandas as pd
import json
import requests

from sqlalchemy import create_engine, insert
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
#from config import password


######################
# retrieve JSON data #
######################
# define our base URL
base_url = "https://admin.beachreportcard.org/api/locations"

# read JSON data from web
r = requests.get(base_url)


#######################################
# create list of all available fields #
#######################################
# create empty list of column names
title_list = []

# loop through water quality data
for row in r.json():
    # grab all the keys from the source dict
    key_list = row["_source"].keys()
    
    # if we find a key we haven't seen
    # before, add it to out list
    for key in key_list:
        if key not in title_list:
            title_list.append(key)
            
#print(title_list)
    

##########################################
# create beach object to build dataframe #
##########################################
# create empty beach dict
beach_data = {}

# loop through list of all titles found across all beaches
# and add an empty array to the beach data for each
for title in title_list:
    # need to break up the geo coordinates
    if title == "geo":
        beach_data["latitude"] = []
        beach_data["longitude"] = []
    else:
        beach_data[title] = []

# loop through all the beaches we scraped
for beach in r.json():
    # we only want cali data
    if beach["_source"]["state"] == "CA":
     
        for title in title_list:
            if title == "alerts":
             # grab current Alerts instead of _source.alerts
                if "currentAlert" in beach:
                    beach_data["alerts"].append(beach["currentAlert"])
                else:
                    beach_data["alerts"].append("")

            # check for data in associated with this key 
            if title in beach["_source"]:
                 # skip if alerts, we got it from currentAlert
                if title == "alerts":
                    continue
                                   
                if title == "geo":
                    # separate coordinates
                    beach_data["latitude"].append(beach["_source"][title][0])
                    beach_data["longitude"].append(beach["_source"][title][1])
                else:
                    # we have data in this field, add it to our array
                    beach_data[title].append(beach["_source"][title])
            else:
                # no data found for this column name --
                # set to null
                beach_data[title].append("")
        

#print(beach_data)
#print(len(beach_data))


####################################################
# build dataframe, get rid of fields we don't need #
# and write to a CSV file                          #
####################################################
# dump data into dataframe
beach_df = pd.DataFrame(beach_data)

# pull out columns of value
beach_df = beach_df[["id", "title", "name1", "latitude", "longitude", "address", "city", "state", "zip", "county", "active", "grade_updated","dry_grade", "wet_grade", "annual_summer_dry", "annual_year_wet", "annual_winter_dry", "annual_year", "grade_created", "alerts"]]

# write dataframe to a CSV file
beach_df.to_csv("data/grade_info.csv")
