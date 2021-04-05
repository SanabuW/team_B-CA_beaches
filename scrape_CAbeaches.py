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
#from config import password



# initialize connection with Chrome Driver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)



# define our base URL
base_url = "https://www.californiabeaches.com/beaches/"


#######################
#  FIRST LEVEL SCRAPE #
#######################
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
                county_urls.append([region.title(), cnty.title(), county_url])
                

#print(len(county_urls))


#######################
# SECOND LEVEL SCRAPE #
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
# THIRD LEVEL SCRAPE #
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


##############################################
# FINAL SCRAPE -- INDIVIDUAL BEACH PAGES HIT #
##############################################
# initialize empty list of data titles
title_list = []


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

                if "address" not in title_list:
                    title_list.append("address")
                    title_list.append("city")
                    title_list.append("state")
                    title_list.append("zip")
                    title_list.append("latitude")
                    title_list.append("longitude")
        
            elif title.text == "Owner":
                owner = value_soup[i].text
                beach[5]["owner"] = owner
                if "owner" not in title_list:
                    title_list.append("owner")
            
                if value_soup[i].a:
                    owner_url = value_soup[i].a["href"]
                    beach[5]["owner_url"] = owner_url
                    
                    if "owner_url" not in title_list:
                        title_list.append("owner_url")
        
            else:
                mod_title = title.text.replace(" ", "_").lower()
                beach[5][mod_title] = value_soup[i].text
                if mod_title not in title_list:
                    title_list.append(mod_title)
                                     
            i+=1


    except Exception as e:
        print(f"Error processing: {beach[4]}, {e}")
        
#    print(beach)

#print(title_list)    
#print(beach_urls[0])



########################################
# CREATE OBJECT FOR BUILDING DATAFRAME #
########################################
# define static portion of beach dictionary
beach_data = {"region": [], "county": [], "area": [], "beach_name": [], "beach_url": []}

# loop through list of all titles found across all beaches
# and add a dictionary to the beach data
for title in title_list:
    beach_data[title] = []

# loop through all the beaches we scraped
for beach in beach_urls:
    
    # add data to appropriate lists
    beach_data["region"].append(beach[0])
    beach_data["county"].append(beach[1])
    beach_data["area"].append(beach[2])
    beach_data["beach_name"].append(beach[3])
    beach_data["beach_url"].append(beach[4])
    
    for title in title_list:
        if title in beach[5]:
            beach_data[title].append(beach[5][title])
        else:    
            beach_data[title].append("")


###################
# BUILD DATAFRAME #
###################
# dump data into dataframe
beach_df = pd.DataFrame(beach_data)

beach_df["pets_allowed"] = ""
beach_df["free_parking"] = ""

# write dataframe to a CSV file
beach_df.to_csv("data/beach_info.csv")