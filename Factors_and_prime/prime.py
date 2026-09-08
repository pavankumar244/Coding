# Write a program to check if the given number is a prime number or not
a=int(input("Enter a Number"))
if(a<=0):
    print("Invalid Input")
else:
    c=0
    for i in range(1,a+1):
        if(a%i==0):
            c=c+1
    if(c==2):
        print("Prime Number")
    else:
        print("Not a Prime Number")
            