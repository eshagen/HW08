#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################
from string import ascii_letters
import re

def histogram_old(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def histogram_new(s):
    d = dict()
    for c in s:
    	# Checks how many times c has occurred, adds one to the result
        d[c] = d.get(c, 0) + 1
    return d

def get_pledge_list():
    # I toiled with this for a while before copy/pasting code you suggested others use
    with open('pledge.txt') as f:
        pledge_list = f.read().split()
    # Eliminate punctuation from the end of words with ternary operation
    pledge_list_noPunct = [word if word[-1] in ascii_letters  # Requires from string import ascii_letters
                           else word[:-1] for word in pledge_list]
    return pledge_list_noPunct

##############################################################################
def main():  # DO NOT CHANGE BELOW
    print histogram_new(get_pledge_list())
    #print histogram_new('aaabldke')
    #print histogram_old('aaabldke')
    #print get_pledge_list()
if __name__ == '__main__':
    main()