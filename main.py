import hm_ascii_art as hm_module
import random

def get_random_word(word_list):
  """ This function returns a random string from the passed list of strings."""
  word_index = random.randint(0, len(word_list) - 1)
  return word_list[word_index]

def display_board(missedLetters, correctLetters, secretWord):
  print(hm_module.HANGMAN_PICS[len(missedLetters)])
  print()

  print('Missed letters:', end=' ')
  for letter in missedLetters:
    print(letter, end=' ')
  print()

  blanks = '_' * len(secretWord)

  for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
    if secretWord[i] in correctLetters:
      blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
  
  for letter in blanks: # Show the secret word with spaces in between each letter.
    print(letter, end=' ')
  print()
 
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = get_random_word(hm_module.words)

# print(display_board(missedLetters, correctLetters, secretWord))

def getGuess(alreadyGuessed):
  """Returns the letter the player entered. This function makes sure the player
  entered a single letter and not something else."""
  while True:
    print('Guess a letter.')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
      print('Please enter a single letter.')
    elif guess in alreadyGuessed:
      print("You have already guessed that letter. Choose again.")
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
      print("Please enter a LETTER.")
    else:
      return guess

def playAgain():
  """This function returns True if the player wants to play again;
  otherwise, it returns False."""
  print('Do you want to play again? (yes or no)')
  return input().lower().startswith('y')

print(playAgain())