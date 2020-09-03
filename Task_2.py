#This fuction accepts a positive integer and determines if it is a prime number.

def main():
    num = int(input("enter a number a:"))
#prime numbers are numbers greater than 1
    if (num <= 1):
        print("False")
    elif (num ==2):
        print ("True")
    else:
#prime numbers are divisible by themselves and 1 only
        for x in range(2, num):
            if (num % x ==0):
                print("False")
                break

            else:
                print("True")
                break
    
main()
