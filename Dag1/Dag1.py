import numpy as np 

# Text file data converted to integer data type 
a = np.loadtxt('Dag1\inp.txt') 

a1 = sorted(a.copy()[:,0])
a2 = sorted(a.copy()[:,1])
print ("len(a1)", len(a1))
print ("len(a2)", len(a2))
print ("a1", a1[:30])
print ("a2", a2[:30])

totdiff = 0
totdiff2 = 0

for i in range(len(a1)):
    mydiff = abs(a2[i]-a1[i])
    # print (a2[i], a1[i], mydiff)
    totdiff  += mydiff
    totdiff2 += a1[i] * a2.count(a1[i])

print ("totdiff", totdiff)
print ("totdiff2", totdiff2)
 