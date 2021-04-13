# set environment
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import ast
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

from sqlalchemy import create_engine, insert
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from config import username
from config import password

# initialize connection with Chrome Driver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

# define our base URL
base_url = "https://www.californiabeaches.com/beaches/"


######################
# first level scrape #
######################
# scrape the regions off the main beach page
browser.visit(base_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser") 

cali_soup = soup.find(id="regions")

# initialize empty county URL list
county_urls = []    
county_url = ""

# scrape lists of counties in each region
region_soup = cali_soup.find_all("ul")


for region in region_soup:
    county_soup = region.find_all("a", href=True)


    for county in county_soup:
        if county:
            # we found one, so pull out the URL
            new_url = county["href"]
            
            # only save one copy of each url
            if new_url != county_url:
                county_url = new_url
                x = county_url.split("/")
                
                # split out the region and county
                # and clean out hyphens
                region = x[-3]
                cnty = x[-2]
                cnty = cnty.replace("-", " ")
                cnty = cnty.replace(" county", "")
                county_urls.append([region.title(), cnty.title(), county_url])
                

#print(len(county_urls))

#######################
# second level scrape #
#######################
# initialize empty area list
area_urls = []    
area_url = ""

# loop through county URLs
for county in county_urls:

    # scrape the county webpage
    browser.visit(county[2])
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    # scrape the list of beaches
    county_soup = soup.find(id="beach-list")
    
    # scrape the links
    area_soup = county_soup.find_all("a", href=True)
    
    for area in area_soup:
        if area:
            # we have one, so pull out the URL
            new_url = area["href"]

            if new_url != area_url:
                area_url = new_url
                x = area_url.split("/")
                
                # split out the area name
                # and clean out hyphens
                curr_area = x[-2]
                curr_area = curr_area.replace("-", " ")
                area_urls.append([county[0], county[1], curr_area.title(), area_url])
                
#print(area_urls)
#print(len(area_urls))


######################
# third level scrape #
######################
# initialize empty beach list
beach_urls = []    
beach_url = ""

for area in area_urls:
    
    # scrape the area page
    browser.visit(area[3])
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    # scrape the list of beaches
    area_soup = soup.find(id="beach-list")
    
    # scrape the links
    beach_soup = area_soup.find_all("a", href=True)
    
    for beach in beach_soup:
        if beach:

            # we found one, so pull out the URL
            new_url = beach["href"]

            if new_url != beach_url:
                beach_url = new_url
                x = beach_url.split("/")
                # split out the beach name and
                # clean out the hyphens
                curr_beach = x[-2]
                curr_beach = curr_beach.replace("-", " ")
                beach_urls.append([area[0], area[1], area[2], curr_beach.title(), beach_url])
                
#print(beach_urls[0])
#print(len(beach_urls))

for beach in beach_urls:
    
    # append an empty dictionary to each beach list
    # to hold beach info
    beach.append({})
    
    try:
        
        # scrape each beach page
        browser.visit(beach[4])
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        # scrape the list of data
        data_soup = soup.find("dl")

        # scrape the titles and data values
        title_soup = data_soup.find_all("dt")
        value_soup = data_soup.find_all("dd")

        i = 0
        
        # save column titles and data
        for title in title_soup:
            
            if title.text == "Address":
                addr_str = str(value_soup[i])
                addr_br = addr_str.split("<br/>")
        
                addr1_br = addr_br[0].split(">")
                beach[5]["address"] = addr1_br[-1]
        
                addr2_br = addr_br[1].split("<")
                
                city_state = addr2_br[0].split()
                
                beach[5]["zip"] = city_state[-1]
                beach[5]["state"] = city_state[-2] 
                beach[5]["city"] = city_state[0].replace(",", "")              
                    
                gmap = ast.literal_eval(value_soup[i].find("span")["data-gmapping"])                
               
                beach[5]["latitude"] = gmap["latlng"]["lat"]
                beach[5]["longitude"] = gmap["latlng"]["lng"]
                
#                print(lat, lng)

        
            elif title.text == "Owner":
                owner = value_soup[i].text
                beach[5]["owner"] = owner
            
                if value_soup[i].a:
                    owner_url = value_soup[i].a["href"]
                    beach[5]["owner_url"] = owner_url
        
            else:
                mod_title = title.text.replace(" ", "_").lower()
                beach[5][mod_title] = value_soup[i].text

                                     
            i+=1


    except Exception as e:
        print(f"Error processing: {beach[4]}, {e}")
        beach[0] = "Not scraped"
        
#    print(beach)

#print(title_list)    
#print(beach_urls[0])

#################
# load database #
#################
# connect to SQL database
engine = create_engine(f"postgresql://{username}:{password}@ec2-54-87-34-201.compute-1.amazonaws.com:5432/ddh5sm9o0kv98b")
connection = engine.connect()

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# create references to our tables
Beaches = Base.classes.beaches

# initiate a database session
session = Session(connection)

# clear database before dump
session.query(Beaches).delete()
session.commit()

# initialize empty list of data titles
title_list = ["address", "city", "state", "zip", "latitude", "longitude", "park_name", "owner", "owner_url", "activities", "amenities", "pet_policy", "fees", "phone", "other_names"]


# loop through all the beaches we scraped
for beach in beach_urls:
    if beach[0] != "Not scraped":
    
        for title in title_list:
            if title not in beach[5]:   
                 beach[5][title] = ""
                    
        if "No " in beach[5]["pet_policy"] or "not allowed" in beach[5]["pet_policy"]:
            # no pets allowed
            pets_allowed = "N"
        else:
            pets_allowed = "Y"
            
        if "free" not in beach[5]["fees"] and "Free" not in beach[5]["fees"]:
            # free parking somewhere near beach
            free_parking = "N"
        else:
            free_parking = "Y"
    
        # add data to database
        new_beach = Beaches(region = beach[0], county = beach[1], area = beach[2], beach_name = beach[3], \
                        beach_url = beach[4], address = beach[5]["address"], city = beach[5]["city"], \
                        state = beach[5]["state"], zip = beach[5]["zip"], latitude = beach[5]["latitude"], \
                        longitude = beach[5]["longitude"], park_name = beach[5]["park_name"], \
                        owner = beach[5]["owner"], owner_url = beach[5]["owner_url"], \
                        activities = beach[5]["activities"], amenities = beach[5]["amenities"], \
                        pet_policy = beach[5]["pet_policy"], pets_allowed = pets_allowed, fees = beach[5]["fees"], \
                        free_parking = free_parking, phone = beach[5]["phone"], other_names = beach[5]["other_names"])
    

        session.add(new_beach)

##################################
# commit all inserts to database #
# ################################       
session.commit()

session.close()