import re

def ComputeSum(s):
    sum = 0
    m = re.findall('mul\((\d+),(\d+)\)', s)
    for j in range(len(m)):
        sum += int(m[j][0]) * int(m[j][1])
    
    return sum

with open('Dag3\\inp.txt', 'r') as file: 
    lines = file.readlines()
# concatenate all lines to one
all = ''.join(lines)
print (all[:5])
print (all[2:5])
# all = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
exit
#part1
sum = ComputeSum(all)
print("Part1: sum", sum)

# part 2
sum2 = 0
keep = True

adjusted = ""
pattern = ""
pos = 0
done = False
while not done:
    if keep:
        pattern = "don't()" # search for next Stop 
    else:
        pattern = "do()" # search for next Start 

    # start searching at position pos
    m = re.search(pattern, all[pos:])
    if m == None:
        # found nothing, we are done, we are at the end now
        if keep:
            adjusted += all[pos:]
        done = True
    else:
        # found something, keep on looping, possibly append, and make the switch
        x = m.span()        
        nextPos = x[1] + pos      
        if keep:
            adjusted += all[pos: nextPos]
            keep = False 
        else:
            keep = True 

        pos = nextPos

part2sum = ComputeSum(adjusted)
print (all[:2000])
print (adjusted[:2000])
print ("Part 2: part2sum", part2sum)