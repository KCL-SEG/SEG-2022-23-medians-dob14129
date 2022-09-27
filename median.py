"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()
length = len(numbers)
if length % 2 == 0:
    first = numbers[int((length / 2) - 1)]
    second = numbers[int(length / 2)]
    print((first + second) / 2)
else:
    print(numbers[int((length - 1) / 2)])
