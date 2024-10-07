"""Guessing Game"""

import random

def update_range(number: int, input_number: int, min_number: int, max_number: int) -> tuple[int]:
    """
    Update the range of input number.

    Args:
        number (int): the answer.
        input_number (int): the number user input.
        min_number (int): current min number.
        max_number (int): current max number.

    Returns:
        tuple[int]: updated min number and max number.
    """

    if input_number > number:
        max_number = input_number - 1
    else:
        min_number = input_number + 1

    return (min_number, max_number)

def main() -> None:
    """
    Main function.
    """

    min_number = 1
    max_number = 1000
    guess_count = 1

    number = random.randint(min_number, max_number)

    while True:
        try:
            input_number = input(f"Enter your guess from {min_number} to {max_number}: ")
            input_number = int(input_number)
        except ValueError:
            print(f"Your input '{input_number}' is invalid. Please enter a valid number.")
            continue

        if (input_number < min_number) or (max_number < input_number):
            print(
                f"Your input {input_number} is out of range. " \
                f"Please enter a number from {min_number} to {max_number}"
            )
            continue

        if input_number == number:
            break

        print(f"Wrong! Guess count: {guess_count}")
        min_number, max_number = update_range(number, input_number, min_number, max_number)
        guess_count += 1

    print(f"You got it! The hidden number is {number}")
    print(f"It took you {guess_count} guess(es).")

if __name__ == "__main__":
    main()
