def Addition(n1,n2):
    n3=n1+n2
    return n3
def Substract(n1,n2):
    n3=n1-n2
    return n3
def Divide(n1,n2):
    n3=n1/n2
    return n3
def Multiplication(n1,n2):
    n3=n1*n2
    return n3
print("\n=======================================\n")
print("Choose a mathametical operation\n")
print(" 1. Addition")
print(" 2. Substract")    
print(" 3. Divide")
print(" 4. Multiplication\n")
Choice=int(input("Enter your choice (1  to 4 ) :"))
if Choice ==1:
    n1=int(input("Enter the number too add : "))
    n2=int(input("Enter the another number : "))
    n3=Addition(n1,n2)
    print(f"The addition of two number is : {n3}")
elif Choice ==2:
    n1=int(input("Enter the number too Substract : "))
    n2=int(input("Enter the another number : "))
    n3=Substract(n1,n2)
    print(f"The substract of two number is : {n3}")
elif Choice ==3:
    n1=int(input("Enter the number too Divide : "))
    n2=int(input("Enter the another number : "))
    n3=Divide(n1,n2)
    print(f"The divide of two number is : {n3}")
elif Choice ==4:
    n1=int(input("Enter the number too Multiplication : "))
    n2=int(input("Enter the another number : "))
    n3=Multiplication(n1,n2)
    print(f"The multiplication of two number is : {n3}")
else:
    print("Wrong choice ")
