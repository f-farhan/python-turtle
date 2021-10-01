# Importing the module
import turtle
# initalizing turtle

t = turtle.Turtle()

radius = int(input("Enter radius of circle :") )#declaring the unit of radius
t.color("red")
t.begin_fill()
t.circle(radius) #calling the circle(built-in) method
t.end_fill()
time.sleep(5)
