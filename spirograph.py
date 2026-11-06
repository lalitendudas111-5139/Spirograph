import turtle
import random

timmy_the_turtle=turtle.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
turtle.speed("fastest")

turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    
    randomcolour=(r,g,b)
    return randomcolour

for angle in range(0,360,2):
    
    turtle.circle(100)
    turtle.setheading(angle)
    turtle.color(random_color())

screen=turtle.Screen()
screen.exitonclick()