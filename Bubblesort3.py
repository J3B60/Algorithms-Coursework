import random as rd
import time
import datetime
import matplotlib.pyplot as plt
#/ Bubble Sort /#

x = []
y = []

#///////////////#
def Bubblesort(A):
    global x
    global y
    print ("Input Array: ", A)
    n = len(A)  #Number of elements remaining
    swapped = False
    i = 1       #Element in Array
    NoNaN = 0   #Number of NaNs
    R = A      #Result Array
    NumLoop = 1   #Number of loops
    print(n)
    print(datetime.datetime.now())
    start_time = time.time()
    while (n > 0):
        swapped = False
        while i < n:
            print (NumLoop)
            NumLoop += 1
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
    ExeTime = time.time() - start_time
    print("Execution: --- %s seconds ---" % (ExeTime))
    print(datetime.datetime.now())
    x = x + n
    y = y + ExeTime

A = [1.32,-float('inf'),3.25,float('inf'),0.22,6.32,-float(0),5.1,0,0.94,float('inf'),7,2,float('nan')]
Bubblesort(A)
A = []
Bubblesort(A)
A = [4]
Bubblesort(A)
A = [45, 32]
Bubblesort(A)
A = [4, 2, 9, 7, 1, 5, 3, 8, 6, 10]
Bubblesort(A)
A = [5,4,6,7,8,5,5,3,2,1,5,9,7]
Bubblesort(A)
A = [float('inf'), 4, 6, 7, -float('inf'), 8, 5,5, 3,2, 1, 5, 9, 7]
Bubblesort(A)
A = [-float(0), 5, float(0), 3, float(2), float(0), 6, float(1), float(4), -float(0), 7, 0]
Bubblesort(A)
A = [6,2,float('nan'),5,3,float('nan'),1,7,4,float('nan')]
Bubblesort(A)
A = [rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000),rd.uniform(-1000,1000)]
Bubblesort(A)
A = [3.432, 4.12, 43.2, 4.0, 3.5342, 432, 543.4324, 324.56, 7.324]
Bubblesort(A)
A = [0, 1, False, True, True, False, False, True, 4, 1, 0, 3, -1, 2]
Bubblesort(A)
A = ['a','z','g','b','w']
Bubblesort(A)
A = ['/','a','z','g','$','!','A','b','w','D','^','|']
Bubblesort(A)
A = ['P/\R', 'abc', 'Qfc', 'agf', 'g', '$DATA']
Bubblesort(A)
A = [31.312, 3422.23, 123.123, 123.43, 534, 4235464, 23564, 4234, 342, 3465464]
Bubblesort(A)
A = ['q', 'w', 'd', 'e', 's', 'a', 'e', 'g', 'a']
Bubblesort(A)
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Bubblesort(A)
A = [1.32, -float('inf'), 3.25, float('inf'), 0.22, 6.32, -0.0, 5.1, 0, 0.94, float('inf'), 7, 2, float('nan')]
Bubblesort(A)
plt.plot(x, y)
plt.ylable('Number of Elements')
plt.xlable('Execute Time')
plt.title('Bubble Sort Test Results')
plt.show()
