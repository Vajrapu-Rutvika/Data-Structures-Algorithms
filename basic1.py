#1
print("Lets start the challenge i will be consistant")
#2
name=input("Enter your name: ")
print(name,"welcome to the challenge")
#3
num1=int(input("enter first number: "))
num2=int(input("enter second number:"))
sum=num1+num2
print("the sum of",num1,"and",num2,"is",sum)
#4
num3=float(input("enter first number: "))
num4=float(input("enter second number: "))
reminder=num3%num4
print("the reminder of",num3,"and",num4,"is",reminder)
#6
num5=int(input("enter first number: "))
num6=int(input("enter second number:"))
num5,num6=num6,num5
print("the value of first number is",num5)
print("the value of second number is",num6)
#7
sub1=int(input("enter marks for subject1: "))
sub2=int(input("enter marks for subject2: "))
sub3=int(input("enter marks for subject3: "))
sub4=int(input("enter marks for subject4: "))
sub5=int(input("enter marks for subject5: "))
total_marks=sub1+sub2+sub3+sub4+sub5
percentage=(total_marks/500)*100
print("total marks:",total_marks)
print("percentage:",percentage)
#8
temparature=float(input("enter temparature in celsius: "))
fahrenheit=(temparature*9/5)+32
print("temparatur in fahrenheit is: ",fahrenheit)
#9
temparature=float(input("enter temparature in fahrenheit: "))
celsius=(temparature-32)*5/9
print("temparature in celsius is: ",celsius)
#10
length=float(input("enter length in meters"))
breadth=float(input("enter breadth in meters"))
height=float(input("enter height in meters"))
volume=length*breadth*height
print("volume of the cuboid is: ",volume)
