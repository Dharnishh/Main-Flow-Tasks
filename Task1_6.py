org_str=input("enter a string:")
str = org_str.replace(" ","").lower()
is_palindrome= str == str[::-1]
print("is the string a palindrome:",is_palindrome)
