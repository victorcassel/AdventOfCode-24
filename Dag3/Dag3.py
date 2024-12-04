import re

with open('Dag3\inp.txt', 'r') as file: 
    lines = file.readlines()

print (lines[:10])
sum = 0
for i in range(len(lines)):    
    m = re.findall('mul\((\d+),(\d+)\)', lines[i])
    for j in range(len(m)):
        sum += int(m[j][0]) * int(m[j][1])

print("sum", sum)

sum2 = 0
for i in range(len(lines)):    
    stripped = ""
    dos = True
    pattern = ""
    pos = 0
    while True:
        if dos:
            pattern = "don't\(\)"
        else:
            pattern = "do\(\)"

        # start searching at position pos
        s = lines[i][pos:]
        m = re.search(pattern, s)
        
        t = 1

