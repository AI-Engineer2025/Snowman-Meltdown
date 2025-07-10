from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[min(mistakes, len(STAGES) - 1)])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    # print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = 3

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter only letters and a single Letter.")
            continue

        # GANZES WORT geraten?
        # if len(guess) > 1:
        # if guess == secret_word:
        # rint("Amazing! You guessed the word!")
        # print("You saved the snowman!")
        # break
        # else:
        # mistakes += 1
        # print("Wrong word!")
        # display_game_state(mistakes, secret_word, guessed_letters)
        else:
            # EIN BUCHSTABE geraten
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("Correct!")
            else:
                print("Sorry, that's not in the word.")
                mistakes += 1

            display_game_state(mistakes, secret_word, guessed_letters)

            # Gewinnprüfung
            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! you saved the snowman!")
                new_game = input("Would you like to play again? (y/n): ").lower()
                if new_game == "n":
                    print("Thank you for playing!")
                elif new_game == "y":
                    play_game()
                break

        # Verlustprüfung
        if mistakes >= max_mistakes:
            print(f"Game over. The word was: {secret_word}")
            new_game = input("Would you like to play again? (y/n): ").lower()
            if new_game == "n":
                print("Thank you for playing!")
            elif new_game == "y":
                play_game()
            break


if __name__ == "__main__":
    play_game()
