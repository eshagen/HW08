
#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

def print_hist_old(h):
    for c in h:
        print c, h[c]


def print_hist_new(h):
    # Created a list of the sorted keys in 'h.'
    sorted_ = sorted(h.keys())
    for c in sorted_:
    	# For each key, I 'reunite' the key with value for printing
    	print c, h[c]

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
	final_list = []
	with open('pledge.txt') as f:
		pledge_list = f.read().split()
    # Eliminate punctuation from the end of words with ternary operation
	pledge_list_noPunct = [word if word[-1] in ascii_letters  # Requires from string import ascii_letters
                           else word[:-1] for word in pledge_list]
	for word in pledge_list_noPunct:
		final_list.append(word.lower())
	return final_list

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()