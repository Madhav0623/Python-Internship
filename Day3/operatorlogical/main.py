n1=10
n2=20
n3=30

if n1>n2 and n1>n3:
    print("n1 is the largest number")

if n2>n1 and n2>n3:
    print("n2 is the largest number")

if n3>n1 and n3>n2:
    print("n3 is the largest number")

ch = input("Enter a character:")\

if (ch=='A' or ch=='a' or ch=='E' or ch=='e' or ch=='I' or ch=='i' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")

else:
    print(ch, "is a consonant")
