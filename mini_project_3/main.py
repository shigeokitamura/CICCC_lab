"""
Hangman Game Project

Project Description:
In this project, you will create a text-based Hangman game using Python.
Hangman is a classic word-guessing game where the player tries to guess a word
by suggesting letters within a certain number of guesses. This project will help
you practice fundamental Python concepts such as loops, conditionals, functions,
and string manipulation.
"""

import random
import os
import sys
import time
from contextlib import redirect_stdout
from english_words import get_english_words_set
from PyDictionary import PyDictionary


def init_word() -> tuple[str, dict]:
    """
    Initializes a word for the Hangman game by retrieving a random English word
    and its meaning from an online dictionary.

    Returns:
        tuple[str, dict]: A tuple containing the selected word and its meaning.
    """

    print("Retrieving a word", end="")

    word_list = list(get_english_words_set(['web2'], alpha=True, lower=True))

    for _ in range(10):
        word = random.choice(word_list)
        # print(word)

        dictionary = PyDictionary()

        # stop stdout temporary
        with redirect_stdout(open(os.devnull, "w", encoding="utf-8")):
            meaning = dictionary.meaning(word)

        if isinstance(meaning, dict):
            print("\n")

            return word, meaning

        print(".", end="")
        time.sleep(1)

    print("\nCould not retrieve word. Please try later.")
    sys.exit(1)

def check_letter_input(letter: str) -> bool:
    """
    Validates the user's input for a letter guess.

    Args:
        letter (str): The letter input from the user.

    Returns:
        bool: True if the input is valid, False otherwise.
    """

    if len(letter) != 1:
        print(f"Your input '{letter}' is invalid, please enter only one letter.")
        return False

    if letter == "?":
        return True

    if not letter.isalpha():
        print(f"Your input '{letter}' is invalid, please enter a letter.")
        return False

    if not letter.islower():
        print(f"Your input '{letter}' is invalid, please enter a letter in lowercase")
        return False

    return True

def get_user_guess(guessed_letters: list, meaning: dict) -> str:
    """
    Retrieves and validates the user's letter guess.

    Args:
        guessed_letters (list): A list of letters that have already been guessed.
        meaning (dict): The meaning of the word.

    Returns:
        str: The letter guessed by the user.
    """

    while True:
        letter = input("Guess a letter(type '?' for hint): ")
        if not check_letter_input(letter):
            continue
        if letter == "?":
            print(meaning)
        elif letter in guessed_letters:
            print(f"You have already guessed '{letter}'")
        else:
            return letter

def update_game_state(letter: str, word: str, answer: list, life: int) -> tuple[list, int]:
    """
    Updates the game state based on the user's guess.

    Args:
        letter (str): The letter guessed by the user.
        word (str): The correct word.
        answer (list): The current state of the guessed word.
        life (int): The remaining life count.

    Returns:
        tuple: The updated state of the guessed word and the remaining life.
    """
    if (letter in word) and (letter not in answer):
        print(f"Good job! '{letter}' is in the word.")
        for idx, char in enumerate(word):
            if char == letter:
                answer[idx] = letter
    else:
        print(f"Sorry, '{letter}' is not in the word.")
        life -= 1

    return answer, life

def hangman() -> None:
    """
    Main function to run the Hangman game. It handles the game loop,
    user input, and displays the current state of the game.

    Returns:
        None
    """

    print("Welcome to Hangman!\n")
    word, meaning = init_word()

    answer = ["_"] * len(word)
    life = len(word)

    while "_" in answer:
        print(f"Current word: {' '.join(answer)}")
        guessed_letters = list(set(filter(lambda x: x != "_", answer)))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Incorrect guesses remaining: {life}")

        letter = get_user_guess(guessed_letters, meaning)

        answer, life = update_game_state(letter, word, answer, life)
        if life <= 0:
            print(f"Game over! The word was: {word}\n")
            return

        print()

    print(f"Congratulations! You guessed the word: {word}\n")

def main():
    """
    Main entry point of the program. It starts the Hangman game and
    prompts the user to play again after the game ends.

    Returns:
        None
    """

    hangman()

    while True:
        again = input("Play again? [y/n]: ")
        if again == "y":
            hangman()
        elif again == "n":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
