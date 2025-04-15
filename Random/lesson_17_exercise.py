#---SE370 Lesson 16 Lecture/Exercise---#
#-By: Ian Kloo
#-February 2025

#---Background
#-we've already made static visualizations and learned how to use AI to customize them
#-no we want to see how to make interactive visualizations

#---Objectives
#-make interactive visualizations using altair
#-share interactive visualizations
import os
os.getcwd()
#---libraries
import altair as alt
import pandas as pd

df = pd.read_csv('thor_bombings_clean.csv')
df.head()
df['year_month'] = df['msndate'].str[:7]

#----Plots for discrete data----#
#-barchart of count of bombings with altiar

#make a dataframe of count of bombings per year/month
df_plot = df.groupby('year_month').size().reset_index(name = 'count')
df_plot.head()

alt.Chart(df_plot).mark_bar().encode(
    x = 'year_month',
    y = 'count'
)
#adding axis titles and chart title
alt.Chart(df_plot).mark_bar().encode(
    x = alt.X('year_month', title = 'Year & Month'),
    y = alt.Y('count', title = 'Number of Missions'),
).properties(
    title = '# of Missions Per Month'
)

#make it interactive!
alt.Chart(df_plot).mark_bar().encode(
    x = alt.X('year_month', title = 'Year & Month'),
    y = alt.Y('count', title = 'Number of Missions'),
).properties(
    title = '# of Missions Per Month'
).interactive()
#!this lets you zoom and pan on the chart

#add hover tooltip to show the exact count

#customize tooltip to format text and make it look more professional
alt.Chart(df_plot).mark_bar().encode(
    x = alt.X('year_month', title = 'Year & Month'),
    y = alt.Y('count', title = 'Number of Missions'),
    tooltip = [alt.Tooltip('year_month', title = 'Year & Month'), alt.Tooltip('count', title = '# Missions')]
).properties(
    title = '# of Missions Per Month'
).interactive()

#-histograms
#make a histogram of the count of bombings
alt.Chart(df_plot).mark_bar().encode(
    x = alt.X('count', bin=alt.Bin(maxbins=20)),
    y = 'count()'
).properties(
    title = 'Histogram of Num Missions per Month',
    width = 400,
    height = 150
)

#fix the width
#good

#!!!Exercise: Change the number of bins to 20.
#good

#-boxplots
#make a boxplot of the number bombing runs by milservice
df.head()
df_plot = df.groupby(['year_month','milservice']).size().reset_index(name = 'num_missions')
df_plot.head()

alt.Chart(df_plot).mark_boxplot(size = 40).encode(
    x = 'milservice',
    y = 'num_missions'
).properties(
    height = 150,
    width = 350
)

#!note the use of size to change the width of the boxes


#sorting the groups by median
median_order = df_plot.groupby('milservice')['num_missions'].median().sort_values(ascending=False).index

mean_order = df_plot.groupby('milservice')['num_missions'].mean().sort_values(ascending=False).index


alt.Chart(df_plot).mark_boxplot(size = 40).encode(
    x = alt.X('milservice', sort = median_order),
    y = 'num_missions'
).properties(
    height = 150,
    width = 350
)

alt.Chart(df_plot).mark_boxplot(size = 40).encode(
    x = alt.X('milservice', sort = mean_order),
    y = 'num_missions'
).properties(
    height = 150,
    width = 350
)

#!!!Exercise: categorize prices into 3 groups: low, medium, and high. Make a boxplot of range by price group.
#sort the groups by median range


#-heatmaps
#make a heat map of target type by milservice
df_plot = df.groupby(['tgttype', 'milservice']).size().reset_index(name = 'numtgts')

alt.Chart(df_plot).mark_rect().encode(
    x = 'tgttype',
    y = 'milservice',
    color = 'numtgts'
).properties(
    height = 400,
    width = 1200
)

#-scatter plots
ec_df = pd.read_csv('electric_cars.csv')

#make a scatter plot of range vs price
ec_df = pd.read_csv('electric_cars.csv')
ec_df.head()

alt.Chart(ec_df).mark_point().encode(
    x = 'range',
    y = 'price',
    tooltip = ['range', 'price']
).interactive()

#fit then add correlation line using layering



#!!!Exercise: make a scatterplot of battery_capacity and speed.  Color the dots orange.  Add a blue regression line.
#change the x and y axis titles to be "Range" and "Price" and add a chart title.
#make it so the user can pan/zoom on the chart



#!!!Exercise: make a line chart of the count of bombings over time by milservice.  Add a tooltip to show the exact count.
#customize the tooltip to format the text and make it look more professional.
#add a chart title and axis titles.






