number=int(input("enter the number:"))
c=number
factorial=1
for i in range(0,number):
    factorial=factorial*number
    number-=1
print("factorial of",c,'is:',factorial)
