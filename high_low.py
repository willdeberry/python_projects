#!/usr/bin/python

from random import randint

def intro():
	''' Intro message explaining the game '''
	print('\nI have picked a number from 1-100, try and guess it.\nAfter each guess, I will let you know if you need to guess higher or lower.\n')

def pick_number():
	''' Pick a number between 1 and 100 '''
	return randint(0,101)

def player_guess():
	'''
	Prompt the player to choose a number and then make sure they actually
	picked a number
	'''
	while True:
		try:
			return int(raw_input('Pick a number between 0-99: '))
		except ValueError:
			print('Incorrect guess, please pick a number between 0-99')
			continue

def high_low(number,guess):
	''' Is the number higher or lower than the number I have picked '''
	result = number - guess
	if result > 0:
		print('Guess Higher...')
	else:
		print('Guess Lower...')

	return result

def main():
	''' Play the game and give feeback to the player '''
	answer = raw_input('Would you like to play a game?[Y/n] ').lower() or 'y'
	intro()
	while answer in ('y','yes'):
		guesses = 0
		number = pick_number()
		high_or_low = high_low(number,player_guess())
		guesses += 1
		while high_or_low != 0:
			high_or_low = high_low(number,player_guess())
			guesses += 1
			continue

		print('You guess correctly and it only took {} guess(es)!'.format(guesses))
		answer = raw_input('Would you like to play again?[Y/n] ') or 'y'

if __name__ == "__main__":
	main()
