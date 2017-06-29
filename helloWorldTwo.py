from turtle import*
import math
setup(500,500)

def whileDrawShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.rt(angle)
        drawnSides += 1
def helloYou(name):
    print("Hello",name)

arty = Turtle()
arty.turtlesize(2,2)
arty.pensize(5)
arty.pendown()

another = True
while another == True:
    print("What is your name?")
    name = input()
    helloYou(name)
    print("My name is Arty.")
    print("How was your day?")
    ans = input()
    if (ans == "bad" or "Bad"):
        print("Oh, I'm sorry")
        another = False
    else:
        print("Great!")
    print("Anything you want to talk about?")
    ans = input()
    if (ans == "no" or "No"):
        whileDrawShape(arty,numSides,chosenColor)
        print("Do you want to draw another one?")
        answer = input()
        if (answer == "no"):
            another = False
            print("Ok, talk to you later.")
        if (answer == "yes" or "Yes"):
            arty.penup()
            arty.forward(100)
            arty.pendown()
            break


