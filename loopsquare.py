#! /usr/bin/python
import turtle

def draw_square(some_turtle):
	for i in range(4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_rhombus(some_turtle):
	some_turtle.forward(100)
	some_turtle.right(20)
	some_turtle.forward(100)
	some_turtle.right(160)
	some_turtle.forward(100)
	some_turtle.right(20)
	some_turtle.forward(100)
	some_turtle.right(160)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	count = 360 / 5 
	brand = turtle.Turtle()
	for i in range(count):
		brand.right(5)
		brand.color("yellow")
		brand.shape("turtle")
		brand.speed(100)
		draw_rhombus(brand)
	window.exitonclick()

draw_art()
