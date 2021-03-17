import threading
import sys

#################
###Input Array###
#################

Array = [float('nan')]

#################

ArrayC = Array
x = 0 #Array position
y = 1 #Y always = x+1
Unsorted = len(ArrayC)#Number of unsorted items
Reserved = []
MAXArray = []
MINArray = []
NaNArray = []


while (Unsorted != 0):
    if (ArrayC[x] != ArrayC[x] || ArrayC[y] != ArrayC[y]):
        NaNArray.Append(ArrayC[x])
        del ArrayC[x]
    elif (len(ArrayC)%2 != 0):
        Reserved.append(ArrayC[len(ArrayC)-1])
        del ArrayC[len(ArrayC)-1]
        print ('Array Odd Length, Last Item Reserved')
    else:
        while (y != len(Array) -1):
            if (ArrayC[x] > ArrayC[y]):
                MAXArray.append(ArrayC[x])
                MINArray.append(ArrayC[y])
            else:
                MINArray.append(ArrayC[x])
                MAXArray.append(ArrayC[y])
print ('Input Array:', Array)
print ('Output', ArrayC)
print ('NaNs', NaNArray)
