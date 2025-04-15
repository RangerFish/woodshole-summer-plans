#---SE370 Lesson 12 Lecture/Exercise---#
#-By: Ian Kloo
#-December 2024

import os
os.chdir('C:/Users/william.monahan/OneDrive - West Point/SE370/Lesson_12_Data')

import pandas as pd

#-calculating statistics
#load the dataset called shopping.csv

shopping = pd.read_csv('shopping.csv')
shopping.head()
len(shopping)

#what is the maximum and minimum sales amount?
shopping['sales_amount'].min()
shopping['sales_amount'].max()

#what store had that sales amount?
shopping[shopping['sales_amount'] == 800]
shopping[shopping['sales_amount'] == shopping['sales_amount'].min()]

#!!!Warm up exercise: find the average sales amount
shopping['sales_amount'].mean()

#!!!Exercise: find the row with the closest sales amount to the average
shopping['sales_vs_avg'] = shopping['sales_amount'] - shopping['sales_amount'].mean()
shopping['sales_vs_avg'].min()
shopping[shopping['sales_vs_avg'] == shopping['sales_vs_avg'].min()]

#-grouping and aggregating
#calculate the maximum, minimum, and average sales for each store
shopping.groupby('store_id').max('sales_amount')
shopping.groupby('store_id').min('sales_amount')
shopping.groupby('store_id').mean('sales_amount')

#we can also group by multiple things.  find the max sales by store for each day
shopping.groupby(['store_id','date']).max('sales_amount')

#return indicies to columns
shopping.groupby(['store_id','date']).max('sales_amount').reset_index()

#confirm we have the same number of records for each store in the data
shopping.groupby('store_id').size()

#count the number of categories reported for each store
shopping.groupby('store_id')['product_category'].count()

#!!!Exercise: on which day were the customers the oldest (on average)?
shopping.groupby('date').mean('customer_age')

#!!!Exercise: show the total sales for store 3 only for each day
s3sbyd = shopping[shopping['store_id'] == 3].groupby(['store_id','date']).sum('sales_amount').reset_index()
s3sbyd.drop(['customer_age', 'sales_vs_avg'], axis = 1)

#!!!Exercise: suppose we don't care about department.  Calculate the total sales for each store and each day.  Then find the max total sales for each store.
#hint, you will probably have to do 2 different groupby() operations.
tmp = shopping.groupby(['store_id','date']).sum('sales_amount').reset_index()
tmp.groupby('store_id').max('sales_amount').reset_index()


#---reshaping pandas dataframes
#first, create a dataframe of average sales by store for each day FOR ASSIGNMENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
df = shopping.groupby(['store_id', 'date']).mean('sales_amount').reset_index()
df
df = df.drop(['customer_age','sales_vs_avg'], axis = 1)
df

#now reshape the data so there is a row for each store and a column for each date
wide = df.pivot(index = 'store_id', columns = 'date', values = 'sales_amount').reset_index()
wide = wide.rename_axis(None, axis = 1)
wide

#reconvert the wide data to long
long = wide.melt(id_vars = 'store_id')
long

#-!!!Exercise: Load the sales.csv data.  Convert it to long format.  Use groupby() to find the average sales for each product and region.
#For example, your final data should have a product column (laptop or smartphone), a region column (north, south, east, west), and a column
#with the average sales
sales = pd.read_csv('sales.csv')
sales.head()

sales.melt(id_vars = ['Product', 'Region']).groupby(['Product','Region']).mean('value').reset_index()
#---Joining dataframes

#let's read in some new datasets
employees = pd.read_csv('employees.csv')
salaries = pd.read_csv('salaries.csv')

employees.head()
salaries.head()
#join the salary data to the rest of the employee data
employees.merge(salaries, how = 'left', left_on = 'id', right_on = 'employee_id')
employees.merge(salaries, how = 'right', left_on = 'id', right_on = 'employee_id')
employees.merge(salaries, how = 'inner', left_on = 'id', right_on = 'employee_id')
employees.merge(salaries, how = 'outer', left_on = 'id', right_on = 'employee_id')
#let's do the same thing with a new salaries table


#!!!Exercise: Join the salary and employee data using a left join (with employee as the left table).  
#Drop missing values and only retain the highest salary for each person.
#your final table should have id, name, department, and salary - with no na values and one record per employee.


#!!!Stretch Exercise: using projects.csv and employee_projecs.csv in addition to the (max) salary and employees data,
#create a function that takes the name of a project and outputs a dataframe with the employee names, roles, and salaries and the project name.
#Project name should be the only input to the function.
