"""
Binary search implementation in Python
"""


import random


def create_array(size):
    """
    Creates an array based on how many elements the user wants to enter.
    """

    # Create an empty array
    input_array = []

    # Generate random numbers and append them to the array
    for _ in range(size):
        input_array.append(random.randint(1, 200_000))

    # Sort the array
    sorted_arr = sorted(input_array)

    return sorted_arr


def binary_search(input_array, target):
    """
    Returns the index position of the target if found, else returns -1
    """

    low, high = 0, len(input_array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_array[mid]

        if mid_value == target:
            return mid  # The target value was found, return its index
        if mid_value < target:
            low = mid + 1  # Target value is in the right half, update low
        else:
            high = mid - 1  # Target value is in the left half, update high

    return -1  # The target value was not found in the list


TRIES = 0

DEF_VALUE = random.randint(1, 200_000)

VALUE = input(f"Enter a value to search for else {DEF_VALUE} will be used: ")

if VALUE == "":
    VALUE = DEF_VALUE

else:
    VALUE = int(VALUE)


while True:
    arr = create_array(20_000)

    index = binary_search(arr, VALUE)

    if index == -1:
        TRIES += 1

    elif index != -1:
        print(f"Found {VALUE} at index {index} after {TRIES} tries.")
        break
