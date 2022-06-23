num1 = int(input("Enter Value of Number1 (num1):"))
num2 = int(input("Enter Value of Number2 (num2):"))

temp=num1
num1=num2
num2=temp

print("The Value of num1 after swapping is : {}".format(num1))
print("The Value of num2 after swapping is : {}".format(num2))