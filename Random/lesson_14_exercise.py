#---SE370 Lesson 14 Lecture/Exercise---#
#---Debugging---#
#-By: Steve Gillespie
#-February 2025

#---Key points to hit
# Execution Errors all have an error message 


#--- Show each error and provide a fix
# IncompleteInputError
print("Hello World")  
# Fix:


# Syntax Error
def my_function():
    print('hello world')
# Fix:


# Indentation Error
def my_function():
    print("This line is not indented correctly")
# Fix


# Name Error
undefined_variable = 1
print(undefined_variable)
# Fix:


# Type Error
result = "5" + 5

result = '5' + str(5)
# Fix


# ValueError
int("seven")
int('7')
# Fix


# IndexError
my_list = [1, 2, 3]
print(my_list[0])
# Fix


# KeyError
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict["c"])
# Fix


# AttributeError
number = [42]   
number.append(10)
print(number)
# Fix


# ModuleNotFoundError
import nonexistent_module 

import pandas
import os
# Fix


# ImportError
from numpy import some_function
from numpy import sin

import numpy as np

sin(3.14159)
# Fix


# ZeroDivisionError
result = 10 / 1
# Fix


# FileNotFoundError
with open("nonexistent_file.txt", "r") as file:
    content = file.read()
# Fix



#--- Exercise 
# Fix the following code. with the following data frame

df = bear.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Print out each column in the data frame
for myKey in ['a','b','c']:
    print(dataframe[C])

# Fix
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

for myKey in ['A','B','C']:
    print(df[C])


#--- Verification Fix
# Assuming that your code runs, you also need to check it to make sure it's actually doing what you want.
# This takes some level of practice and experience, but a good way to do this is to build test cases.
# Test cases are situations you develop that stress the code in different ways.  
# Generally you should attempt to figure out what **can** happen, not what **should** happen.

import random

def roll_dice():
    """Roll two six-sided dice and return their sum."""
    return random.randint(1, 6) + random.randint(1, 6)

def play_craps():
    """Play a single game of Craps."""
    print("Welcome to Craps!")
    
    first_roll = roll_dice()
    print(f"You rolled: {first_roll}")

    # First roll conditions
    if first_roll in {7, 11}:
        print("You win!")
        return
    elif first_roll in {2, 3, 12}:
        print("Craps! You lose.")
        return

    # Set point and continue rolling
    point = first_roll
    print(f"Your point is now {point}. Keep rolling to match it, but avoid a 7!")

    while True:
        roll = roll_dice()
        print(f"You rolled: {roll}")

        if roll == point:
            print("You hit your point! You win!")
            return
        elif roll == 7:
            print("You rolled a 7! You lose.")
            return

# Run the game
play_craps()


#--- Debug this code
# Craps Pass Line Bet
# https://entertainment.howstuffworks.com/craps4.htm 
# Roll Two Dice and Sum the Result
# If you roll a 7 or 11, you double your money.
# If a 4, 5, 6, 8, 9, or 10, this is a "point"
# Roll again until you either roll a 7 or the point.  If point happens before the 7 you double your money.
# If a 2, 3, or 12 (called a craps) is initially rolled, you lose.
# If a 7 is rolled before your point, you lose.

import random

def craps(bet):
    point = 2*random.random()  # Calculate your point by two random rolls

    if point in (7, 11): # If your initial roll is a 7 or 11 you win and return 2x the bet
        payoff = 2*bet 
    
    if point in (2, 3, 12): # If your initial roll is a craps (2, 3, or 12) you lose and get nothing
        payoff = 0
    
    while keep_playing: # while keep playing is true 
        new_roll = 2*random.random() # roll 2 new dice 
        if new_roll == point: # if you roll your point before the shooter rolls a 7 you win
            payoff = 2*bet 
        if new_roll == 7: # if the shooter rolls a 7 first, you lose 
            payoff = 0
            keep_playing = False # stop if you roll a 7 
    
    return payoff # end the function and return the payoff


# Stretch Exercise:
# Does the house win on this?  Run this 1000 times using a dollar bet and find out how much the house takes in vs. how much the house pays out



# Hint: The house always wins!


#--- Try Except
# Often we can't predict every possible input or situation our code will encounter. 
# As this code is usually part of a larger code set, we generally 1) don't want it to all crash and 2) want some useful feedback when we encounter different errors

# Take a function to divide numbers:
def divide_numbers(a, b):
    return a/b 

# Test it on a few inputs
x = divide_numbers(10, 2) # x = 5
x = divide_numbers(10, 0) # x doesn't get defined and we throw an error

# use the try except method


# Test the function


# Add in else and finally


# Why is this useful?
# Often you'll write code that has variable input. You don't want it to break every time it encounters a simple error.
# Consider code that calculates the mean of a list by progressively summing every number, 
# skipping elements that can't be summed, and counting the number of errors 

