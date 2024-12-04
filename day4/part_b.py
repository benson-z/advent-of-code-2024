import re
mat=[]
with open("input.txt") as f:
    for l in f:
        mat.append(list(l)[:-1])

total = 0
for r in range(1, len(mat)-1):
    for c in range(1, len(mat[0])-1):
        if mat[r][c] == 'A':
            tl = mat[r-1][c-1]
            tr = mat[r-1][c+1]
            bl = mat[r+1][c-1]
            br = mat[r+1][c+1]
            if tl == 'M' and br == 'S':
                if tr == 'M' and bl == 'S':
                    total += 1
                if tr == 'S' and bl == 'M':
                    total += 1
            if tl == 'S' and br == 'M':
                if tr == 'M' and bl == 'S':
                    total += 1
                if tr == 'S' and bl == 'M':
                    total += 1

print(total)
