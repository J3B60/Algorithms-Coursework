################
###Input List###
################

A = [2,3,4,3,2,3]

################

n = len(A)
swapped = False
i = 1
NaNCounter = 0
while n !=0:
    swapped = False
    while i < n:
        if A[i-1] > A[i]:
            A[i], A[i-1] = A[i-1], A[i]
            swapped = True
            print (swapped)
            i = i + 1
print (A)
print ("Number of NaNs: ", NaNCounter)
