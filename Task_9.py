# Funstion that determines if a string is a palindrome
#a palindrome is a word, number or sequence of data that remains the same when it is reversed.

def Palindrome(a):
    return a == a[::-1]
# this reverses the string to determine if it remains the same.

a = "auta"
test = Palindrome(a)

# testing with a string

if test:
    print("Yes")
else:
    print("No")




