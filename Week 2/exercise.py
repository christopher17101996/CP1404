import random

MAX_INCREASE = 15
MIN_LENGTH = 2
MAX_LENGTH = random.randint(3, MAX_INCREASE)
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():

    word = ""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    for rad in password:
        word += str(random.choice(password))
    print("Your {}-character password is valid: {}".format(len(password),password))
    print("Your random username is\t{}".format(word))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1


    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False

    return True

main()