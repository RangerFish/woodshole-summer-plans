#---SE370 Lesson 8 Lecture/Exercise---#
#-By: Ian Kloo
#-December 2024

#---Key points to hit
#-write simple logic statements
#-understand the syntax of if/else 
#-understand the purpose of loops
#-recognize the issue of infinite loops
#-write for and while loops
#-use break and if/else statements to debug loops


#---if/else in python
#logical equivalency in Python is done with == or !=

10 == 10
10 != 10

x = 'abc'
y = 'xyz'
x == y

#other operators apply as well

10 < 30
30 <= 10
'abc' > 'xyz'   
#alphabetization, later in the alphabet is greater

[1, 2, 3] < [4, 5, 6]
[1, 2, 3] > [0, 5, 0]
#uses first number in list

1 in [1, 2, 3]
'a' not in "abc"

#you can also use compound logic

True and True
True and False

True or True
True or False
#returns True

not(True or False)

#exclusive or xor

True ^ False
False ^ True
False ^ False
True ^ True

#writing a simple if/else statement
#!if statements evaluate logic and then do whatever is indicated

age = 15
if age < 18:
    print('kid')
else:
    print('adult')

#adding another condition

age = 20

if age < 13:
    print('kid')
elif age < 20:
    print('teen')
else:
    print('adult')

#example of screwing up
age = 40

if age <= 18:
    print('kid')
elif age > 13:
    print('teen')
else:
    print('adult')

#!!!Exercise: write if/else logic that prints "cold" if a variable called
#degrees is less than 40, mild if between 40 and 60, and warm if between 60 and 80,
#hot if above 80.

degrees = 81

if degrees < 40:
    print('cold')
elif degrees >= 40 and degrees <= 60:
    print('mild')
elif degrees >= 60 and degrees <= 80:
    print('warm')
else:
    print('hot')


#--for loops
#!loops are critical for repeated tasks, like operating on every element of a list
#add 10 to every item in a list and print the results
my_list = [1, 2, 3, 4, 5]

for my_element in my_list:
    print(my_list + 10)
    z = my_element**2
    print(z)

#do the same loop, but now with an index
#!with some objects, it makes more sense to use range - but not often with lists

list(range(10))

for i in range(len(my_list)):
    print('i is: ' + str(i))
    print(my_list[i] + 10)

#go back to looping over the list directly and save the results to a new list

my_new_list =[]

for my_element in my_list:
    my_new_list.append(my_element + 10)

my_new_list

#!!!Exercise: write a for loop that looks at each element of the following loop
#and assigns a value to a new list stating if the temperature is cold, mild, warm or hot

temp_list = [100, 43, 10, 6, 68, 90, 24, 34]
temp_cat = []

for my_temp in temp_list:
    if my_temp < 40:
        temp_cat.append('cold')
    elif my_temp >= 40 and my_temp <= 60:
        temp_cat.append('mild')
    elif my_temp >= 60 and my_temp <= 80:
        temp_cat.append('warm')
    else:
        temp_cat.append('hot')

#print the full final list to check your work

temp_cat

#--while loops
#write a simple loop that does the same thing as our simple for loop

my_list = [1, 2, 3, 4, 5]

counter = 0

while counter < len(my_list):
    print('Coutner is: ' + str(counter))
    print(my_list[counter] + 10)
    counter += 1
    

#make a loop that counts to 100 by 10s

start = 0

while start <= 100:
    print(start)
    start = start + 10 

#!!!Exercise: create a while loop that counts the number of random draws needed to 
#draw the number 53.

#this code will create a random number between 1 and 100


import random
rando = random.randint(1,100)
num_counter = 1

while rando != 53:
    num_counter += 1
    rando = random.randint(1,100)

num_counter


#!!!Stretch Exercise: rerun the above loop 1,000 times and calculate the average 
#number of draws needed to get 53.  Do your results suggest the randint() function
#is truely random?



#--debugging loops
#going back to our simple loop, let's see how we can debug problems


#break is a useful tool to stop a loop after one run
my_list = [1, 2, '3', 4]

my_new-list = []

for x in my_list:
    my_new_list.append(x + 10)
    break

x

#now we can let the loop run again 


#!!!Exercise: debug this loop
words = ["apple", "banana", "cherry", "date"]
for i in range(0, 5):
    print(words[i])

