# Function to check if a given string is a palindrome
def isPalindrome(s):
    return s == s[: : -1]

# Input string to be checked for palindrome
s = "GAURI"

# Calling the isPalindrome function and storing the result in 'ans'
ans = isPalindrome(s)

# Checking the result and printing "yes" if it's a palindrome, otherwise "no"
if ans:
    print("yes")
else:
    print("no")