myString = input("your input: ")
reverseString = reversed (myString)
if list(myString) == list(reverseString):
    print ("this is a palindrome")
else:
    print("this isn't a palindrome") 