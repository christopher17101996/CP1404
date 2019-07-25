# for i in range(1, 21, 2):
#     print(i, end=' ')

# for j in range (0,100, 10):
#     print(j, end=' ')

# for k in range(20,0, -1):
#     print(k, end=' ')

stars = input("Enter number of stars")
stars = int(stars)

for l in range (0, stars):
    for m in range(0,l+1):
        print("*", end=' ')
    print("\r")
