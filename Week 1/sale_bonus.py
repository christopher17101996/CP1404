"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales > 0:
    if sales < 1000:
        result = sales * 0.1
    else:
        result = sales * 0.15
    print("You get {:.2f} bonus".format(result))
else:
    print("Input wrong number")