def palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
str=input("Enter a string: ")
print(palindrome(str))
#commit cheyyaledachesanu