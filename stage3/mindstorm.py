deimport turtle

def draw_sequare(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right (90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    #creat the turtle brad to drew sequare
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color('green')
    brad.speed(10)
    for u in range(1,37):
        draw_sequare(brad)
        brad.right(10)
    #creat tutle angie to drew circle
    '''angie = turtle.Turtle()
    angie.circle(100)
    angie.shape("circle")
    angie.color("blue")
    angie.speed(10)

    ted = turtle.Turtle()
    for j in range(1,4):
        ted.backward(50)
        ted.right(120)  '''
    window.exitonclick()

draw_art()


