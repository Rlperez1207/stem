#!/usr/bin/env python3

# Create an object called number that stores the value 7
number = 7

# Create an object called my_list that stores the list of numbers from 1 to 10 inclusive.
my_list = list(range(1,11))

# Use list slicing on my_list to store the list [1, 2, 3] under the name easy_as

easy_as = my_list[:3]
# Define a function called reverse that accepts a string as input and returns that string in reverse.
def reverse(word):
    return word[::-1]


# Define a function called is_palindrome that accepts a string as input and returns True if that string reads the same backwards and forwards, and False otherwise.
# Example: is_palindrome("racecar") should return True. is_palindrome("minivan") should return False.
# You may assume that all characters will be lowercase.

def is_palindrome(word):
    return word == word[::-1]
