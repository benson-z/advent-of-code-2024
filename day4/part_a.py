import re

mat=[]

with open("input.txt") as f:
    for l in f:
        mat.append(list(l)[:-1])

def to_vert(mat):
    out = []
    for a in mat:
        o = ""
        for b in a:
            o += b
        out.append(o)
    return out

def to_horizontal(mat):
    out = []
    for a in range(len(mat[0])):
        o = ""
        for b in range(len(mat)):
            o += mat[b][a]
        out.append(o)
    return out

def to_diagonal(mat, dir='f'):
    rows, cols = len(mat), len(mat[0])
    diagonals = []
    
    if dir == 'f':
        for col in range(cols):
            d = []
            r, c = 0, col
            
            while r < rows and c >= 0:
                d.append(mat[r][c])
                r += 1
                c -= 1
            
            diagonals.append(''.join(d))
        
        for row in range(1, rows):
            d = []
            r, c = row, cols - 1
            
            while r < rows and c >= 0:
                d.append(mat[r][c])
                r += 1
                c -= 1
            
            diagonals.append(''.join(d))
    
    elif dir == 'b':
        for col in range(cols-1, -1, -1):
            d = []
            r, c = 0, col
            
            while r < rows and c < cols:
                d.append(mat[r][c])
                r += 1
                c += 1
            
            diagonals.append(''.join(d))
        
        for row in range(1, rows):
            d = []
            r, c = row, 0
            
            while r < rows and c < cols:
                d.append(mat[r][c])
                r += 1
                c += 1
            
            diagonals.append(''.join(d))
    
    return diagonals

all = to_horizontal(mat) + to_vert(mat) + to_diagonal(mat) + to_diagonal(mat, dir='b')
total = 0
for s in all:
    matches = re.findall(r'XMAS', s)
    matches2 = re.findall(r'SAMX', s)
    total += len(matches) + len(matches2)

print(total)
