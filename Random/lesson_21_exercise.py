#---SE370 Lesson 21 Lecture/Exercise---#
#-By: Ian Kloo
#-March 2025

#---Background
#-intro to working with geospatial data in Python

#---Objectives
#-know usecases for geospatial analysis
#-know how to read and write geospatial data in Python
#-understand the concept of projections

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

#-geopandas basics
#read in starbucks data
df = pd.read_csv('Starbucks.csv')
#explore the data to get a sense for what is in there
df.shape
df.head()
#plot the lat/long with a matplotlib scatterplot
fig, ax = plt.subplots()
ax.scatter(df['Longitude'], df['Latitude'])
plt.show()

#read in as a geopandas dataframe
gdf = gpd.GeoDataFrame(df)
df.head()
type(df)
gdf.head()
type(gdf)

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
gdf.head()
#-Coordinate Reference Systems (CRS) and projections
#the reason thigns look distorted before is because we are plotting lat/long on a flat surface
#Lat/Long is a spherical coordinate system, but we are plotting on a flat surface (x/y)
#we need to use a projection to convert the lat/long to x/y

#first let's check the current CRS - it is inhereted rom the file used to create the geodataframe
gdf.crs
gdf.plot(markersize=1)
#set the CRS to the common lat/long system, also called WGS84
gdf.crs = 'EPSG:4326'
gdf.plot(markersize=1)

#setting the wrong CRS can cause major problems
gdf = gdf.to_crs('EPSG:27700')
gdf.plot(markersize=1)
#you can always set it back
gdf = gdf.to_crs('EPSG:4326')
gdf.plot(markersize=1)

#-plotting from shape files
#shape files are a common format for geospatial data that can be used in various GIS software
#natural earth provides a number of interesting shape files
#download the countries file here: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/
#unzip the file and point to the folder
world = gpd.read_file("ne_110m_admin_0_countries.zip")
world.head(2)
world.crs
world.plot()
#we can also plot just the outline
world.boundary.plot(color = 'pink', linewidth = .5)
#now we can add the starbucks locations
fig, ax = plt.subplots(figsize = (12,12))
world.boundary.plot(ax = ax, color = 'white', linewidth = .5)
gdf.plot(ax = ax, markersize = 1, color = 'yellow')
ax.set_facecolor('black')
plt.show()

#you can modify aesthetics like you normally do with matplotlib to make cool intel-guy maps


#!Exercise - plot only the starbucks locations in NYstate on a map with counties
#you can find the data here: https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html

usa = gpd.read_file('cb_2018_us_country_500k')
usa.crs
usa = usa.to_crs('EPSG:4326')
usa.plot()

usa.head(2)

ny = usa[usa["STATEFP"] == "36"]
ny.plot()

ny_sbucks = gdf[gdf["State/Province"] == "NY"]

fig, ax = plt.subplots(figsize = (12,12))
ny.plot(ax = ax, color = '#525252', linewidth = 1)
ax.set_facecolor('Black')
ny_sbucks.plot(ax= ax, markersize = 1,color = 'yellow')
plt.show()

#-choropleth maps
#choropleths color boundaries based on some value
#the census data already has a variable for land area in a county - lets make counties with more land darker blue
fig, ax = plt.subplots(figsize = (12,12))
ny.plot(column = "ALAND", legend = True, cmap='Blues', ax=ax)
plt.show()

#-chorolpleths with spatial joins
#one of the most useful features of geopandas is the ability to do spatial joins
#let's use the county boundaries to make a choropleth map of the number of starbucks in each county

#first, make sure the projections line up
ny_sbucks.crs
ny.crs

#do a spatial join, counting how many points fall in each polygon
joined = gpd.sjoin(ny_sbucks, ny, how = 'inner', predicate = 'within')
joined.head(2)

county_count = joined.groupby('NAME').size().reset_index(name = 'count')
county_count.head(2)

ny_count = ny.merge(county_count, left_on = 'NAME', right_on= 'NAME')

fig, ax = plt.subplots(figsize = (12,12))
ny.boundary.plot(ax=ax, color = "black", linewidth = 1)
ny_count.plot(ax = ax, coloumn = 'count', legend = True, cmap = 'Greens')
plt.show()
#make a dataframe of just the counts

#merge count data back into the ny county data

#plot both the polygons and the counts

#put the counts in a log scale to deal with heavy skew



#!Exercise - read in the NY Colleges data and plot them as points on the choropleth map you created above



#!Exercise - make a dataframe with a row for each county and columns for the number of starbucks and colleges in each county
#sort by number of colleges (descending order).  Make a plot exploring the correlation.





