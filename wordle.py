import random
from colorama import Back
import sys

with open('wordle_answers.txt') as f:
    words = f.read().splitlines()

with open('wordle_allowed.txt') as f:
    allowed = f.read().splitlines()

word = random.choice(words) #randomly choosing the word from words.txt
lives = 5
to_print = ""
is_puzzle_solved = False
colours = [Back.RESET] * 5

def error_message():
    print('Error! Please restart the game and contact the developer if the error continues.')

def winning_message():
    print(f"Congratulations! You've won, the word was {word} and you had {lives} livesleft.")

if len(word) != 5:
    error_message() #Check to see if the word is 5 letters
    sys.exit(error_message())
try:
    while is_puzzle_solved == False and lives > 0: #checking to see if the program should be run
        to_print = ""
        guess = input(Back.RESET + 'Guess a 5 letter word:').lower()
        if guess in allowed or guess in words:
            if len(guess) != 5:
                print('Please make sure your word is 5 letters.')
            elif guess == word:
                winning_message()
                break
            else:
                remaining = list(word)
                for i, char in enumerate(guess):
                    if char == word[i]:
                        remaining[i] = None  # consume this letter
                for i, char in enumerate(guess):
                    if char == word[i]:
                        to_print += Back.GREEN + char
                    elif char in remaining:
                        to_print += Back.YELLOW + char
                        remaining[remaining.index(char)] = None  # consume this letter
                    else:
                        to_print += Back.RESET + char

                print(to_print + Back.RESET)
                lives -= 1
                print('Lives left:', lives)
        else:
            print('Make sure your guess is a real word please.')
except KeyboardInterrupt:
    error_message()
    
    
if lives == 0:
    print(f'Game over! You ran out of lives. The word was {word}') #Game over message

if is_puzzle_solved == True:
    print(f'Well done! You completed the hangman with {lives} left. The word was {word}') #Winning message