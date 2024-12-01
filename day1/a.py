total = 0
list1 = []
list2 = []

with open("input.txt") as file:
    for l in file:
        a, b = l.split("  ")
        list1.append(int(a))
        list2.append(int(b))

list1.sort()
list2.sort()

for a, b in zip(list1, list2):
    total += abs(a-b)

print(total)
