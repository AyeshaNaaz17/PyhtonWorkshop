## Day 2

##1
def squareRoot():
    num1 = int(input('Enter the number: '))
    n = num1
    n= n ** (1/2)
    print(n)

##2
def prime():
    num2 = int(input())
    if num2 == 2:
        print("Prime")
    elif num2 % 2 == 0:
        print("Not Prime")
    else:
        print("Prime")

##3
def primeRange():
    num3 = int(input())
    for i in range(1, num3+1):
        if i == 2:
            print(str(i) + " Prime")
        elif i % 2 == 0:
            print(str(i) + " Not Prime")
        else:
            print(str(i) + " Prime")

##4
def sumSeries1():
    num4 = int(input())
    sum = 0
    for i in range(num4 + 1):
        sum += (i**2)
    print(sum)

##5
def sumSeries2():
    num5 = int(input())
    sum = 0
    for i in range(num5 + 1):
        for j in range(i+1):
            sum = sum + j
            print(sum)

##6
def sumSeries3():
    num6 = int(input())
    sumProduct = 1
    sum = 0
    for i in range(1, num6 + 1):
        for j in range(1, i + 1):
            sumProduct = sumProduct * j
        sum += sumProduct
    print(sum)

##7
def twoPower():
    num7 = int(input())
    num8 = int(input())
    product = 1
    for i in range(1, num8+1):
        product = num7 ** i
    print(product)

##8
def largestSmallestInput():
    n = int(input("Number of time you want to enter the input"))
    a = []
    for i in range(n):
        user = input()
        a.append(user)
        print(a)
    o = max(a)
    b = min(a)
    print(o)
    print(b)

##9
def avgNum():
    b = []
    for i in range(10):
        num9 = int(input())
        b.append(num9)
    print(sum(b)/10)

##10
def BinDec():
    num10 = int(input())
    n = num10
    r = 0
    p = 0
    while (n > 0):
        ld = n % 10
        r += ld * pow(2, p)
        p += 1
        n //= 10
    print(r)

# squareRoot()
# prime()
# primeRange()
# sumSeries1()
# sumSeries2()
# sumSeries3()
# twoPower()
# largestSmallestInput()
# avgNum()
BinDec()