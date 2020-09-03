#This program determins the character with highest occurences in a string.


ASCII_SIZE =256

def MaxOccurChar(str):
#creating array that keeps count of characters.
    #initializing count to zero
    count = [0] * ASCII_SIZE

    max = -1
    a= ''


    for i in str:
        count[ord(i)]+=1;

    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            a= i

    return a

#test

str = "Hello World"
print("The Character with highest occurences is:", MaxOccurChar(str))
