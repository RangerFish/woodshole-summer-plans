#---SE370 Lesson 25 Lecture/Exercise---#
#-By: Ian Kloo
#-March 2025

import pandas as pd
import bs4 as bs
import requests
from io import StringIO  
import re
from tqdm import tqdm
import time

#things to do:
#1. How to avoid sending too many request
#2. Scrape a website with a table (e.g., wikipedia) 
#3. Scrape non-tabular data --> parsing the results
#4. Web crawling example (demo)

#---responsible webscraping
#making too many requests is a good way to get your IP banned
#and if you do that from a government device...good luck

#how do you avoid sending too many requests?

#1. Read the robots.txt file for the website (for today: https://en.wikipedia.org/robots.txt, https://www.understandingwar.org/robots.txt) 
#   Key things to look for are whether certain parts of the site are blocked and if they have a delay request
#   Wikipedia has no real limits for most pages and no delay request
#   ISW allows for permissive scraping as well, but asks for a 10 second delay between requests
#2. Use a delay even if one isn't requested.  Making more than 1 request per second is usually a bad idea.
#3. In general, try not to deviate too much from "normal" traffic that a site would visit.  Websites are designed to give you
#   access to data and using an automated process to get it is totally fine.  But hosting a website isn't free and servers are
#   sized based on expected traffic.  Try not to create a burden.
#4. Use an exponential delay on requests that get a 429 error (too many requests).  This is a sign you're going too fast.
#   We will not cover this implementation, but you can see it here: https://tenacity.readthedocs.io/en/latest/


#---scraping a website with a table
#first, we need to visit the page and get the HTML content
page = requests.get('https://en.wikipedia.org/wiki/List_of_current_United_States_senators')
page.content
#now we use BeautifulSoup to parse the HTML into a more searchable format
soup = bs.BeautifulSoup(page.content, 'html.parser')
soup
#now we can use the find and find_all methods to search for specific tags
#here, we are pulling all tables from the page.  the results are a list of tables (still in HTML)
tables = soup.find_all('table')
#the first table is clearly not what we want
#key through the tables to see which one has the full senate list
print(tables[5])
#we can use the read_html method to read the HTML table into a pandas dataframe
#the function was made to work with files, so we need to convert the HTML into a string and then
#into a "file-like object" using StringIO.  You can get away with not doing this, but it will throw a warning
df = pd.read_html(StringIO(str(tables[5])))[0]
df
#the table requires some cleaning to get rid of extra/blank fields


#---scraping non-tabular data
#the institute for the study of war publishes a daily brief on Ukraine/Russia
#suppose we're building a daily report and want to pull the key takeaways from this page

#first access the page and parse the HTML content
page = requests.get('https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-march-25-2025')
soup = bs.BeautifulSoup(page.content, 'html.parser')
#now we sub-select into the division with the class "field-name-body" as this is the main content section
main_page = soup.find('div', class_ = 'field-name-body')
#now we further sub-select to only pull the unorder list (ul), this has the key takeaways
takeaway_section = main_page.find('ul')
#we can now pull each list item (li)
list_elements = takeaway_section.find_all('li')
#and finally get the text from each list item
list_elements[0].text

key_takeaways = []
for le in list_elements:
    key_takeaways.append(le.text)

key_takeaways
#first, make the scraper into a function

#next build the urls

#now loop over them, get the takeaways, and store them


#---web crawling (demo code provided)
#check out the wiki page for the russian ground forces
#note the table in "Structure" that shows the field armies.
#we can see the formation leadership, but not the field army leadership
#let's try to crawl the links to the field armies and pull the leadership

#process: get main page -> extract part of page we want -> extract links we want -> visit each link and pull data

#first, get the main page 
page = requests.get('https://en.wikipedia.org/wiki/Russian_Ground_Forces')
soup = bs.BeautifulSoup(page.content, 'html.parser')

#now let's get the table
tables = soup.find_all('table')

#this looks good, but doesn't have the links we want - it just pulls the names
#!go to the page and show them how the <a> tags have the text and an href attribute (with the link)
df = pd.read_html(StringIO(str(tables[4])))[0]
df

#let's clean up the field army names to remove the extra numbers
field_army_clean = []
for fa in df['Field army']:
    tmp = re.sub('\[\d+\]', '', fa) #removes all numbers within brackets
    field_army_clean.append(tmp)

df['Field army'] = field_army_clean

#this will pull all the links - but it is everythign and not just the ones we want!
all_links = tables[4].find_all('a')

#we can loop through the links and only pull the href for the ones with text that matches a field army
field_army_names = df['Field army'].tolist()
field_army_links = []
for link in all_links:
    if link.text in field_army_names:
        field_army_links.append(link['href'])

#note that the links do not contain the base URL (https://en.wikipedia.org) so we need to add that
base_url = 'https://en.wikipedia.org'

#let's just work with one of the field armies and see if we can pull the current commander
page = requests.get(base_url + field_army_links[1])
soup = bs.BeautifulSoup(page.content, 'html.parser')

#!go to the page and show that the current commander is in a table row (tr) that has a 
#!table head (th) with the text "Currentcommander".  The name is in the td tag in that same row.
table_rows = soup.find_all('tr')
for tr in table_rows:
    if tr.find('th') is not None:
        if tr.find('th').text == 'Currentcommander':
            commander = tr.find('td').text

#note, the first field army doesn't work - they don't list the commander in an easy-to-find way
#we'll just have to skip this one or do it manually...webscraping is rarely perfect

#now we can turn our scraper into a function
def get_commander(url):
    page = requests.get(url)
    soup = bs.BeautifulSoup(page.content, 'html.parser')
    table_rows = soup.find_all('tr')
    commander = 'not-found'
    for tr in table_rows:
        if tr.find('th') is not None:
            if tr.find('th').text == 'Currentcommander':
                commander = tr.find('td').text
                
    return(commander)

#and run it over all the field armies
field_army_commanders = []
for link in tqdm(field_army_links):
    field_army_commanders.append(get_commander(base_url + link))

field_army_data = pd.DataFrame({'Field army':field_army_names, 'commander':field_army_commanders})
field_army_data

#bring in commander to original data
df = df.merge(field_army_data, on = 'Field army', how = 'left')
df




