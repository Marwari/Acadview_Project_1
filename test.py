num=int(raw_input("Enter num to convert in hexadecimal: "))
i=0
while(num>0):
    if num<10:
        print(num)
    elif num==10:
        print("A")
    elif num==11:
        print "B"
    elif num==12:
        print "C"
    elif num==13:
        print "D"
    elif num==14:
        print "E"
    elif num==15:
        print "F"
    else:
        print "I don't know."