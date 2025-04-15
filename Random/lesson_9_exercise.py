#---SE370 Lesson 9 Lecture/Exercise---#
#-By: Ian Kloo
#-December 2024

#---working with your file system
#os is a python library that is included in the default install, but not loaded unless you specify that you want to use it
import os

os.listdir()

os.getcwd()

os.chdir()

#list the files in the current directory

os.listdir()

#make a directory in the current folder

os.mkdir('temp')

#remove a directory (warning, this can be dangerous!)
os.removedirs('temp')
#list everything in your downloads folder
os.listdir('c:/Users/william.monahan\\Downloads')
#absolute references start with the drive (e.g., C:/...) but you can also use relative references
os.getcwd()
os.listdir('./Lesson_9_Alt')
os.listdir('../')
#---XLSX (excel files) vs CSV demo
#download the csv file called sample.csv and save it do your downloads folder
#download the csv file called sample.xlsx and save it do your downloads folder

#---reading CSV

with open('./Lesson_9_Alt/sample.csv', 'r') as file:
    lines = file.readlines()

lines[0]
lines[0].split(',')
lines[0].strip()
lines[0].strip().split(',')

with open('./Lesson_9_Alt/sample.csv', 'r') as file:
with open('./Lesson_9_Alt/data/sample.csv', 'r') as file:
    lines = file.readlines()

    data = []
    for line in lines:
        data.append(line.strip().split(','))

data[1][1]
#!!!Exercise: modify the file reading script to ignore the first line (with the header)



#!!!Stretch Exercise: modify the file reading script to create a list of dictionaries, one per line of the CSV, with keys for Name, Age, and City


#to test, this should give the value "San Fransisco"
data[1]['City']


os.getcwd()

with open('./Lesson_9_Alt/sample.csv', 'r') as file:
    lines = file.readlines()

    data = []
    for line in lines:
        data.append(line.strip().split(','))

data[1][1]
lines[0]

#counter = 1
#while counter < len(lines):
#    line = lines[counter]
#    data.append(line.strip().split(','))
#    counter =+ 1


#python also has a csv module to help parse these files without all the splitting and text manipulation
import csv

with open('./Lesson_9_Alt/data/sample.csv', 'r') as file:
    reader = csv.reader(file)

    data = []
    for row in reader:
        data.append(row)

data

#---JSON files
#download sample.json from Canvas into your downloads folder
import json

with open('./Lesson_9_Alt/data/sample.json', 'r') as file:
    data = json.load(file)
data

#JSON is a better choice if you have nested data
#for example, suppose you wanted to store all the cities each person lived instead of just one?
#let's say we want to store that Bob also lived in Manchester

#in CSV, we'd have to do something like



#in JSON, we could have

for d in data:
    if d['Name'] == 'Bob':
        print(d['City'])


#!!!Exercise: write a function that reads in exercise.csv and converts all numbers to integers.  the only argument should be the file name

import csv

def bird_data_function(my_file):
    with open(my_file, 'r') as file:
        reader = csv.read(file)
        next(reader, None)

        bird_data = []
        for row in reader:
            print(row)
            row[0] = int(row[0])
            row[4] = int(row[4])
            bird_data.append(row)

    return bird_data

bd = bird_data_function('./Lesson_9_Alt/sample.csv')

#!!!Exercise: find the maximum wingspan in the data and prints both the wingspan and the bird name in a single line that looks like: "Bird = , Wingspan = "

max_wing = 0
bird = ''

for my_bird in bd:
    if my_bird[4] > max_wing:
        max_wing = my_bird[4]
        bird = my_bird[1]

max_wing
bird
print('Bird = ' + str(bird) + ", Wingspan = "+ str(max_wing))



