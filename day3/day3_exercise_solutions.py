# SIPB IAP 2013 Introduction to Programming
# Instructors: Nathan Arce, Luke O'Malley

# This file contains solutions to practice problems over the 
# topics we've covered during the last two lectures.

import sys
# This is a helper function for the course staff, it allows us to very simply
# check that your code is outputing what it should
def assertEquals(a,b, msg=None):
    if a == b:
        print msg
    else:
        sys.exit("TEST FAILED: {} is not equal to {}".format(a,b))

# Excercise 1: What is indentation good for?
# Print the numbers 0-9 to the console
def print_a_to_b(a,b):
    
    i = a
    while i <= b:
        if i == a:
            print "Printing {}-{}:".format(a,b)
        
        
        # to prevent run away code
        print i
        i += 1


# Excercise 2: Those numbers don't look right...
# Correctly calculate a/b

# You can convert a number to a float by calling float(arg)
# or to an int by calling int(arg). Operations are executed
# in the order you learned in elementary school, and any
# single math operation that involves a float will return
# a float
def divide(a,b):
    return float(a)/b

# Nathan sometimes would just do
# 1.0 * a / b, because a becomes a float by multiplying it
# with a float. As you can see, it's fewer characters, but
# some consider it worse practice


# Exercise 3: That string is missing something...
# Reverse the input string with recursion

# Note: You can access string members the same way as
# list members: string[0] gets the first character
# in the string, string[-1] gets the last, etc.
# However, unlike lists, you CANNOT change a character
# with the line string[number] = letter. This is just
# a built in property of strings; if you want to change
# a string, you have to make a new one, for example, by
# adding two strings together.

def reverse(s):
    if (s == ""):
        return ""
    return reverse(s[1:]) + s[0]


# Excercise 4: We're going shopping with lists!
# Here we're using a list that contains items with the format (cost, item_name)
def check_money(items, cash):
    # if an item in the list has multiple components within a tuple you can
    # access those elements like: for item1, item2 in list
    
    # complete the following line, using cost and item_name as your argument names
    for cost, item_name in items:
        cash -= cost
        if cash < 0:
            return "Can't afford to buy everything"
        else:
            print "Buying {}".format(item_name)
        
    return cash


# Excercise 5: Find the maximum value...
# Iterate over the list and find its maximum value, return the value and
# the index of that value
def find_max(numbers):
    max_value = 0
    index = None
    # How do you check if a value is greater than the previously stored max_value?
    # How do you keep track of the index?
    # Is it better to iterate over the items of the list or instead use indices
    # to access list elements?
    check_index = 0
    while check_index < len(numbers):
        if index == None or numbers[check_index] > max_value:
            max_value = numbers[check_index]
            index = check_index
        check_index += 1
    
    # return the pair as a tuple
    return (max_value, index)


# Excercise 6: What time is it?
# Our time function doesn't work, can you tell us what time it is?
import time

def tell_time():
    return time.strftime('%X %x %Z')


# Excercise 7: Dictionaries, and we don't mean those big old books no one knows how to use...
# Write a function called translate that takes a word and a foreign language dictionary
# and checks if we can translate the word, returning the translation if we can, 
# otherwise return "CANNOT TRANSLATE".
def translate(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    return "CANNOT TRANSLATE"

# Excercise 8: First name and last name...
# Given two lists, one of first names, one of last names, produce a new list
# with the first and last names properly combined
def first_and_last(first_names, last_names):
    names = []

    for i in range(len(first_names)):
        names.append(first_names[i] + ' ' + last_names[i])
        # names.append("{} {}".format(first_names[i], last_names[i])

    return names

# List comprhension solution
# def first_and_last(first_names, last_names):
#     return ["{} {}".format(first, last) for first, last in zip(first_names, last_names)]

# Exercise N: Building a user database.
# We're going to fill in the methods of a class that stores, in a dictionary,
# (username, password) pairs. Because this is just an example, we won't ask
# you to encrypt the passwords, but if you do so, your code should still pass
# the tests.

class Database:
    def __init__(self):
        #initialize the dictionary that will store all (user, password) pairs
        self.user_dict = {} 
    def add_user(self, username, pword):
        if (username in self.user_dict):
            return False
        self.user_dict[username] = pword
        return True
    def change_pword(self, username, oldp, newp):
        if (username not in self.user_dict):
            return False
        elif self.user_dict[username] != oldp:
            return False
        self.user_dict[username] = newp
        return True
    def access_acct(self, username, pword):
        if (username not in self.user_dict):
            return False
        elif self.user_dict[username] != pword:
            return False
        return True




# RUN FUNCTIONS
# 1
print_a_to_b(0,5)
# 2
assertEquals(divide(5,2), 2.5, "PASSED: Excercise 2")
# 3
assertEquals(reverse("Hello?"), "?olleH", "PASSED: Excercise 3")
# 4
shopping_list = [(2, "Seasoning"),
                 (10, "Meat"),
                 (4, "Eggs")]
assertEquals(check_money(shopping_list, 20.0), 4, "PASSED: Excercise 4")
# 5
assertEquals(find_max([1,2,3,10,6,4]), (10, 3), "PASSED: Excercise 5")
# 6
print "Time is {}".format(tell_time())
print "PASSED: Excercise 6"
# 7
spanish =  {'hello': 'hola',
            'yes': 'si',
            'one': 'uno',
            'two': 'dos',
            'three': 'tres',
            'red': 'rojo',
            'black': 'negro',
            'green': 'verde',
            'blue': 'azul'}
assertEquals(translate('hello', spanish), 'hola', "Translated hello")
assertEquals(translate('red', spanish), 'rojo', "Translated red")
assertEquals(translate('teacher', spanish), 'CANNOT TRANSLATE', "PASSED: Excercise 7")
# 8
first = ["Ben", "Lisa"]
last = ["Bitdiddle", "P. Hacker"]
assertEquals(first_and_last(first, last), ['Ben Bitdiddle', 'Lisa P. Hacker'], "PASSED: Excercise 8")

# N
db = Database()
assertEquals(db.add_user('fluffy', 'password123'), True, "Successfully added a user")
#returns True
assertEquals(db.add_user('fluffy', 'newpword'), False, "Successfully conflicted users")
#returns False
assertEquals(db.change_pword('hello?', 'password123', 'newpword'), False, "Successfully failed to change password")
#returns False
assertEquals(db.change_pword('fluffy', 'something', 'newpword'), False, "Successfully failed to change password")
#returns False
assertEquals(db.change_pword('fluffy', 'password123', 'newpword'), True, "Successfully changed password")
#returns True
assertEquals(db.access_acct('fluffy', 'password123'), False, "Successfully failed a login")
#returns False
assertEquals(db.access_acct('who?', 'newpword'), False, "Successfully failed a login")
#returns False
assertEquals(db.access_acct('fluffy', 'newpword'), True, "Successfully logged in.\nPASSED: Exercise N")
#returns True
