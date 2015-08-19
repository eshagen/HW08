#!/usr/bin/env python
# Exercise 1  

##############################################################################

def store_to_dict():
"""Function doesn't accept any arguments, simply takes the lines of words.txt
and returns a dictionary containing all 'words' in the file.
"""	

	d = dict()
	with open ("words.txt", 'r') as f:
		data = f.readlines()
		for line in data:
			if line not in d:
				d[line.strip()] = 1
		return d




##############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print "Yup."
    if "qwertyuiop" in words_dict:
        print "Hmm."

if __name__ == '__main__':
    main()