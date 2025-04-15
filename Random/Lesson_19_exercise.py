#---SE370 Lesson 18 Lecture/Exercise---#
#-By: MAJ Matthew wolfe
#-February 2025

#---Key points to hit
#-this class is about connecting to an open API
#-it's getting real, students can crash their kernel or get our IP blocked 
#-for too many API calls
#---Background

###########################################
##### SHIFT + ENTER Each line, don't do all at once!! ########
import sqlite3
from geopy.distance import geodesic
import pandas as pd
import json
import requests

# API's Application Programming Interface is a set of directions
# that allow users to exchange information with each other.  API's
# are used in every app and most websites you interact with.

# The following parameters could be a part of any API request:
# -Base URL (e.g., https://api.example.com)
# -Endpoints (e.g., /v1/data)
# -HTTP Methods (GET, POST, PUT, DELETE)
# -Authentication (API keys, OAuth, JWT)
# -Response Format (JSON, XML)
# -Rate Limits (e.g., 100 requests/min)

# How do i know if a website has a open API?  
# use AI to find out, there are a variety of API's you may want 
# to leverage in your research, projects, capstone or the app you 
# might want to build.

# Ron Swanson API URL is a great way to start!  Anyone can set up an 
# This works by someone running a server with a database of 
# Ron Swanson quotes. 
# 
# We want to connect to that server, and retrieve that database to get a 
# random Ron Swanson quote to make our day.  
#
# API's are accessed through a set of directions between the server
# and the client.  Some API's are open, some need keys  
#

#

url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"

response = requests.get(url)
quote = response.json()[0]
print(f"Ron Swanson says: \'{quote}\'")

# get request to the database of ron-swanson quotes url
# The API returns a list with one quote

print(f"Ron Swanson says: \"{quote}\"")


# The Overpass API is a read-only API that serves up custom selected 
# parts of the OpenStreetMap (OSM) map data. It acts as a database over the web, 
# allowing users to send queries and retrieve corresponding data sets. The Overpass 
# API is free to use for commercial purposes.

# There is even an overpass api specific website: "http://overpass-api.de/api/interpreter" 
# users connect on a 80 or 441 port, your api connection is a 
# this means your internet web page won't bring this api website up.

# Chat GPT can help with the API connection to overpass, or you can read this wiki: 
# https://wiki.openstreetmap.org/wiki/Overpass_API



# Define HNL Airport Coordinates, we will need this later
hnl_coords = (21.3245, -157.9253)

# There is a URL that gives us a live update for the overpass API
# https://overpass-api.de/api/status
# If the api has 4 active connections you may receive an error
# 
#
#
# Overpass API instruction for Query to get ALL locations within 50km of HNL
# This give us the widest possible pull of data, we will use python to filter
# Overpass gives instruction on how we access their open api
# overpass_urls = [
# 
# Alternate API URL
# "https://overpass-api.de/api/interpreter"
#  
#  
overpass_url = "https://overpass.kumi.systems/api/interpreter"
overpass_query = f"""
[out:json];
(
  node(around:10000,21.3245,-157.9253);
  way(around:10000,21.3245,-157.9253);
  rel(around:10000,21.3245,-157.9253);
);
out center; 
"""
# The Above are just the instructions for the connection, it doesn't connect yet 
# outputs are set to latitude/longitude in JSON format
# return provides OpenStreetMap (OSM) data, the JSON consists of: 
# Version of OSM schema, timestamp when the dta was last updated, copyright data
# 
# WARNING WARNING WARNING!!!!!!
# DO NOT KEEP SHIFT ENTERING THE FOLLOWING RESPONSE LINES!
# Fetch data from Overpass API
# you can run a print statement at the same time as your variables to help you understand what is happening

print("Fetching data from Overpass API...") # informs you your initiating a request.get
response = requests.get(overpass_url, params = {'data': overpass_query})
data = response.json()
print('api request complete')


print("Fetch from overpass API complete") # only runs after data = response.json() completes


#This gives us the response JSON the website returns to us.
# It is to large to read there are over 1 million items, we can preview the JSON 
# through the following to print the first 3 locations

print(json.dumps(data["elements"][:3], indent =2))

# we don't want to get all "elements", but lets see what it returned
# most attributes we want to pick out and put on a map is data
# within the "tags"

# How many seperate elements did we pull from our querie?
num_elements = len(data.get("elements", []))
print(f"locations fetched from API: {num_elements}")

# that's hundreds of thousands of icons that could be put on a map!!!, 
# we need to filter this down
# Extract only elements that have locations, valid names
# of interest in our trip to Honolulu.  
# 1 Create a locations list
# 2 filter out only elements that have a location
# 3 filter out elements that only have a valid "name"
#########################

# Step 1: extract list of elements, lat, lon
raw_data = []
for element in data["elements"]:
    # Extract latitude & longitude
    if "lat" in element and "lon" in element:
        lat, lon = element["lat"], element["lon"]
    elif "center" in element:  # For 'way' elements
        lat, lon = element["center"]["lat"], element["center"]["lon"]
    else:
        lat, lon = None, None  # Keep empty values

    # Extract name and all available tags
    name = element.get("tags", {}).get("name", None) #Will return tags with no name, we will filter later
    tags = element.get("tags", {})
    
    # Store all raw data
    raw_data.append({
        "id": element.get("id"),
        "type": element.get("type"),
        "latitude": lat,
        "longitude": lon,
        "name": name,
        "tags": tags  # Store tags as a dictionary for later filtering
    })

# Convert raw data into a DataFrame
df_filtered = pd.DataFrame(raw_data)  # run with print statement below.... 
#then make a typo on this line to show that your print statement can act as a confirmation of successful code
print(f"converted raw data list to dataframe with {len(df_filtered)} rows.")

#lets do a little more analyses of our data



# Step 2: Filter DataFrame for places with that actually have a name


# Step 3: Extract place types into a new column and filter valid place types
# Under type node there are some tags that would be good if we want 
# to travel to Hawaii and have a vacation
def extract_place_type(tags):
    return tags.get("amenity") or tags.get("shop") or tags.get("tourism") or \
           tags.get("leisure") or tags.get("historic")



# Step 4: Extract place

# only assigns an identified tag above 


# Step 5: Only keep Place Types with data



# Drop any duplicates from our data that have the same lon, lat and name
# Ensure we have no duplicate locations that may have been listed under seperate tags



# Add calculation of distance from our original HNL location to any of the location
# Road distance calculations would need additional API's and a lot of processing power

def calculate_distance(row):
    if pd.notna(row["latitude"]) and pd.notna(row["longitude"]):
        return geodesic(hnl_coords, (row["latitude"], row["longitude"])).km
    return None



# only keep locations within 8 km
df_named.loc[:, "distance_km"] = df_named.apply(calculate_distance, axis=1)
df_named = df_named[df_named["distance_km"] <= 8]

#we don't need tags or type columns we extracted what we needed drop those columns

print(f"locations after filtering within 10km: {len(df_named)}")

################################################################################################################################################################################################################################### ASK DURING AI

#########################
#SQL DB
# KEY ACTION: Connect to SQLite Database (Creates it if no instance exists)


# We can create a table of our data in SQL lite that runs in our python environment, 
# print statement confirms there was no error
# There is no data in this table after we create it, next step is to write data to it

cursor.execute("DROP TABLE IF EXISTS locations;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS locations (
    db_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id INTEGER,
    name TEXT
    latitude REAL
    longitude REAL,
    place_type TEXT,
    distance_km REAL           
)
""")
print("locations table created")

 #only run if you have previous data


# this is a blank table with no data


# Insert data into SQLite, print statement confirms the write with no error

df_named.to_sql('locations', conn, if_exists = 'append', index = False)

print(f"Successfully inserted {len(df_named)} records into SQLite.")

# KEY ACTION: Commit and close
conn.commit()
conn.close()

# KEY ACTION: Connect, fetch, close
# Pull the data from SQL "locations.db", this file persists and can be accessed in your file directory

#---SE370 Lesson 18 Lecture/Exercise---#
#-By: MAJ Matthew wolfe
#-February 2025

#---Key points to hit
#-this class is about connecting to an open API
#-it's getting real, students can crash their kernel or get our IP blocked
#-for too many API calls
#---Background

###########################################
##### SHIFT + ENTER Each line, don't do all at once!! ########
import requests
import sqlite3
from geopy.distance import geodesic
import pandas as pd
import json

# API's Application Programming Interface is a set of directions
# that allow users to exchange information with each other.  API's
# are used in every app and most websites you interact with.

# The following parameters could be a part of any API request:
# -Base URL (e.g., https://api.example.com)
# -Endpoints (e.g., /v1/data)
# -HTTP Methods (GET, POST, PUT, DELETE)
# -Authentication (API keys, OAuth, JWT)
# -Response Format (JSON, XML)
# -Rate Limits (e.g., 100 requests/min)

# How do i know if a website has a open API?  
# use AI to find out, there are a variety of API's you may want
# to leverage in your research, projects, capstone or the app you
# might want to build.

# Ron Swanson API URL is a great way to start!  Anyone can set up an
# This works by someone running a server with a database of
# Ron Swanson quotes.
#
# We want to connect to that server, and retrieve that database to get a
# random Ron Swanson quote to make our day.  
#
# API's are accessed through a set of directions between the server
# and the client.  Some API's are open, some need keys  
#

#

url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"
response = requests.get(url)
response.content
quote = response.json()[0]
# get request to the database of ron-swanson quotes url
# The API returns a list with one quote

print(f"Ron Swanson says: \"{quote}\"")


# The Overpass API is a read-only API that serves up custom selected
# parts of the OpenStreetMap (OSM) map data. It acts as a database over the web,
# allowing users to send queries and retrieve corresponding data sets. The Overpass
# API is free to use for commercial purposes.

# There is even an overpass api specific website: "http://overpass-api.de/api/interpreter"
# users connect on a 80 or 441 port, your api connection is a
# this means your internet web page won't bring this api website up.

# Chat GPT can help with the API connection to overpass, or you can read this wiki:
# https://wiki.openstreetmap.org/wiki/Overpass_API



# Define HNL Airport Coordinates, we will need this later
hnl_coords = (21.3245, -157.9253)

# There is a URL that gives us a live update for the overpass API
# https://overpass-api.de/api/status
# If the api has 4 active connections you may receive an error
#
#
#
# Overpass API instruction for Query to get ALL locations within 50km of HNL
# This give us the widest possible pull of data, we will use python to filter
# Overpass gives instruction on how we access their open api
# overpass_urls = [
#
# Alternate API URL
# "https://overpass-api.de/api/interpreter"
#  
#  
overpass_url = "https://overpass.kumi.systems/api/interpreter"
overpass_query = f"""
[out:json];
(
  node(around:10000,21.3245,-157.9253);
  way(around:10000,21.3245,-157.9253);
  rel(around:10000,21.3245,-157.9253);
);
out center;
"""
# The Above are just the instructions for the connection, it doesn't connect yet
# outputs are set to latitude/longitude in JSON format
# return provides OpenStreetMap (OSM) data, the JSON consists of:
# Version of OSM schema, timestamp when the dta was last updated, copyright data
#
# WARNING WARNING WARNING!!!!!!
# DO NOT KEEP SHIFT ENTERING THE FOLLOWING RESPONSE LINES!
# Fetch data from Overpass API
# you can run a print statement at the same time as your variables to help you understand what is happening

print("Fetching data from Overpass API...") # informs you your initiating a request.get
response = requests.get(overpass_url, params = {'data': overpass_query})
data = response.json()
print("Fetch from overpass API complete") # only runs after data = response.json() completes


#This gives us the response JSON the website returns to us.
# It is to large to read there are over 1 million items, we can preview the JSON
# through the following to print the first 3 locations

print(json.dumps(data["elements"][:3], indent =2))

# we don't want to get all "elements", but lets see what it returned
# most attributes we want to pick out and put on a map is data
# within the "tags"

# How many seperate elements did we pull from our querie?
num_elements = len(data.get("elements", []))
print(f"locations fetched from API: {num_elements}")

# that's hundreds of thousands of icons that could be put on a map!!!,
# we need to filter this down
# Extract only elements that have locations, valid names
# of interest in our trip to Honolulu.  
# 1 Create a locations list
# 2 filter out only elements that have a location
# 3 filter out elements that only have a valid "name"
#########################

# Step 1: extract list of elements, lat, lon
raw_data = []
for element in data["elements"]:
    # Extract latitude & longitude
    if "lat" in element and "lon" in element:
        lat, lon = element["lat"], element["lon"]
    elif "center" in element:  # For 'way' elements
        lat, lon = element["center"]["lat"], element["center"]["lon"]
    else:
        lat, lon = None, None  # Keep empty values

    # Extract name and all available tags
    name = element.get("tags", {}).get("name", None) #Will return tags with no name, we will filter later
    tags = element.get("tags", {})
   
    # Store all raw data
    raw_data.append({
        "id": element.get("id"),
        "type": element.get("type"),
        "latitude": lat,
        "longitude": lon,
        "name": name,
        "tags": tags  # Store tags as a dictionary for later filtering
    })

# Convert raw data into a DataFrame
df_filtered = pd.DataFrame(raw_data)  # run with print statement below....
#then make a typo on this line to show that your print statement can act as a confirmation of successful code
print(f"converted raw data list to dataframe with {len(df_filtered)} rows.")

#lets do a little more analyses of our data
df_filtered.head()
df_grouped = df_filtered.groupby('type').size().reset_index(name = 'count')
df_grouped

# Step 2: Filter DataFrame for places with that actually have a name
df_named = df_filtered[(df_filtered['name'].notna())]
df_named.head()
print(f'locations with names: {len(df_named)}')

# Step 3: Extract place types into a new column and filter valid place types
# Under type node there are some tags that would be good if we want
# to travel to Hawaii and have a vacation
def extract_place_type(tags):
    return tags.get("amenity") or tags.get("shop") or tags.get("tourism") or \
           tags.get("leisure") or tags.get("historic")



# Step 4: Extract place
df_named.loc[:, 'place_type'] = df_named['tags'].apply(extract_place_type)
# only assigns an identified tag above


# Step 5: Only keep Place Types with data
df_named = df_named[(df_named['place_type'].notna())]




# Drop any duplicates from our data that have the same lon, lat and name
# Ensure we have no duplicate locations that may have been listed under seperate tags



# Add calculation of distance from our original HNL location to any of the location
# Road distance calculations would need additional API's and a lot of processing power

def calculate_distance(row):
    if pd.notna(row["latitude"]) and pd.notna(row["longitude"]):
        return geodesic(hnl_coords, (row["latitude"], row["longitude"])).km
    return None

df_named.loc[:, 'distance_km'] = df_named.apply(calculate_distance, axis = 1)

#check how many locations were filtered

print(f'locations after filering within 10km: {len(df_named)}')

# only keep locations within 8 km
df_named.loc[:, "distance_km"] = df_named.apply(calculate_distance, axis=1)
df_named = df_named[df_named["distance_km"] <= 8]

#we don't need tags or type columns we extracted what we needed drop those columns




#########################
#SQL DB
# KEY ACTION: Connect to SQLite Database (Creates it if no instance exists)
conn = sqlite3.connect('locations.db')
cursor = conn.cursor()


# We can create a table of our data in SQL lite that runs in our python environment,
# print statement confirms there was no error
# There is no data in this table after we create it, next step is to write data to it
cursor.execute('DROP TABLE IF EXISTS locations;')
 #only run if you have previous data
cursor.execute("""
create table if not exists locations (
    db_id integer primary key autoincrement,
    id integer,
    name text,
    latitude real,
    longitude real,
    place_type text,
    distance_km real
)
""")
print('locations table created.')

# this is a blank table with no data


# Insert data into SQLite, print statement confirms the write with no error
df_named.to_sql('locations', conn, if_exists = 'append', index = False)

print(len(df_named))
# KEY ACTION: Commit and close


# KEY ACTION: Connect, fetch, close
# Pull the data from SQL "locations.db", this file persists and can be accessed in your file directory

