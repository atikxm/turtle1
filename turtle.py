import turtle
turtle.Screen().bgcolor('black')
t=turtle.Turtle()
t.speed(0)
t.hideturtle()

for i in range(1000):
    t.color('red')
    t.circle(i)
    t.color('green')
    t.circle(i*0.6)
    t.right(3)
    t.forward(3)
turtle.done()