import hello2
from math import *

# simple printing of hello world to console
print "Hello World!"

print "hello" + str(15)

# print hello world when function is called
def hellofunc():
	print "From function hello: Hello World!"

# print hello world with arguments
def hello_with_args(word):
	print "Hello " + word

# hello_with_args("Luke!")

# print hello world with arguments
def hello_with_args_default(something, word="World!"):
	print "Hello " + something + " " + word

# hello_with_args_default()
# hello_with_args_default("Luke!")
