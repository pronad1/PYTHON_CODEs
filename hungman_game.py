import random

def choose_random_word():
    """Selects a random word from a predefined list."""
    word_list = ["python", "hangman", "programming", "developer", "function", "variable"]
    return random.choice(word_list)

def display_current_state(word, guessed_letters):
    """Displays the current state of the word with guessed letters."""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def play_hangman():
    word = choose_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_current_state(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess.")
        
        if set(word) <= guessed_letters:
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    play_hangman()
