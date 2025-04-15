# CDT Wyatt Sirimaturos. Assistance given to the author. 
# Helped debug code and recommended using local variable. 
# West Point, NY, 05FEB2025.


def square_number(num):
        if type(num) != int:
            if type(num) != float:
                return "Wrong data type!"
        square = num ** 2
        return square


def check_number(num):
    if type(num) != int:
        return "This is not an integer"
    elif num % 2 == 0 and num > 0:
        return "positive and even"
    elif num % 2 == 0 and num < 0:
        return "negative and even"
    elif num % 2 != 0 and num > 0:
        return "positive and odd"
    elif num % 2 != 0 and num < 0:
        return "negative and odd"
    else:
        return "Zero not valid"

# ChatGPT. Assistance given to the author, AI. 
# Helped implement count and char to interate through string. 
# Prompt: How to write a function that checks for characters in a string and returns that number? 
# Response: you can use the .count() method or a loop. 
# OpenAI, (https://chatgpt.com). West Point, NY, 04FEB2025.

def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


# ChatGPT. Assistance given to the author, AI. 
# Showed how to use index < len(word). 
# Prompt: how to do this with while loop instead of for? 
# Response:while index < len(word): if word[index] in vowels:
# OpenAI, (https://chatgpt.com). West Point, NY, 04FEB2025.

def count_vowels_while(word):
    vowels = "aeiou"
    count = 0
    index = 0
    while index < len(word):
        if word[index] in vowels:
            count += 1
        index += 1
    return count

# ChatGPT. Assistance given to the author, AI. 
# Debugged by code by using return instead of print. 
# Prompt: why is my code returning this error message
# Response: use return "Key already exists!" instead of print :
# OpenAI, (https://chatgpt.com). West Point, NY, 05FEB2025.

def add_to_dict(my_dict, key, value):
    if key in my_dict:
        return "Key already exists!"
    my_dict[key] = value
    return my_dict


# ChatGPT. Assistance given to the author, AI. 
# Helped fix return with commas in string. 
# Prompt: How to get rid of commas in return value (pasted code)
# Response: use {len(list_1)} in string :
# OpenAI, (https://chatgpt.com). West Point, NY, 05FEB2025.

def make_dict(list_1, list_2):
    if type(list_1) != list or type(list_2) != list:
        return 'Wrong data type!'
    if len(list_1) != len(list_2):
        return f'Length mismatch! length of list 1 is {len(list_1)} while length of list 2 is {len(list_2)}'
    return dict(zip(list_1, list_2))


# ChatGPT. Assistance given to the author, AI. 
# Defined what makes up prime number and put into function. 
# Prompt: Write a function that returns True if a number is prime.
# Response: code notated below
# OpenAI, (https://chatgpt.com). West Point, NY, 04FEB2025.

# CDT Wyatt Sirimaturos. Assistance given to the author. 
# Told me to use return instead of print. 
# West Point, NY, 05FEB2025.

def check_prime(num):
    if num < 2:
        return "Number must be greater than or equal to 2"
    for i in range(2, int(num ** 0.5) + 1):   # wrote this
        if num % i == 0:  # wrote this
            return False
    return True

def check_prime_list(num_list):
    def check_prime(num):
        if num < 2:
            return "Number must be greater than or equal to 2"
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [check_prime(num) for num in num_list] #showed to to interate through list and return values


# ChatGPT. Assistance given to the author, AI. 
# Debug code. 
# Prompt: debug code.
# Response: Function that with reverse the string to see if it matches
# OpenAI, (https://chatgpt.com). West Point, NY, 04FEB2025.

def check_palindrome(word):
    return word == word[::-1]