# Write a program to check Given Number is Palindrome or Not.
n=int(input("Enter Number "))
temp=n
if(n<=0):
    print("InvAlid Input")
else:
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(rev==temp):
        print("Palindrome")
    else:
        print("Not a Palindrome")
