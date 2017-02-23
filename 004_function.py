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
