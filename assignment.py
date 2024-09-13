# 4.1
def loop_over_list():
    """Loop over a list of fruits and print each one"""
    pcc_4_list = ['apple', 'banana', 'carrot', 'date']
    for fruit in pcc_4_list:
        print(fruit)

# 4.2
def loop_over_list_and_capitalize():
    """Loop over a list of fruits and print the index and the element capitalized
    Ex: 0: Apple
        1: Banana ..."""
    my_list = ["apple", "banana", "carrot", "date"]
    for index, fruit in enumerate(my_list):
        print(f"{index}: {fruit.capitalize()}")

# 4.3
def print_numbers_1_to_10():
    """Print the numbers 1 to 10 using a for loop"""
    for number in range(1, 11):
        print(number)

# 4.4
def print_numbers_1_to_n():
    """Print the numbers 1 to n"""
    n = 15
    for number in range(1, n + 1):
        print(number)

# 4.5
def create_list_of_numbers(n: int) -> list:
    """Create a list of numbers from 1 to n
    return the list"""
    return list(range(1, n + 1))

# 4.6
def create_list_of_even_numbers(n: int) -> list:
    """Create a list of even numbers from 1 to n
    return the list"""
    return [number for number in range(1, n + 1) if number % 2 == 0]

# 4.7
def create_list_of_first_ten_cube_numbers() -> list:
    """Create a list of the first ten cube numbers
    return the list"""
    return [x**3 for x in range(1, 11)]

# 4.8
def create_list_comprehension_of_first_ten_cube_numbers() -> list:
    """Create a list of the first ten cube numbers
    using list comprehension
    return the list"""
    return [x**3 for x in range(1, 11)]

# 4.9
def copy_list_and_append_11(my_list: list) -> list:
    """Copy the list and append the number 11 to the end
    return the new list
    Make sure not to modify the original list"""
    new_list = my_list.copy()
    new_list.append(11)
    return new_list

# 4.10
def return_first_index_of_tuple(my_tuple: tuple) -> int:
    """Return the first index of the tuple
    return the first index
    Remember that a tuple is like a list but immutable"""
    return my_tuple[0]

# 4.11
def loop_over_tuple():
    """Loop over the tuple and print each item"""
    my_tuple = (1, 2, 3, 4, 5)
    for item in my_tuple:
        print(item)
