#---SE370 Lesson 6 Lecture/Exercise---#
#-By: Ian Kloo
#-December 2024

#---Doing math with Python
#add 4 and 8

4 + 8

#subtract 6 from 12

6 - 12

#multiply 4 by 7

4 * 7

#divide 12 by 4

12 / 4
type(12/4) # check the data type
int(12/4) # convert from float to int
12//4 # does integer division

#raise 5 to the 3rd power

5**3

#find the remainder of 28 and 6

28%6

#!!!Exercise!!!#
#convert 21.5 degrees Fahrenheit to Celsius in one line in Python

(21.5 - 32)*(5/9)


#---Assigning variables
#assign the value of 6 to x

x = 6
type(x)
#assign the value of 12 to y

y = 12

#divide y by x

y/x

#multiply y by x and save the result to z

z = x * y
z

#divide z by a
z/a

#variables can have other types, assign a the value "hello"

a = 'hello'

#note the type difference between a and x
type(x)
type(a)
#what happens if we try to add an int with a str?
x + a
#create a variable b with the value "10", in quotes
b = "10"
#add it to x
x + b

#how can we make this work?
int(b) + x
str(x)
str(x)+b
#!!!Exercise!!!#
#Creat a variable called age with your age as an integer
age = 20
#Create a variable called height with your height in inches as a float
height = 75.
#Create a variable called major with your major as a string
major = "Systems Engineering"

#add your age and height
age + height

#Create a variable called description with your age, height, and major separated by commas
description = str(age) + ', ' + str(height) + ', ' + major
description
#!!!Stretch Exercise!!!#
#the formula for compound interest can be found here: https://www.thecalculatorsite.com/finance/calculators/compound-interest-formula
#implement the formula to find the amount with principal of 20,000, interest rate 0.08, compounded monthly, for 50 years

#---lists
#make a list of numbers from 1 to 10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
type(my_list)
my_list
#get the first element of the list
my_list[0]


#get the last element of the list
my_list[-1]
my_list[len(my_list)-1]
#get the first 5 elements of the list
my_list[:5]
#get the last 4 elements from the list
my_list[-4:]

#methods
my_list.reverse()
my_list
x.as_integer_ratio()

#---dictionaries
my_dict = dict({'name': "Liam", 'department': 'DSE'})
my_dict
#get the persons name
my_dict['name']= 'CDT M'
my_dict['age'] = 20
my_dict.keys()