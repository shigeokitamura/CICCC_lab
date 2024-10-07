"""
Part 2: Star Drawings with Nested Loops
"""

def get_valid_input() -> int:
    """
    Get a valid input from the user.

    Raises:
        ValueError: If the input is not a positive integer.

    Returns:
        int: Number of rows.
    """

    while True:
        try:
            n = int(input("n: "))
            if n <= 0:
                raise ValueError("Number must be positive")

            return n
        except ValueError as e:
            print(f"Invalid input: {e}")

def print_pyramid(n: int) -> None:
    """
    Print a pyramid with n rows.

    Args:
        n (int): Number of rows.
    """

    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    print()

def print_triangle_1(n: int) -> None:
    """
    Print a triangle with n rows.

    Args:
        n (int): Number of rows.
    """

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
    print()

def print_triangle_2(n: int) -> None:
    """
    Print a triangle with n rows.

    Args:
        n (int): Number of rows.
    """

    for i in range(n):
        if i < n // 2:
            for j in range(i + 1):
                print("*", end="")
            print()
        else:
            for j in range(n - i):
                print("*", end="")
            print()
    print()

def print_hourglass(n: int) -> None:
    """
    Print an hourglass with n rows.

    Args:
        n (int): Number of rows.
    """

    for i in range(n):
        if i < n // 2:
            for j in range(i):
                print(" ", end="")
            for j in range(n - 2 * i):
                print("*", end="")
        else:
            for j in range(n - i - 1):
                print(" ", end="")
            for j in range(2 * i - n + 2):
                print("*", end="")
        print()
    print()

def print_diamond(n: int) -> None:
    """
    Print a diamond with n rows.

    Args:
        n (int): Number of rows.
    """

    for i in range(n):
        if i < n // 2:
            for j in range((n + 1) // 2 - i - 1):
                print(" ", end="")
            for j in range(2 * i + 1):
                print("*", end="")
        else:
            for j in range(i - n // 2):
                print(" ", end="")
            for j in range(2 * (n - i) - 1):
                print("*", end="")
        print()
    print()

def main() -> None:
    """
    Main function to run the program.
    """

    n = get_valid_input()
    print_pyramid(n)
    print_triangle_1(n)
    print_triangle_2(n)
    print_hourglass(n)
    print_diamond(n)

if __name__ == "__main__":
    main()
