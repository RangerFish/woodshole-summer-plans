#---SE370 Lesson 14/15 Lecture/Exercise---#
#-By: Ian Kloo
#-February 2025

#---Background
#-Make visualizations using matplotlib and seaborn
#-I honestly don't love these plotting libraries, but they are the best Python has for making publication quality plots
#-Consider making the point that R/ggplot is often used by people who use Python for the rest of their analysis

#-we will be using matplotlib for basic plotting and seaborn for more advanced plotting
#-matplotlib lets you control more things, but the flip side of that is it takes a lot of work to get things to look good
#-seaborn is a better option for more advanced plots and the code is typically much more succinct and easier to read

#-key learning point: use LLMs to improve your plots
#-you need to know enough syntax to make basic plots and get going, but there's no point memorizing deep options from the documentation
import os

#---libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('thor_bombings_clean.csv')

#----Plots for discrete data----#
#-bar plots
#!you probably want to do this as a build instead of rewriting the whole thing.  including all steps for instructor reference.
#!the syntax is weird and there is no way we expect anyone to memorize it.  we just want them to get used to the types of things
#!they can do with these libraries - and, importantly, how to look up the syntax they need

#make dataframe of count of bombings per year/month
df['msndate'].str[:7]

df['year_month'] = df['msndate'].str[:7]

df_plot = df.groupby('year_month').size().reset_index(name = 'count')

df_plot

fig, ax = plt.subplots(dpi = 300)
ax.barh(df_plot['year_month'], df_plot['count'],color = "red")
ax.set_xticks(df_plot['year_month'][::3])
ax.set_xticklabels(df_plot['year_month'][::3], rotation = 60, ha = 'right')
ax.set_xlabel('Year and Month')
ax.set_ylabel('Number of Bombings')
ax.set_title('Crushing it in Vietnam')
#plt.savefig('g1_barplot.png')
plt.show()

#use barh to rotate the entire thing

#only make ticks every 3 months, rotate labels and adjust left

#give it a title and axis titles

#change color of bars

#increase the dpi for publication-quality plotting and save

#!!!Exercise: find a way to flip the axes on this plot.  Hint: use an LLM to help.

#-histograms
#!showing this after barcharts so we can take a second to discuss the differences in chart types.  
#!they both have bars so people often confuse them, but they're for completely different things

#make histogram boming runs by month - what does this tell you?
df_plot['count']

fig, ax = plt.subplots()
ax.hist(df_plot['count'])
plt.show()

#!this shows the distribution of the number of monthly bombing runs.  emphasize y axis is count of months with that many runs.
#!demonstrate sensitivity to bin size
fig, ax = plt.subplots()
ax.hist(df_plot['count'], bins = 20)
plt.show()

#!!!Exercise: Create a histogram of electric car prices
#Customize the plot by adding a title, x and y axis labelssing , and adjusting the bin size to 15.
#Change the bar color to blue, and save the plot as a PNG with 300dpi.
fig, ax = plt.subplots(dpi = 300)
ax.hist(df_plot['count'], bins = 15)
plt.show()

#-small multiples
#make a separate histogram for each service in a single plot

df_plot = df.groupby(['year_month', "milservice"]).size().reset_index(name = 'count')

fig, ax = plt.subplots(1, 2, figsize = (10,5))
ax[0].hist(df_plot[df_plot['milservice']=='USAF']['count'])

#---seaborn
#!making boxplots with matplotlib is a mess and requires loops and confusing syntax.  seaborn is much easier

#-boxplots
#make a boxplot of the number bombing runs by milservice
df_plot = df.groupby(['year_month', 'milservice']).size().reset_index(name = 'count')

#boxplot of count by milservice much easier to do in seaborn
fig, ax = plt.subplots()
sns.boxplot(x = 'milservice', y = 'count', data = df_plot, ax = ax)
plt.show()

#sorting the groups by median
order = df_plot.groupby('milservice')['count'].median().sort_values()

#-heatmaps
#make a heat map of aircraft application by milservice
df.head()

df.groupby(["AIRCRAFT_APPLICATION", 'milservice']).size().reset_index(name = 'count')

df_plot.pivot(index = 'AIRCRAFT_APPLICATION', columns = 'milservice', values = 'count')

fig, ax = plt.subplots()
sns.heatmap(df-plot, cmap = 'Blues', ax = ax)
plt.show()

#!!!Exercise: make a grouped barchart of bombing runs by year, with milservice as color using seaborn
#give it a good title, x axis title, y axis title, format the y axis using commas for thousands, change the color palette and save it as a png with 600dpi
#!!!use GPT for the settings



#----Plots for continuous data----#


#-scatter plots
#make a scatter plot of range vs price
ec_df = pd.read_csv('electric_cars.csv')

fig, ax = plt.subplots()
sns.scatterplot(x = 'range', y = 'price', data = ec_df, ax = ax)
plt.show()

#or for matplot

fig, ax = plt.subplots()
ax.scatter(ec_df['range'], ec_df['price'])

#make axes start at zero
ax.set_xlim(0)
ax.set_ylim(0)

plt.show()

#fit then add correlation line
#!note how you can add a confidence interval
import seaborn as sns

fig, ax = plt.subplots()
sns.regplot(x = 'range', y = 'price', ci = 95, line_kws={'color': 'red'}, data = ec_df, ax = ax)
ax.set_xlim(0)
ax.set_ylim(0)
ax.set_xlabel('Range (mi)')
ax.set_ylabel('Price ($)')
plt.show()

#you can use the same plt. syntax to change the aesthetics of a seaborn plot as if it were a standard matplotlib plot


#-pair plots
#make a pair plot of all the continuous variables
#!this is useful for exploratory purposes, but make sure you explain how to read it

sns.pairplot(ec_df)

#-joint plots
#make a joint plot of range vs price


#!!!Exercise: make a lineplot of bombing runs over time by milservice
#each service should get their own line color and style
#add a title, x axis title, y axis title, and legend
#format the x axis to show every 6th month
#save as a png with 600 dpi


#multiple lineplot of count by milservice without a loop with dots
