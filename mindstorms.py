#! /bin/usr/python

import turtle

def draw_square(some_turtle):	
	for i in range(4):
		some_turtle.forward(100)
		some_turtle.right(90)
	
def main():
	window = turtle.Screen()
	window.bgcolor("red")
	brand = turtle.Turtle()
	brand.shape("turtle")
	brand.color("green")
	brand.speed(2)
	brand.shapesize(2)
	draw_square(brand)	
	angie = turtle.Turtle()
	angie.circle(100)
	angie.shape("arrow")
	angie.color("blue")

	window.exitonclick()

main()
