#1
number=int(input("enter a number: "))
if number>0:
    print(number," is positive")
else:
    print(number," is negative")
#2
if number%5==0:
    print(number," is divisible by 5")
else:
    print(number," is not divisible by 5")
#3
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial:", fact)
#4
n = int(input("Enter terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
#5
num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is Not Prime")
#6
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed Number:", rev)
          
        