"""
Part 1: Mod and Integer Division
Question: How can I use mod (%) and integer division (/) to figure out the nth digit of an
Integer?
"""

def main():
    """
    Main function to run the program.
    """

    while True:
        try:
            number = input("number: ")
            num_digits = len(number)
            number = int(number)
            if number <= 0:
                raise ValueError("Number must be positive")

            n = int(input("n: "))
            if n <= 0:
                raise ValueError("n must be positive")

            if n > num_digits:
                raise ValueError(
                    f"The specified position {n} exceeds the number of digits {num_digits} in {number}"
                )
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    # Calculate the nth digit from the right
    nth_digit: int = (number // 10 ** (n - 1)) % 10

    print(f"The {n}th digit from the right is {nth_digit}")

if __name__ == "__main__":
    main()
