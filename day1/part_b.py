list1 = []
list2 = []

with open("input.txt") as file:
    for l in file:
        a, b = l.split("  ")
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

total = 0
for a in list1:
    for b in list2:
        if b == a:
            total += a

print(total)
