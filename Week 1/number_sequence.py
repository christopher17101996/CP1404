# for num in range (100):
#     for i in range (num):
#         print (num, end=" ")
#     print("\n")

SMENU = """S - To start\nQ - To Exit"""
MENU = """Enter O to see odd number sequence \nEnter E to see even number sequecne\nEnter S to see square number sequence"""
print(SMENU)

sinput = input(">>>").upper()
while sinput !="Q":
    if sinput == "S":
        start = input("Enter your start number: ")
        end = input("Enter your end number: ")
        try:
            cstart = int(start)
            cend = int(end)
            print(MENU)
            choice = input(">>>").upper()
            if choice == "E":
                for num in range(cstart, cend + 1):
                    if num % 2 == 0:
                        print(num, end=" ")

            elif choice == "O":
                for num in range(cstart, cend + 1):
                    if num % 2 == 1:
                        print(num, end=" ")

            elif choice == "S":
                for num in range(cstart, cend + 1):
                    print(num ** 2, end=" ")

            else:
                print("Please enter correct input")
            break

        except ValueError:
            print("Please enter number only")
    else:
        print("Your input is Invalid")
        print(SMENU)
        sinput = input(">>>").upper()
print("\nThank You!")