import turtle

turtle.shape("turtle")
turtle.left(90)
MIN = 7

def strom(vetev):
    if vetev < MIN: return
    turtle.forward(vetev/3)
    turtle.left(35)
    strom(vetev*2/3)
    turtle.right(35)
    turtle.forward(vetev/6)
    turtle.right(30)
    strom(vetev/2)
    turtle.left(30)
    turtle.forward(vetev/6)
    turtle.left(25)
    strom(vetev/2)
    turtle.right(25)
    turtle.forward(vetev/6)
    turtle.right(20)
    strom(vetev/3)
    turtle.left(35)
    strom(vetev/3)
    turtle.right(15)
    turtle.backward(vetev*5/6)

turtle.tracer(4)
strom(200)

turtle.goto(200, 60)

turtle.tracer(4)
strom(200)

turtle.goto(-200, -60)

turtle.tracer(4)
strom(200)

turtle.exitonclick()