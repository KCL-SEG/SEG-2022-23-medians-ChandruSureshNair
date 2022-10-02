"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
    except ValueError:
        print("Some input could not be converted to a number!")
    except EOFError:
        exit()
    else:
        n = len(numbers)
        median = 0
        if n == 1:
            median = numbers[0]
        elif n % 2:
            median = numbers[n//2]
        else:
            median = (numbers[n//2 - 1] + numbers[n//2]) / 2.0
        
        print(median, flush=True)
