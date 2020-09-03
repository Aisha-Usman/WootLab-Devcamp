#This function counts the number of 3's in an array

def count_3(n):
    count = 0
    while (n>0):
        if (n % 10 == 3):
            count = count + 1
        n = int(n/10)
        return count

def count_range(n):
    count = 0
    for i in range(2,n):
        count = count + count_3(i);
    return count

num = int(input("Enter number:"))
print(count_range(num))



