# SIPB IAP 2013 Introduction to Programming
# Instructors: Nathan Arce, Luke O'Malley

# This file contains practice problems to solidify your understanding of the 
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
    # 'safety' is here only for course staff to prevent an infinite loop in the
    # below code
    safety = 0
    
    i = a
    while i <= b:
        if i == a and safety == 0:
            print "Printing {}-{}:".format(a,b)
        elif safety > b:
            sys.exit("WOAH THERE! RUNAWAY WHILE LOOP")
        
        
        # to prevent run away code
        safety += 1
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
    return a/b

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

# Bonus question: Is there a better way to do this than
# with recursion?

def reverse(s):
    if (s == ""):
        return ""
    return reverse(s[1:-1]) + s[0]

# Excercise 4: We're going shopping with lists!
# Here we're using a list that contains items with the format (cost, item_name)
def check_money(items, cash):
    # comment out the following line
    pass
    
    # if an item in the list has multiple components within a tuple you can
    # access those elements like: for item1, item2 in list
    
    # complete the following line, using cost and item_name as your argument names
    for change_me in items:
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
    
    # return the pair as a tuple
    return (max_value, index)
    
# Excercise 6: What time is it? Working with imports.
# Our time function doesn't work, can you tell us what time it is?
def tell_time():
    return time.strftime('%X %x %Z')

# Excercise 7: Dictionaries, and we don't mean those big old books no one knows how to use...
# Write a function called translate that takes a word and a foreign language dictionary
# and checks if we can translate the word, returning the translation if we can, 
# otherwise return "CANNOT TRANSLATE".
def translate(word, dictionary):
    pass

# Excercise 8: First name and last name...
# Given two lists, one of first names, one of last names, produce a new list
# with the first and last names properly combined. Bonus points if you can use
# list comprehension and Python's zip() method. 
def first_and_last(first_names, last_names):
    pass

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
        # Make sure the user does not already exist
        # if it does exist, add a new account to the dictionary
        # Returns True if a new account is made, False otherwise
        pass

    def change_pword(self, username, oldp, newp):
        # Two things must be true: the username must
        # already exist, and the old password must be right
        # If both are true, change the entry in self.user_dict
        # Returns True if the password is changed, False otherwise
        pass

    def access_acct(self, username, pword):
        # Again, the username must exist and the password
        # must be correct, but nothing is modified
        # Returns True if the account is accessed, False otherwise
        pass

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
db = database()
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

#incorrect
#[x ** 2 if x > 11 for x in range(20)]

#correct
#[x ** 2 for x in range(20) if x > 11]

#multiplication tables
#[i * j for i in range(13) for j in range(13)]