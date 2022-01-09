import random

# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []

word_length = len(chosen_word)

lives = 6

end_game = False


for char in chosen_word:
    display.append("_")


while end_game == False:
    guess = input("Guess a letter").lower()

    for index in range(0, word_length):
        char = chosen_word[index]
        if char == guess:
            display[index] = guess

    if char != guess:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lost")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
