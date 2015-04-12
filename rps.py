#!/usr/bin/python

from prettytable import PrettyTable
from random import randint

class Game:
	player_score = 0 # Keep track of how many times the player wins
	cpu_score = 0 # Keep track of how many times the cpu wins

	def num_to_letter(self,num):
		''' Convert the number to a selection so we can tell the player what the cpu chose '''
		letter = {'0': 'rock','1': 'paper','2': 'scissors'}
		return letter[str(num)]

	def letter_to_num(self.letter):
		''' Convert the player's selection to a number for easier determination for who wins '''
		numbers = {'r': 0,'p': 1,'s': 2}
		return numbers[letter]

	def cpu_choice(self):
		''' THe CPU needs to pick too '''
		return randint(0,2)

	def is_valid_selection(self,selection):
		''' Verify that the players choice is a valid and return False if it isn't '''
		if selection in ('r','p','s'):
			return True

		return False

		print('Invalid selection. Please select again...')
		return False

	def players_choice(self):
		''' Get the player's choice of paper, rock, scissors '''
		try:
			return raw_input("Please choose (r)ock, (p)aper, (s)cissors: ").lower()[0]
		except IndexError:
			return False

	def who_wins(self,player,cpu):
		''' Determine who wins this round '''
		result = player - cpu
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
		''' The actual gameplay function. Is in control of user output '''
		players_selection = self.players_choice()
		cpu_selection = self.cpu_choice()
		table = PrettyTable()
		if self.is_valid_selection(players_selection):
			result = self.who_wins(self.letter_to_num(players_selection),cpu_selection)
			table.add_column("Score",["CPU Picks","Results"])
			table.add_column("Player ({} - {}) CPU".format(self.player_score,self.cpu_score),["{}".format(self.num_to_letter(cpu_selection)),"{}".format(result)])
			print(table)
			return True

		return False

def main():
	''' Ask the player if they want to play and keep playing till they say otherwise '''
	answer = raw_input('Ready to play a game?[Y/n] ').lower() or 'y'
	start_game = Game()
	while answer in ('y','yes'):
		if not start_game.play():
			continue

		answer = raw_input('How about another round?[Y/n] ') or 'y'

if __name__ == "__main__":
	main()
