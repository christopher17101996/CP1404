e = open("names.txt", "w+")
e.write("Your name is Bob")
e.close()
f = open("numbers.txt", "w+")
for j in range(2):
    f.write("%d\n" % (j+1))
f.close()
total = 0
g = open("numbers.txt", "r")

for line in g:
    num = int(line)
    total += num

print(total)
g.close()