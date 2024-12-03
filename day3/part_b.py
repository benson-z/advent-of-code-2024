import re

f = open("input.txt", 'r')
b = f.read()
f.close()

pattern = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')
matches = re.findall(pattern, b)

total = 0
enable = True
for m in matches:
    if m == "do()":
        enable = True
        continue
    if m == "don't()":
        enable = False 
        continue
    x, y = m.rstrip(')').lstrip('mul(').split(",")
    if enable:
        total += int(x) * int(y)

print(total)
