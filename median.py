"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        n = len(numbers)
        if n % 2:
            median = numbers[n//2]
            print(median)
        else:
            median = (numbers[n//2 - 1] + numbers[n//2]) / 2.0
            print(median)
