#---SE370 Lesson 11 Lecture/Exercise---#
#-By: Ian Kloo
#-December 2024


#-sorting dataframes
#load the electric cars data from last class


#sort by price, least to most


#sort by price, most to least


#sort by battery capacity, then price

#-filtering dataframes
#filter to just teslas


#filter using negation


#filter to teslas with range over 350


#!!!Exercise: create a dataframe called 'non_tesla' that contains all non-tesla cars with range prices under 50,000.  Sort it by most to least range.


#-transforming columns using filters
#create a new column called "range_category" that is 'long' if the range is over 250, 'short' otherwise


#!!!Exercise: create a new column called 'capacity' that is 'high' if the batery capacity is over 70 and 'low' otherwise.
#Then, filter to cars with long range and low capcaity


#-dealing with missing data
#it would be nice if our data was always clean...but there's almost always something missing
#read in 'electric_cars_bad.csv'

#finding rows with missing data

#drop these rows for now

#our bigger problems come from things like blank columns, spaces, or columns with strang string values
#looking at column types can help identify likely issues


#sometimes, it can be difficult to find bad values


#as with before, we can either research these errors or drop them if we can't figure out the missing data


#!!!Exercise: read in the deer harvest data in 'deer_harvest.csv'.  Remove any rows with NA/missing values and fix any type issues.
#output a dataframe with only Muzzleloader harvests, sorted by buck count (descending)


#!!!Stretch Exercise: create a function that takes in a file name, searches each column for NA/missing values, drops them, and returns a clean dataframe
#try to be robust to many different potential missing data signifiers.
#also print how many rows were dropped
