# 2. Hangman: Implement the wordguessing game with visual
#  progress and hints. 



import random

# Hangman stages (visuals)
HANGMANPICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# Word bank with categories for hints
WORD_BANK = {
    "Fruits": ["apple", "banana", "orange", "grape", "mango"],
    "Animals": ["tiger", "elephant", "giraffe", "kangaroo", "zebra"],
    "Countries": ["india", "canada", "brazil", "france", "japan"]
}

def get_random_word():
    category = random.choice(list(WORD_BANK.keys()))
    word = random.choice(WORD_BANK[category])
    return word, category

def display_game_state(word, guessed_letters, incorrect_guesses, category):
    print(HANGMANPICS[incorrect_guesses])
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print("\nWord: ", display_word)
    print("Category (hint):", category)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))

def hangman():
    word, category = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = len(HANGMANPICS) - 1

    print("🎮 Welcome to Hangman!")
    print("Hint: The word belongs to category ->", category)

    while incorrect_guesses < max_attempts:
        display_game_state(word, guessed_letters, incorrect_guesses, category)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print("\n🎉 Congratulations! You guessed the word:", word)
                break
        else:
            print("❌ Wrong guess!")
            incorrect_guesses += 1

    else:
        display_game_state(word, guessed_letters, incorrect_guesses, category)
        print("\n💀 You lost! The word was:", word)

def main():
    while True:
        hangman()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("👋 Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()
