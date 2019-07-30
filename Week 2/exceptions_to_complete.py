"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    result = input("Enter a number:\t")
    try:
        result = int(result)
        break
    except ValueError:
        print("Please enter only number.")
        result = input("Enter a number")
print("Valid result is:", result)