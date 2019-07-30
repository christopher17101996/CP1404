"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

while denominator!=0:
    try:
        cn = int(numerator)
        cd = int(denominator)
        fraction = cn / cd
        print(fraction)
        break
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
        numerator = input("Enter the numerator: ")
        denominator = input("Enter the denominator: ")
    except ZeroDivisionError:
        print("Cannot divide by zero! Please reenter your numbers")
        denominator = input("Enter the denominator: ")
print("Finished.")