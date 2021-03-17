import random as rd
import time
import datetime
#/ Bubble Sort /#

#///////////////#
#/ Input Array /#
#///////////////#

A = [1.32,-float('inf'),3.25,float('inf'),0.22,6.32,-float(0),5.1,0,0.94,float('inf'),7,2,float('nan')]

#///////////////#
print ("Input Array: ", A)
n = len(A)  #Number of elements remaining
swapped = False
i = 1       #Element in Array
NoNaN = 0   #Number of NaNs
R = A      #Result Array
x = 1   #Number of loops
print(n)
print(datetime.datetime.now())
start_time = time.time()
while (n > 0):
    swapped = False
    while i < n:
        print (x)
        x += 1
        if R[i] != R[i]:
            del R[i]
            n -= 1
            NoNaN += 1 
        elif R[i-1] != R[i-1]:
            del R[i-1]
            n -= 1
            NoNaN += 1 
        else:
            if R[i-1] > R[i]:
                R[i], R[i-1] = R[i-1], R[i]
                swapped = True
            else:
                i += 1
    i = 1
    n -= 1
print ("Output Array: ", R)
print ("Number of NaNs: ", NoNaN)
print("Execution: --- %s seconds ---" % (time.time() - start_time))
print(datetime.datetime.now())
