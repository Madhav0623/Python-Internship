a = int(input("Enter a value Bigger Than 100:"))
if(a <= 100):
    if (a % 2 ) == 0:
        print("{0} is Even ".format(a))
    else:
        print("{0} is Odd".format(a))

else:
    print("You Enter Value Bigger Than 100")
