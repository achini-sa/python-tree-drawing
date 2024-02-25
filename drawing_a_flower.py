import turtle

def draw_petal():
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)

def draw_flower():
    for _ in range(6):
        draw_petal()
        turtle.left(60)
        
turtle.bgcolor("black")
turtle.speed(5)
turtle.color("red")
draw_flower()
turtle.hideturtle()
turtle.done()
