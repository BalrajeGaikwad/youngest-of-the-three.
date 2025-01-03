#f) If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three.

a=int(input ("Enter the age of Ram :- "))
b=int(input ("Enter the age of Shyam :- "))
c=int(input ("Enter the age of Ajay :- "))

if(a>b and a>c):
    print(" Ram is youngest")
elif(b>a and b>c):
    print(" Shyam is youngest")
else:
    print("Ajay is youngest")