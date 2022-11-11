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

#cube()
#mul()
#sumsquare()
readsum()
