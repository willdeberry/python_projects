#!/usr/bin/python

from random import randint

def pick_number():
	return randint(0,100)

def player_guess():
	while True:
		try:
			return int(raw_input('Pick a number between 0-99: '))
		except ValueError:
			print('Incorrect guess, please pick a number between 0-99')
			continue

def high_low(number,guess):
	result = number - guess
	if result > 0:
		print('Guess Higher...')
	else:
		print('Guess Lower...')

	return result

def main():
	answer = raw_input('Would you like to play a game?[Y/n] ').lower() or 'y'
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
