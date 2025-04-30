def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("Enter 1 for addition, 2 for subraction, 3 for multiplication, 4 for division")
c=(input("Enter your choice: "))
n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))

if c=="1":
    print("Sum of",n1,"and",n2,"= ",add(n1,n2))

elif c=="2":
    print("Subtraction of",n1,"and",n2,"= ",sub(n1,n2))

elif c=="3":
    print("Multiplication of",n1,"and",n2,"= ",mul(n1,n2))

elif c=="4":
    print("Division of",n1,"and",n2,"= ",div(n1,n2))

else:
    print("Invalid choice")