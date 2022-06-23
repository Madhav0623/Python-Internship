year = int(input("Enter the year : "))

if (year % 400 == 0) and (year % 100 == 0 ) :
    print("{0} is a leap Year".format(year))

elif (year % 4 == 0) and (year % 100 != 0 ) :
    print("{0} is a leap Year".format(year))

else:
    print("{0} is not a leap Year".format(year))