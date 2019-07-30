import random

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MAX_PRICE = 100
MIN_PRICE = 1
INTIAL_Price = 10

price = INTIAL_Price
counter = []

while price>= MIN_PRICE and price<= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)
    price *= (1+price_change)
    counter.append(price)

for i in range(len(counter)):
    print("On day {0} price is ${1:.2f}".format(i+1, counter[i]))

print(price)
out_file = open('capitalist_conrad.txt', 'w+')
for i in range(len(counter)):
    print("${:,.2f}".format(counter[i]), file=out_file)
out_file.close()