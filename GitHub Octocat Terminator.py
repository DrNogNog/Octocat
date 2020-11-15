# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:11:24 2020

@author: Gordo
"""

import turtle
import math

def talloval(r):               # Verticle Oval
    turtle.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        turtle.circle(r,90)    # Long curved part
        turtle.circle(r/2,90)  # Short curved part

def flatoval(r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
def round_rectangle(center_x,center_y,width,height,cornersize):
    cursor = turtle.Turtle() # Cursor
    cursor.shape("turtle")
    cursor.color("white")
    cursor.speed(3)
    cursor.pensize(10)
    cursor.up()
    cursor.goto(center_x-width/2+cornersize,center_y-height/2)
    cursor.down()
    for _ in range(2):
        cursor.fd(width-2*cornersize)
        cursor.circle(cornersize,90)
        cursor.fd(height-2*cornersize)
        cursor.circle(cornersize,90)
    cursor.up()

def movePen(cursor, x, y):
    cursor.penup()
    cursor.setposition(x, y)
    cursor.pendown()

def movePenX(cursor, x):
    cursor.penup()
    cursor.setx(x)
    cursor.pendown()

def movePenY(cursor, y):
    cursor.penup()
    cursor.sety(y)
    cursor.pendown()

def positionAlongCircle(x, y, radius, angle):
    radians = math.radians(angle)
    return [x + (radius*math.sin(radians)),
            y + (radius*math.cos(radians))]

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("gray")

    cursor = turtle.Turtle() # Cursor
    cursor.shape("turtle")
    cursor.color("white")
    cursor.speed(3)
    cursor.pensize(10)

    # Draw the head

    movePenY(cursor, -150)
    round_rectangle(0,0,600,420,200)
    
    # Draw inner Head
    
    round_rectangle(0,-40,460,280,100)
    
    # Draw the nose
    
    noseMouthOffset = -20

    movePenY(cursor, -90 + noseMouthOffset)
    cursor.circle(20)

    # Draw the mouth

    movePenY(cursor, -120)
    movePenX(cursor, 30)         
    cursor.setheading(270) 
    cursor.circle(-30,180)
    
    # Draw the eyes
    # Right eye
    cursor.setheading(270) 
    movePenY(cursor, -60)
    movePenX(cursor, 120)  
    cursor.left(45)
    
    for loop in range(2):      # Draws 2 halves of ellipse
        cursor.circle(20,90)    # Long curved part
        cursor.circle(100/2,90)  # Short curved part
    #Bigger Right Eye
    cursor.setheading(270) 
    movePenY(cursor, -100)
    movePenX(cursor, 110)  
    cursor.left(45)
    
    for loop in range(2):      # Draws 2 halves of ellipse
        cursor.circle(40,90)    # Long curved part
        cursor.circle(200/2,90)
        
    # Left eye
    cursor.setheading(270)
    movePenY(cursor, -60)
    movePenX(cursor, -140) 
    cursor.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        cursor.circle(20,90)    # Long curved part
        cursor.circle(100/2,90)  # Short curved part
        
    #Bigger Left eye
    
    cursor.setheading(270)
    movePenY(cursor, -100)
    movePenX(cursor, -160) 
    cursor.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        cursor.circle(40,90)    # Long curved part
        cursor.circle(100,90)  # Short
    
    # # Draw the ears

    # # Right ear
    
    earBeginAngle = 20
    earSize = 85
    earWidth = 22
    positionA = positionAlongCircle(140, 55, 150, earBeginAngle)
    movePen(cursor, positionA[0], positionA[1])

    positionB = positionAlongCircle(140, 55, 150 + earSize, earBeginAngle + earWidth)
    cursor.setposition(positionB[0], positionB[1])

    positionC = positionAlongCircle(140, 55, 150, earBeginAngle + earWidth * 2)
    cursor.setposition(positionC[0], positionC[1])

    # # Left ear

    positionA = positionAlongCircle(-140, 55, 150, -earBeginAngle)
    movePen(cursor, positionA[0], positionA[1])

    positionB = positionAlongCircle(-140, 55, 150 + earSize, -earBeginAngle + -earWidth)
    cursor.setposition(positionB[0], positionB[1])

    positionC = positionAlongCircle(-140, 55, 150, -earBeginAngle + -earWidth * 2)
    cursor.setposition(positionC[0], positionC[1])

    # Whiskers

    whiskerLength = 200

    # Right whiskers

    movePen(cursor, 270, -15)
    cursor.setheading(-15)
    cursor.forward(whiskerLength)

    movePen(cursor, 270, 15)
    cursor.left(30)
    cursor.forward(whiskerLength)

    # Left whiskers

    movePen(cursor, -270, -15)
    cursor.setheading(180+15)
    cursor.forward(whiskerLength)

    movePen(cursor, -270, 15)
    cursor.left(-30)
    cursor.forward(whiskerLength)

    window.exitonclick()


draw_shape()