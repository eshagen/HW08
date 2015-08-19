#!/usr/bin/env python
# Exercise 5
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Update print_hist_new from HW08_ex_11_03.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
##############################################################################

def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    # I used a real informative stackoverflow (Use cases for 'setdefault' dict method).
    # I'm still trying to make myself full comfortable with the process.
    inverse = dict()
    for (key) in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


def print_hist_newest(d):
    # Since we're printing keys w/o values, need to print all 'potential' keys between 1
    # and the greatest key.  
    for key in range(1, (max(d.keys())+1)):
        if key in d:
            print "{0}: {1}".format(key, d[key])
        else:
            print "{0}: {1}".format(key, [])

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
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()