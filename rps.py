#!/usr/bin/python

from prettytable import PrettyTable
from random import randint

def num_to_letter(num):
	letter = {'0': 'rock','1': 'paper','2': 'scissors'}
	return letter[str(num)]

def letter_to_num(letter):
	numbers = {'r': 0,'p': 1,'s': 2}
	return numbers[letter]

def cpu_choice():
	return randint(0,2)

def is_valid_selection(selection):
	if selection in ('r','p','s'):
		return True

	print('Invalid selection. Please select again...')
	return False

def user_choice():
	return raw_input("Please choose (r)ock, (p)aper, (s)cissors: ").lower()[0]

def who_wins(user,cpu):
	global player_score
	global cpu_score
	result = user - cpu
	if result == -2 or result == 1:
		winner = 'You win!'
		player_score += 1
	elif result == -1 or result == 2:
		winner = 'You lose'
		cpu_score += 1
	else:
		winner = "It's a tie"

	return winner

def main():
	global player_score
	global cpu_score
	answer = raw_input('Ready to play a game?[y/n] ').lower()
	while answer in ('y','yes'):
		user_selection = user_choice()
		cpu_selection = cpu_choice()
		table = PrettyTable()
		if is_valid_selection(user_selection):
			result = who_wins(letter_to_num(user_selection),cpu_selection)
			table.add_column("Score",["CPU Picks","Results"])
			table.add_column("Player ({} - {}) CPU".format(player_score,cpu_score),["{}".format(num_to_letter(cpu_selection)),"{}".format(result)])
			print(table)
		else:
			continue

		answer = raw_input('How about another round?[y/n] ')

if __name__ == "__main__":
	player_score = 0
	cpu_score = 0
	main()
