import turtle
import math

#Simple for loop
for i in range(4):
    print(i)

#Drawing square using for loop and turtle

bob = turtle.Turtle()
"""
for i in range(4):
    bob.fd(100)
    bob.lt(90)
"""
#Drawing square function
def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(bob,100)

#Polygon
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(n/n)

#polygon(bob,50,5)

#Circle
def circle(t,r):
    cf = 2*math.pi*r
    length = cf/360
    polygon(t,length,360)

#circle(bob,50)

#Arc
def arc(t,r,angle):
    cf = 2*math.pi*r
    length = cf/360
    polygon(t,length,angle)

arc(bob,50,90)
