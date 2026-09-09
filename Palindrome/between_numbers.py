# Write a program to print all Palindrome Numbers between the Given Numbers?
a=int(input("Enter Value1 "))
b=int(input("Enter Value2 "))
c=0
if(a<0 or b<0):
    print("InvaliD InputS")
else:
    if(a>b):
        a,b=b,a
    for i in range(a+1,b):
        temp=i
        rev=0
        while(temp>0):
            r=temp%10
            rev=rev*10+r
            temp//=10
        if(rev==i):
            c=c+1
            print(i)
    if(c==0):
        print("No Palindrome Values")
