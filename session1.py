#!/usr/bin/env python

# You can write comments with a #

# The first line tells us where/what program we are running 
# it is called a shebang

# First program

print('Hello world')

# Key to python is that you can do 

# Watch 0:54 of the following clip: https://www.youtube.com/watch?v=eB5VXJXxnNU

# Lets make a bunch of 9s

first_number = int('9'*300)
second_number = int('9'*300 + '888' + '9'*200)

print('Here is the first number: ' + str(first_number))
print('Here is the second number: ' + str(second_number))

print('Here is the answer to Ali G')
print(first_number*second_number)

print('Booyakasha Check it')

# Why don't we add a bit more flavor to this

from PIL import Image
Image.open('ali-g-comedian.jpg').show()



# What did we do on line 19?
# What is  '9' + '9' 
# What is  9 + 9
# Strings versus ints

# What is PIL and what are we doing on line 32?

# Last exercise

# What is the sum of each number from 1 to 57 divided by 3?

# Make a list of numbers
mylist = list(range(1,58))
import numpy as np
myarray = np.array(mylist)
print(sum(myarray/3))

i = 1
sumval = 0
while i < 58:
    sumval += i/3
    i += 1

print(sumval)





