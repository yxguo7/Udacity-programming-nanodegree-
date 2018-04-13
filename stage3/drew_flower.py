import turtle

def draw_one(some_turtle):

	some_turtle.forward(100)
	some_turtle.right(60)
	some_turtle.forward(100)
	some_turtle.right(120)
	some_turtle.forward(100)
	some_turtle.right(60)
	some_turtle.forward(100)

def draw_flower():
	window = turtle.Screen()
	window.bgcolor('red')

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color('green')
	brad.speed(10)

	for i in range(1,37):
		draw_one(brad)
		brad.right(170)
	
	window.exitonclick ()

draw_flower()
