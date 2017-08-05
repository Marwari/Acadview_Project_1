# print string is palindrome or not

value = raw_input("enter string to check palindrome: ")
rev = str(value)[::-1]
if value == rev:
    print("string is palindrome")
else:
    print("not a palindrome")
