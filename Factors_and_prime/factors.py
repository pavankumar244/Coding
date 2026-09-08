# Write a program to print all factors of the Given Number

a=int(input("Enter Number "))
if(a<=0):
    print("Invalid Input")
for i in range(1,a+1):
    if(a%i==0):
        print(i,end=" ")