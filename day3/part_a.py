import re

f = open("input.txt", 'r')
b = f.read()
f.close()

pattern = r'mul\(\d+,\d+\)'
matches = re.findall(pattern, b)

total = 0
for m in matches:
    x, y = m.rstrip(')').lstrip('mul(').split(",")
    total += int(x) * int(y)

print(total)
