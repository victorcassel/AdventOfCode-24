import re

# TODO
with open('Dag3\inp.txt', 'r') as file: 
    lines = file.readlines()

print (lines[:10])
sum = 0
for i in range(len(lines)):    
    m = re.findall('mul\((\d+),(\d+)\)', lines[i])
    for j in range(len(m)):
        sum += int(m[j][0]) * int(m[j][1])

print("sum", sum)
#     for skip in [-1] + list(range(len(lst))):
#         lst2 = lst.copy()
#         if skip > -1:            
#             lst2.pop(skip)
        
#         print(lst2)

#         allIncreasing = True
#         allDecreasing = True
#         okDistance = True
#         for j in range(len(lst2) -1):
#             dist = abs(lst2[j] - lst2[j+1])
#             okDistance = okDistance and dist > 0 and dist < 4
#             allIncreasing = allIncreasing and (lst2[j] < lst2[j+1])
#             allDecreasing = allDecreasing and (lst2[j] > lst2[j+1])

#         if okDistance and (allIncreasing or allDecreasing):
#             safeCount2 += 1
#             if skip == -1:
#                 safeCount += 1
#             break

# print ("safecount", safeCount)
# print ("safecount2", safeCount2)
 