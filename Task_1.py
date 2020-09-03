#This function takes an array of positive integers and calculates the sum of all even
#and odd integers.



def EvenOddSum(a, n):
        even = 0
        odd = 0
#Loop to find even and odd numbers
        for i in range(n):
            if i% 2 == 0:
                even += a[i]

            else:
                odd += a[i]

        print("sum of even numbers:", even)
        print ("sum of odd numbers :", odd)


# examplw eith a given array
a = [10,20,30,40,50,60]
n = len(a)

EvenOddSum(a, n)




