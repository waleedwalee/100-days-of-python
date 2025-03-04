import random

# Hangman ASCII stages
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

# Hangman logo
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
'''

print(logo)


lives = 6
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


li = ["_"] * len(chosen_word)

# Store guessed letters to avoid repeated inputs
guessed_letters = []

while "_" in li and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
        continue

    # Add guess to guessed letters list
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                li[index] = guess
        print("✅ Correct guess!")
    else:
        lives -= 1
        print(f"❌ Wrong guess! You have {lives} lives left.")

    # Display the current word progress
    print(" ".join(li))
    print(stages[lives])  # Show Hangman stage

if "_" not in li:
    print("\n🎉 Congratulations! You guessed the word! 🎉")
else:
    print("\n💀 You Lose! The word was:", chosen_word)
