import math

def printRhyme():
    print('I eat rice,')
    print('Python is nice')

#Calling function
printRhyme()
print('\n')

#Function inside another function
def repeatRhyme():
    printRhyme()
    printRhyme()

repeatRhyme()
print('\n')

#Function with parameters
def printArea(radius):
    area = math.pi * radius**2
    print('Area: ' + str(area))

printArea(5)
print('\n')

#Function with return statement
def rightJustify(s):
    l = len(s)
    res = ''
    while l < 70:
        res = res + ' '
        l = l + 1
    res = res + s
    return res

print('Right Justify: ')
print(rightJustify('monty'))
print(rightJustify('shahid'))
print(rightJustify('bangladesh'))
print('\n')

#Function as arguments
def calculate(f,a,b):
    return f(a,b)

def addNum(x,y):
    return x+y

def multiplyNum(x,y):
    return x*y

print(calculate(addNum,4,5))
print(calculate(multiplyNum,4,5))
print('\n')

#Print grids
def doTwice(f):
    f()
    f()

def doThrice(f):
    f()
    f()
    f()

def doFourTimes(f):
    f()
    f()
    f()
    f()

def printColTop():
    print('+----',end='')

def printRowTop():
    doThrice(printColTop)
    print('+')

def printColPart():
    print('|    ', end='')

def printAllCols():
    doThrice(printColPart)
    print('|')

def printRow():
    printRowTop()
    doTwice(printAllCols)
    doTwice(printAllCols)

doThrice(printRow)
printRowTop()
