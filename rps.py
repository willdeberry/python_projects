#!/usr/bin/python

from prettytable import PrettyTable
from random import randint

def num_to_letter(num):
	letter = {'0': 'rock','1': 'paper','2': 'scissors'}
	return letter[str(num)]

def letter_to_num(letter):
	numbers = {'r': 0,'p': 1,'s': 2}
	return numbers[letter]

class Game:
	player_score = 0
	cpu_score = 0

	def cpu_choice(self):
		return randint(0,2)

	def is_valid_selection(self,selection):
		if selection in ('r','p','s'):
			return True

		return False

		print('Invalid selection. Please select again...')
		return False

	def user_choice(self):
		try:
			return raw_input("Please choose (r)ock, (p)aper, (s)cissors: ").lower()[0]
		except IndexError:
			return False

	def who_wins(self,user,cpu):
		result = user - cpu
		if result == -2 or result == 1:
			winner = 'You win!'
			self.player_score += 1
		elif result == -1 or result == 2:
			winner = 'You lose'
			self.cpu_score += 1
		else:
			winner = "It's a tie"

		return winner

	def play(self):
		user_selection = self.user_choice()
		cpu_selection = self.cpu_choice()
		table = PrettyTable()
		if self.is_valid_selection(user_selection):
			result = self.who_wins(letter_to_num(user_selection),cpu_selection)
			table.add_column("Score",["CPU Picks","Results"])
			table.add_column("Player ({} - {}) CPU".format(self.player_score,self.cpu_score),["{}".format(num_to_letter(cpu_selection)),"{}".format(result)])
			print(table)
			return True

		return False

def main():
	answer = raw_input('Ready to play a game?[Y/n] ').lower() or 'y'
	start_game = Game()
	while answer in ('y','yes'):
		if not start_game.play():
			continue

		answer = raw_input('How about another round?[Y/n] ') or 'y'

if __name__ == "__main__":
	main()
