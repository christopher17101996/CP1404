# def shopCalculator():
MENU = """Please enter your item numbers and then type each item price"""
print(MENU)
itmNumber = input("Enter item number >>>")
total = 0
while itmNumber is not None:
    try:
        item = int(itmNumber)
        if item > 0:
            for i in range(item):
                itmPrice = input("Enter your item price: $")
                while itmPrice is not None:
                    try:
                        price = int(itmPrice)
                        total = total + price
                        break
                    except ValueError:
                        print("Please enter correct price")
                    itmPrice = input("Enter your item price: $")

            if total > 100:
                discount = total*0.1
                total = total-discount
            print(total)
            break
        else:
            print("Item number must be greater than ZERO")
    except ValueError:
        print("Please enter number only")
    itmNumber = input("Enter item number >>>")
print("Thank You!")
# shopCalculator()
