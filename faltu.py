#print full name in a reverse order

s1 = raw_input("Enter first name ")
s2 = raw_input("Enter last name ")
s3 = " "
li = list(s1) + list(s3) + list(s2)
str = ''.join(list(reversed(li)))
print str