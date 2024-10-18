"""
Lab 4 - Python Data Structures
Dictionaries & Tuples & List Exercises
"""

def exercise_1() -> None:
    """
    Exercise 1: Student Grades Analysis

    Tasks:
    1. Dictionaries & Tuples & List Exercises
    2. Find and print the name of the student with the highest average score.
    3. Find and print the name of the student , with the lowest average score.
    4. Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary.
    """

    print("Exercise 1: Student Grades Analysis")

    students = {
        "Alice": [85, 78, 92],
        "Bob": [79, 74, 81],
        "Charlie": [91, 82, 85],
        "David": [76, 85, 83],
        "Eve": [88, 79, 92]
    }

    print("Task 1. Average scores:")
    average_scores = {name: sum(scores) / len(scores) for name, scores in students.items()}
    print(average_scores)
    print()

    print("Task 2. Student with the highest average score:")
    student = max(average_scores, key=average_scores.get)
    print(f"{student}: {average_scores[student]}")
    print()

    print("Task 3. Student with the lowest average score:")
    student = min(average_scores, key=average_scores.get)
    print(f"{student}: {average_scores[student]}")
    print()

    print("Task 4. Updated dictionary:")
    students["Frank"] = [80, 90, 85]
    print(students)
    print()

def exercise_2() -> None:
    """
    Exercise 2: Product Inventory Management

    Tasks:
    1. Print the current inventory in a user-friendly format.
    2. Calculate and print the total value of the inventory.
    3. Add a new product "mango" with 30 items priced at $0.6 each to the inventory.
    4. Update the quantity of "banana" to 120 and print the updated inventory.
    5. Remove "pear" from the inventory and print the updated inventory.
    """

    print("Exercise 2: Product Inventory Management")

    inventory = {
        "apple": (50, 0,5),
        "banana": (100, 0.2),
        "orange": (75, 0.3),
        "pear": (20, 0.4)
    }

    print("Task 1. Current inventory:")
    for product, details in inventory.items():
        print(f"{product}: {details[0]} items, ${details[1]} each")
    print()

    print("Task 2. Total value of the inventory:")
    total_value = sum(details[0] * details[1] for details in inventory.values())
    print(f"Total value: ${total_value:.2f}")
    print()

    print("Task 3. Updated inventory:")
    inventory["mango"] = (30, 0.6)
    for product, details in inventory.items():
        print(f"{product}: {details[0]} items, ${details[1]} each")
    print()

    print("Task 4. Updated inventory:")
    inventory["banana"] = (120, 0.2)
    for product, details in inventory.items():
        print(f"{product}: {details[0]} items, ${details[1]} each")
    print()

    print("Task 5. Updated inventory:")
    del inventory["pear"]
    for product, details in inventory.items():
        print(f"{product}: {details[0]} items, ${details[1]} each")
    print()

def exercise_3() -> None:
    """
    Exercise 3: Employee Records

    Tasks:
    1. Print the names and departments of all employees.
    2. Print the email addresses of all employees in alphabetical order by their last names.
    3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com") and print the updated list.
    4. Find and print the department of "Jane Smith."
    """

    print("Exercise 3: Employee Records")

    employees = [
        ("John Doe", "Accounting", "john.doe@example.com"),
        ("Jane Smith", "Marketing", "jane.smith@example.com"),
        ("Emily Davis", "HR", "emily.davis@example.com"),
        ("Michael Brown", "IT", "michael.brown@example.com")
    ]

    print("Task 1. Names and departments of all employees:")
    for name, department, email in employees:
        print(f"{name}, {department}")
    print()

    print("Task 2. Email addresses in alphabetical order by last name:")
    sorted_employees = sorted(employees, key=lambda x: x[0].split()[-1])
    for name, department, email in sorted_employees:
        print(email)
    print()

    print("Task 3. Updated list of employees:")
    employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
    print(employees)
    print()

    print("Task 4. Department of Jane Smith:")
    for name, department, email in employees:
        if name == "Jane Smith":
            print(department)
    print()

def exercise_4() -> None:
    """
    Exercise 4: Book Library System

    Tasks:
    1. Print the details of all books in a user-friendly format.
    2. Find and print the details of the book with the ISBN "978-0-14-028329-7".
    3. Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", and year 1925.
    4. Update the year of "To Kill a Mockingbird" to 1961 and print the updated details.
    5. Remove the book with ISBN "978-0-452-28423-4" and print the updated library.
    """

    print("Exercise 4: Book Library System")

    library = {
        "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
        "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
        "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
        "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
    }

    print("Task 1. Details of all books:")
    for isbn, details in library.items():
        print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Year: {details['year']}")
    print()

    print("Task 2. Details of the book with ISBN 978-0-14-028329-7:")
    print(library["978-0-14-028329-7"])
    print()

    print("Task 3. Updated library:")
    library["978-1-4028-9462-6"] = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
    for isbn, details in library.items():
        print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Year: {details['year']}")
    print()

    print("Task 4. Updated details of To Kill a Mockingbird:")
    library["978-0-7432-7356-5"]["year"] = 1961
    print(library["978-0-7432-7356-5"])
    print()

    print("Task 5. Updated library:")
    del library["978-0-452-28423-4"]
    print(library)
    print()

def exercise_5() -> None:
    """
    Exercise 5: City Population Data

    Tasks:
    1. Print the population of each city in a user-friendly format.
    2. Find and print the city with the highest population.
    3. Find and print the city with the lowest population.
    4. Update the population of "Phoenix" to 1700000 and print the updated data.
    5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
    """

    print("Exercise 5: City Population Data")

    cities = {
        "New York": 8419000,
        "Los Angeles": 3980000,
        "Chicago": 2716000,
        "Houston": 2328000,
        "Phoenix": 1690000
    }

    print("Task 1. Population of each city:")
    for city, population in cities.items():
        print(f"{city}: {population}")
    print()

    print("Task 2. City with the highest population:")
    city = max(cities, key=cities.get)
    print(f"{city}: {cities[city]}")
    print()

    print("Task 3. City with the lowest population:")
    city = min(cities, key=cities.get)
    print(f"{city}: {cities[city]}")
    print()

    print("Task 4. Updated population of Phoenix:")
    cities["Phoenix"] = 1700000
    print(cities)
    print()

    print("Task 5. Updated data:")
    cities["San Francisco"] = 884000
    print(cities)
    print()

def exercise_6() -> None:
    """
    Exercise 6: Movie Database

    Tasks:
    1. Print the details of all movies in a user-friendly format.
    2. Find and print the highest-rated movie.
    3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
    4. Update the rating of "Inception" to 9.0 and print the updated details.
    5. Remove "Pulp Fiction" from the database and print the updated list.
    """

    print("Exercise 6: Movie Database")

    movies = {
        "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
        "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
        "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
        "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
        "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
    }

    print("Task 1. Details of all movies:")
    for movie, details in movies.items():
        print(f"{movie}: {details['year']}, {details['rating']}, {details['genre']}")
    print()

    print("Task 2. Highest-rated movie:")
    movie = max(movies, key=lambda x: movies[x]['rating'])
    print(f"{movie}: {movies[movie]['rating']}")
    print()

    print("Task 3. Updated movie database:")
    movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}
    print(movies)
    print()

    print("Task 4. Updated details of Inception:")
    movies["Inception"]["rating"] = 9.0
    print(movies["Inception"])
    print()

    print("Task 5. Updated movie database:")
    del movies["Pulp Fiction"]
    print(movies)
    print()

def exercise_7() -> None:
    """
    Exercise 7: Country Capitals

    Tasks:
    1. Print the names of all countries and their capitals.
    2. Find and print the capital of Germany.
    3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
    4. Update the capital of "USA" to "New Washington" and print the updated
    dictionary.
    5. Remove "France" from the dictionary and print the updated dictionary.
    """

    print("Exercise 7: Country Capitals")

    countries = {
        "USA": "Washington, D.C.",
        "Canada": "Ottawa",
        "France": "Paris",
        "Germany": "Berlin",
        "Japan": "Tokyo"
    }

    print("Task 1. Names of all countries and their capitals:")
    for country, capital in countries.items():
        print(f"{country}: {capital}")
    print()

    print("Task 2. Capital of Germany:")
    print(countries["Germany"])
    print()

    print("Task 3. Updated dictionary:")
    countries["Australia"] = "Canberra"
    print(countries)
    print()

    print("Task 4. Updated dictionary:")
    countries["USA"] = "New Washington"
    print(countries)
    print()

    print("Task 5. Updated dictionary:")
    del countries["France"]
    print(countries)
    print()

def exercise_8() -> None:
    """
    Exercise 8: Shopping Cart

    Tasks:
    1. Print the details of all items in the cart.
    2. Calculate and print the total cost of the cart.
    3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
    4. Update the quantity of "banana" to 10 and print the updated cart.
    5. Remove "pear" from the cart and print the updated cart.
    """

    print("Exercise 8: Shopping Cart")

    cart = [
        {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
        {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
        {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
        {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
    ]

    print("Task 1. Details of all items in the cart:")
    for item in cart:
        print(f"{item['item']}: {item['quantity']} units, ${item['price_per_unit']} each")
    print()

    print("Task 2. Total cost of the cart:")
    total_cost = sum(item['quantity'] * item['price_per_unit'] for item in cart)
    print(f"Total cost: ${total_cost}")
    print()

    print("Task 3. Updated cart:")
    cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})
    for item in cart:
        print(f"{item['item']}: {item['quantity']} units, ${item['price_per_unit']} each")
    print()

    print("Task 4. Updated cart:")
    for item in cart:
        if item['item'] == "banana":
            item['quantity'] = 10
    print(cart)
    print()

    print("Task 5. Updated cart:")
    for item in cart:
        if item['item'] == "pear":
            cart.remove(item)
    print(cart)
    print()

def exercise_9() -> None:
    """
    Exercise 9: Weather Data

    Tasks:
    1. Print the weather details for each day.
    2. Find and print the day with the highest temperature.
    3. Find and print the day with the lowest humidity.
    4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
    5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated weather data.    """

    print("Exercise 9: Weather Data")

    weather = {
        "Monday": {"temperature": 20, "humidity": 60},
        "Tuesday": {"temperature": 22, "humidity": 55},
        "Wednesday": {"temperature": 19, "humidity": 65},
        "Thursday": {"temperature": 23, "humidity": 50},
        "Friday": {"temperature": 21, "humidity": 70}
    }

    print("Task 1. Weather details for each day:")
    for day, details in weather.items():
        print(f"{day}: Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%")
    print()

    print("Task 2. Day with the highest temperature:")
    day = max(weather, key=lambda x: weather[x]['temperature'])
    print(f"{day}: Temperature: {weather[day]['temperature']}°C")
    print()

    print("Task 3. Day with the lowest humidity:")
    day = min(weather, key=lambda x: weather[x]['humidity'])
    print(f"{day}: Humidity: {weather[day]['humidity']}%")
    print()

    print("Task 4. Updated temperature of Wednesday:")
    weather["Wednesday"]["temperature"] = 25
    print(weather["Wednesday"])
    print()

    print("Task 5. Updated weather data:")
    weather["Saturday"] = {"temperature": 24, "humidity": 60}
    print(weather)
    print()

def exercise_10() -> None:
    """
    Exercise 10: Library Members

    Tasks:
    1. Print the names and ages of all members.
    2. Find and print the books borrowed by "Charlie".
    3. Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
    4. Update the age of "Bob" to 31 and print the updated list.
    5. Remove "David" from the list and print the updated list.
    """

    print("Exercise 10: Library Members")

    members = [
        {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
        {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
        {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
        {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
    ]

    print("Task 1. Names and ages of all members:")
    for member in members:
        print(f"{member['name']}: {member['age']}")
    print()

    print("Task 2. Books borrowed by Charlie:")
    for member in members:
        if member['name'] == "Charlie":
            print(member['books_borrowed'])
    print()

    print("Task 3. Updated list of members:")
    members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})
    print(members)
    print()

    print("Task 4. Updated age of Bob:")
    for member in members:
        if member['name'] == "Bob":
            member['age'] = 31
    print(members)
    print()

    print("Task 5. Updated list of members:")
    for member in members:
        if member['name'] == "David":
            members.remove(member)
    print(members)

def main():
    """
    Main function to run all tasks
    """

    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()
    exercise_10()

if __name__ == "__main__":
    main()
