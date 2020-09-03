#program to print prime numbers in a given array

#initiating the start and end of the array
a = 5
b = 15

for i in range(a,b):
    for j in range (2,i):
#finding prime numbers which are numbers divisible by 1 and themselves only.
        if (i % j ==0):
            break
    else:
        print(i)




