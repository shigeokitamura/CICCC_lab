"""
Lab 3 - Exploring NumPy Arrays and Random Value Generation
"""

import numpy as np

def task_1():
    """
    Task 1: Creating a 1D NumPy Array
    * Create a NumPy array containing the numbers from 1 to 30.
    * Print the array and its shape.
    * Access and print the element at index 10.
    """

    print("Task 1: Creating a 1D NumPy Array")

    # Create a NumPy array containing the numbers from 1 to 30
    array = np.arange(1, 31)

    # Print the array and its shape
    print(f"Array: {array}")
    print(f"Shape: {array.shape}")

    # Access and print the element at index 10
    print(f"Element at index 10: {array[10]}\n")


def task_2():
    """
    Task 2: Creating a 2D NumPy Array
    * Reshape the 1D array from Task 1 into a 2D array of shape (6, 5).
    * Print the entire 2D array.
    * Access and print the element at row 3, column 4.
    """

    print("Task 2: Creating a 2D NumPy Array")

    # Reshape the 1D array from Task 1 into a 2D array of shape (6, 5)
    array = np.arange(1, 31).reshape(6, 5)

    # Print the entire 2D array
    print(f"2D Array:\n{array}")

    # Access and print the element at row 3, column 4
    print(f"Element at row 3, column 4: {array[3, 4]}\n")

def task_3():
    """
    Task 3: Subsetting a 2D Array
    * Extract and print the third row from the 2D array created in Task 2.
    * Extract and print the first two rows and the last three columns.
    """

    print("Task 3: Subsetting a 2D Array")
    array = np.arange(1, 31).reshape(6, 5)

    # Extract and print the third row from the 2D array created in Task 2
    print(f"Third row: {array[2]}")

    # Extract and print the first two rows and the last three columns
    print(f"First two rows and last three columns:\n{array[:2, -3:]}\n")

def task_4():
    """
    Task 4: Generating Random Integer Array
    * Use the `numpy.random` module to generate a 1D array of 15 random integers between 10 and 100.
    * Print the array and find its maximum and minimum values.
    """

    print("Task 4: Generating Random Integer Array")

    # Generate a 1D array of 15 random integers between 10 and 100
    array = np.random.randint(10, 101, size=15)

    # Print the array and find its maximum and minimum values
    print(f"Array: {array}")
    print(f"Maximum value: {array.max()}")
    print(f"Minimum value: {array.min()}\n")

def task_5():
    """
    Task 5: Generating a 2D Random Array
    * Generate a 2D array of shape (4, 4) with random integers between 0 and 50.
    * Print the array and find the sum of all the elements in the array.
    """

    print("Task 5: Generating a 2D Random Array")

    # Generate a 2D array of shape (4, 4) with random integers between 0 and 50
    array = np.random.randint(0, 51, size=(4, 4))

    # Print the array and find the sum of all the elements in the array
    print(f"Array:\n{array}")
    print(f"Sum of all elements: {array.sum()}\n")

def task_6():
    """
    Task 6: Manipulating Arrays
    * Create a 2D array of random integers (shape 5, 5) between 1 and 20.
    * Print the array.
    * Set all values in the second row to 0.
    * Replace all values greater than 10 with the value 99.
    """

    print("Task 6: Manipulating Arrays")

    # Create a 2D array of random integers (shape 5, 5) between 1 and 20
    array = np.random.randint(1, 21, size=(5, 5))

    # Print the array
    print(f"Original Array:\n{array}")

    # Set all values in the second row to 0
    array[1] = 0

    # Replace all values greater than 10 with the value 99
    array[array > 10] = 99

    # Print the modified array
    print(f"Modified Array:\n{array}\n")

def task_7():
    """
    Task 7: Arithmetic Operations on Arrays
    * Create two 1D arrays of length 5 with random integers between 1 and 10.
    * Perform element-wise addition, subtraction, and multiplication on the two arrays.
    * Print the results.
    """

    print("Task 7: Arithmetic Operations on Arrays")

    # Create two 1D arrays of length 5 with random integers between 1 and 10
    array1 = np.random.randint(1, 11, size=5)
    array2 = np.random.randint(1, 11, size=5)

    # Perform element-wise addition, subtraction, and multiplication on the two arrays
    addition = array1 + array2
    subtraction = array1 - array2
    multiplication = array1 * array2

    # Print the results
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}\n")

def task_8():
    """
    Task 8: Broadcasting in Numpy
    * Create a 1D array of length 4 with values [2, 4, 6, 8].
    * Create a 2D array of shape (3, 4) with random integers between 1 and 5.
    * Add the 1D array to each row of the 2D array using broadcasting, then print the result.
    """

    print("Task 8: Broadcasting in Numpy")

    # Create a 1D array of length 4 with values [2, 4, 6, 8]
    array1 = np.array([2, 4, 6, 8])

    # Create a 2D array of shape (3, 4) with random integers between 1 and 5
    array2 = np.random.randint(1, 6, size=(3, 4))

    # Add the 1D array to each row of the 2D array using broadcasting
    result = array2 + array1

    # Print the result
    print(f"Array 1: {array1}")
    print(f"Array 2:\n{array2}")
    print(f"Result:\n{result}\n")

def task_9():
    """
    Task 9: Filtering an Array
    * Generate a 1D array of 20 random integers between 1 and 100.
    * Print all elements of the array that are greater than 50.
    * Replace all values less than 30 with -1 and print the modified array.
    """

    print("Task 9: Filtering an Array")

    # Generate a 1D array of 20 random integers between 1 and 100
    array = np.random.randint(1, 101, size=20)

    # Print all elements of the array that are greater than 50
    print(f"Elements greater than 50: {array[array > 50]}")

    # Replace all values less than 30 with -1 and print the modified array
    array[array < 30] = -1
    print(f"Modified Array: {array}\n")

def task_10():
    """
    Task 10: Reshaping Arrays
    * Create a 1D array of 12 random integers between 1 and 50.
    * Reshape the array into a 3x4 2D array.
    * Transpose the array (swap rows and columns) and print the result.
    """

    print("Task 10: Reshaping Arrays")

    # Create a 1D array of 12 random integers between 1 and 50
    array = np.random.randint(1, 51, size=12)

    # Reshape the array into a 3x4 2D array
    array = array.reshape(3, 4)

    # Transpose the array and print the result
    print(f"Original Array:\n{array}")
    print(f"Transposed Array:\n{array.T}\n")


def main():
    """
    Main function to run all tasks
    """

    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()

if __name__ == "__main__":
    main()
