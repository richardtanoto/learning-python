def palindrome(str):
    return s == s[::-1]
 
 
# Driver code
s = "madam"
ans = palindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")