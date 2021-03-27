# Beach Report - Team B

## Proposal

Group: Kate Spitzer, Sanabu Washizuka, Jonathan Hicks

Tools: HTML, JS, Leaflet, Plotly, Leaflet time data plugins (LeafletPlayback, Leaflet.timeline)

Datasets:
https://www.californiabeaches.com/beaches/
https://beachreportcard.org/33.91029999999999/-118.51929100000001/11
https://admin.beachreportcard.org/api/locations

Beach Report Card: Available Data:

- Beach Name
- City
- County
- Geo (Lat/Lng)
- Wet Grade
- Dry Grade
- Comments

### Questions

###### Who is our audience? 
People in California - general public &/or people visiting
###### Which decision is going to be made?
Providing more interactivity and cleanliness of the data, and providing other visualizations where it is easier to compare different beaches without having to click on each beach to see its info.
###### Updates
Reports on wet/dry grade are not always on a daily basis, as some beaches get grades every other day. Updating the database every few days would likely be our route.
###### Why is this important?
It allows users to filter the data in an easier fashion, and to hone in on different factors as people have different wants and needs for the beach they choose (such as water quality, free parking, etc.)

### Considerations

###### How do we want to clean the data?
- Access the api and store into a mongo database.
- Referencing the data in python (or js) from mongo and grabbing necessary columns for functions needed to build our leaflet map and bar chart.
- What is the timeframe we want to explore? (TBD)
- What interactivity do we want to implement?
- Filters on the map where they can show beaches only with good water grades, or by other factors. (Still TBD)
