#!/usr/bin/env python
# Exercise: mimsmind0.py  
# Write a program to:
# usage: python mimsmind0.py [length]
# The program generates a random number with the number of digits equal to length.
# If the command line argument length is not provided, the default value is 3.
# The program prompts the user to type in a guess, informing the user of the 
# number of guess allowed and digits in the random number. The program reads the 
# user input, and provides feedback to the user.  A bull means the guess contained
# a numeral in the exact position, and a cow represents an included digit in the
# wrong position.
##############################################################################
import sys
import random

def get_random():
	"""Generates and returns a random number, size dependent on user input.  If no 
	user input entered, default random number will be 3 digits.
	"""
	# Create a variable to respresent the number of digits our random number will be.
	rand_digits = 0

	try:
		# Checks to see if the user specified their preferred number of digits.
		rand_digits = int(sys.argv[1])
	except:
		# Absent user input, defaults to a single digit random number
		rand_digits = 3

	# Establishes the maximum value for the range of random numbers
	random_range = str(9) * rand_digits

	# Generates and returns the random number.
	random_number = random.randint(1, int(random_range))
	return random_number

def max_rounds(num):
	"""Funciton returns the maximum number of rounds to be played, based on a 
	prescribed formula.
	"""

	# Finds the length of the string of the random number
	rand_digits = len(str(num))
	# Applies to formula rounds = (2 ^ length) + length
	rounds = ((2 ** rand_digits) + rand_digits)
	return rounds

def start_game():
	"""Function generates a random number, the number of user guesses allowed
	and prompts the user for their first input before passing the first user
	guess and the random number to the 'play_game' function.
	"""

	random_number = get_random()
	allowed_guesses = max_rounds(random_number)
	random_length = len(str(random_number))	

	print "Let's play the mimsmind1 game.  You have {0} guesses.".format(allowed_guesses)

	# The first user prompt is different from all furhter prompts.
	guess = raw_input("Guess a {0}-digit number: ".format(random_length))
	play_game(guess, random_number)	
	
def play_game(g, rand_num):	
	"""The play_game function deals directly with user input, and sends proper
	user input to the 'evaluate_input' function.  The play_game function ultimately
	ends when either the user exceeds their maximum permitted turns, or when the 
	user correctly guesses the random number.
	"""

	guess_counter = 1
	random_number = rand_num
	guess = g
	random_length = len(str(random_number))
	allowed_guesses = max_rounds(random_number)

	while guess_counter < allowed_guesses:
		# I am storing the individual digits of the random number in a list.
		rand = [int(char) for char in str(random_number)]
		try:
			# Can't figure out how to also insist on a digit requirement.
			user_guess = int(guess)
		except ValueError:
			print "Invalid input.  Try again:",
			guess = raw_input(" ")
			continue
		else:
			# Creating a list of the digits of the user's guess for evaluation purposes.
			user_list = [int(char) for char in str(user_guess)]
			# Accepting the return from the evaluate_input function.
			bulls, cows = evaluate_input(user_list, rand)
			if bulls == random_length:
				print "Conratulations.  You guessed the correct number in {0} tries.".format(guess_counter)
				return
			# Absent the perfect guess, another iteration of the game is tried.
			else:
				guess = raw_input("{0} bull(s), {1} cow(s).  Try again: ".format(bulls, cows))
				guess_counter += 1
				continue

	print "Sorry.  You did not guess the number in {0} tries.  The correct number is {1}.".format(allowed_guesses, random_number)


def evaluate_input(user_list, actual_list):
	"""This function accepts a list of digits guessed by the user and a list of digits
	representing the random number.  The function evaluates the number of 'bulls' and 
	'cows' and returns those integer values.
	"""

	bulls = 0
	cows = 0
	cow_list = []
	for value in user_list:
		# Checks if the value from the user guess is in the random number.
		if value in actual_list:
			# Checks to see if the value is in the same index as it's counterpart.
			if user_list.index(value) == actual_list.index(value):
				x = user_list.index(value)
				bulls += 1
				# When a bull is found, I change that value in both lists to 'x'.
				user_list[x] = 'x'
				actual_list[x] = 'x'
			else:
				if value not in cow_list:
					# I've had issues with excessive cow assignment when entering
					# user guess like '444' or '222' and am using this list to 
					# try to combat this problem.
					cow_list.append(value)
					cows += 1
	return bulls, cows

##############################################################################
def main():  # CALL YOUR FUNCTION BELOW
	start_game()

if __name__ == '__main__':
    main()