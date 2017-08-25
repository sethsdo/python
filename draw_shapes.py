import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_angle):
    for i in range(1,5):
        some_angle.forward(300)
        some_angle.right(115)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    lose = turtle.Turtle()
    lose.shape("turtle")
    lose.color("yellow")
    lose.speed(10)
    for i in range(1,37):
    	draw_square(lose)
    	lose.right(10)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.speed(10)
    for i in range(1,37):
        angie.circle(100)
        angie.right(10)

    kit = turtle.Turtle()
    kit.shape("arrow")
    kit.color("green")
    kit.speed(10)
    for i in range(1,37):
       draw_triangle(kit)
       kit.right(10)


    #window.exitonclick()


      
draw_art()

