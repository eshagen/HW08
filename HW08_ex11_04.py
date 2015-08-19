#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_new(d, v):
	# I'm creating a new list to capture all keys that map to v.
	new_list = []
	# Running through all keys in the dictionary, only returning finished list.
	for k in d:
		if d[k] == v:
			new_list.append(k)
	return new_list
	



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
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
    	d[c] = d.get(c, 0) + 1
    return d

def get_pledge_list():

    with open('pledge.txt') as f:
        pledge_list = f.read().split()
    # Eliminate punctuation from the end of words with ternary operation
    pledge_list_noPunct = [word if word[-1] in ascii_letters  # Requires from string import ascii_letters
                           else word[:-1] for word in pledge_list]
    return pledge_list_noPunct



##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print reverse_lookup_new(pledge_histogram, 1)
	print reverse_lookup_new(pledge_histogram, 9)
	print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()