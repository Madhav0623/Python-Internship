num = int(input("Enter a Number :"))
factorial = 1
if num<0 :
    print("Factorial Does not exist for negative number")

elif num == 0:
    print("The Factorial is 1 ")

else:
    for i in range(1,num + 1):
        factorial = factorial*i
        print("The Factorial of ",num, "is", factorial )