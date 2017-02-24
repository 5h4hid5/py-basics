import math
import sys

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
