from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)
    # return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman and the current state of the word."""
    # Display the snowman stage for the current number of mistakes.
    print("\n" + STAGES[min(mistakes, len(STAGES) - 1)])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)


def ask_for_letter():
    """Prompts the user to enter a single alphabetic letter."""
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a single letter (a–z).")


def ask_play_again():
    """Asks the user whether to play another round."""
    while True:
        response = input("Would you like to play again? (y/n): ").lower().strip()
        if response in ["y", "n"]:
            return response == "y"
        print("Please enter 'y' or 'n'.")


def play_game():
    """Runs one round of the Snowman game."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = ask_for_letter()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Sorry, that's not in the word.")
            mistakes += 1
            guessed_letters.append(guess)

        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations! You saved the snowman!")
            break

        if mistakes >= max_mistakes:
            print(f"💥 Game over. The word was: {secret_word}")
            break

    if ask_play_again():
        play_game()
    else:
        print("Thanks for playing. Goodbye!")


if __name__ == "__main__":
    play_game()
