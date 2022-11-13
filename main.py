## Day 1

##1
def cube():
    num1 = int(input())
    for i in range(num1+1):
        print(f" {i} * {i} * {i} =  {i**3}")
##2
def mul():
    num2 = int(input())
    for u in range(1, 11):
        print(f"{num2} * {u} = {u * num2}")
##3
def sumsquare():
    num3 = int(input())
    sum = 0
    for h in range(1, num3+1):
        sum += (h*h)
    print(sum)

##4
def readsum():
    sum = 0
    for y in range(10):
        y = int(input())
        sum += y
    print(sum)

##5
def fact():
    num4 = int(input())
    if num4 == 0:
        print(1)
    else:
        fact1 = 1
        for i in range(1, num4+1):
            fact1 *= i
        print(fact1)

##6
def reverse():
    num5 = int(input())
    n = 0
    while (num5 > 0):
        rem = num5 % 10
        n = (n * 10) + rem
        num5 = num5 // 10
    print(n)

##7
def palindrome():
    num6 = int(input())
    x = num6
    n = 0
    while (num6 > 0):
        rem = num6 % 10
        n = (n * 10) + rem
        num6 = num6 // 10
    if (n == x):
        print("Palindrome")
    else:
        print("Not Palindrome")

##8
def sumOfDigits():
    n = 0
    num7 = int(input())
    y = num7
    while (num7 > 0):
        u = num7 % 10
        n = n + u
        num7 //= 10
    print(n)

##9
def totalDigits():
    num8 = int(input())
    count = 0
    while (num8 > 0):
        num8 //= 10
        count += 1
    print(count)

##10
def zeroesAndOnes():
    num9 = input()
    x = ''
    for i in num9:
        if (i == '0'):
            x += '1'
        else:
            x += '0'
    print(x)


# cube()
# mul()
# sumsquare()
# readsum()
# fact()
# reverse()
# palindrome()
# sumOfDigits()
# totalDigits()
# zeroesAndOnes()

