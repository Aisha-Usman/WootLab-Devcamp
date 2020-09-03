# a function to determine standard deviation of an array

import math

def variance(a,n):

#finding the mean
    sum = 0
    for i in range (0,n):
        sum += a[i]
    mean = sum /n
#finding the variance which is the sum of squared differences of mean divided
#by number of elements

    sqDiff = 0
    for i in range(0,n):
        sqDiff += ((a[i] - mean) * (a[i] - mean))
    return sqDiff /n

#finding the standard deviation. SD= sqrt(variance)
def StanDev(arr,n):
    return math.sqrt(variance(arr,n))

arr = [50,47,19,240,10]
n= len(arr)

print("Standard Deviation: ", round(StanDev(arr,n), 3))
