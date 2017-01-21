#! /usr/bin/python3
import random

def get_word():
	with open('dictionary.txt','r') as f:
		line = f.readline()
		words = []
		for line in f:
			words.append(line.rstrip('\n'))
			word = random.choice(words)
		print (word)
		return word
		
if __name__ == '__main__':
	word = get_word()
	guessed = '_' * len(word)
	word = list(word)
	guessed = list(guessed)
	last_guessed = []
	letter = input('Enter the letter:')
	while True:
		if letter.upper() in last_guessed:
			letter = ''
			print ('Already guessed!!')
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
		else:
			print(''.join(guessed))
			if letter is not '':
				last_guessed.append(letter.upper())
			letter = input('Guess the letter:')
		
		if '_' not in guessed:
			print('You won!!')
			break