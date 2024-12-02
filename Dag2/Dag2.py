import numpy as np 
import string

# jagged = np.loadtxt('Dag2\inp.txt') 
# Reading the data into an array 
with open('Dag2\inp.txt', 'r') as file: 
    lines = file.readlines()

print (lines[:10])
safeCount = 0

for i in range(len(lines)):
    lst = [int(ele) for ele in lines[i].split()]

    print(lst)

    allIncreasing = True
    allDecreasing = True
    okDistance = True
    for j in range(len(lst) -1):
        dist = abs(lst[j] - lst[j+1])
        print (dist)
        okDistance = okDistance and dist > 0 and dist < 4
        allIncreasing = allIncreasing and (lst[j] < lst[j+1])
        allDecreasing = allDecreasing and (lst[j] > lst[j+1])

    if okDistance and (allIncreasing or allDecreasing):
        safeCount += 1

print ("safecount", safeCount)
 