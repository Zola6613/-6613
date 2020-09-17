import turtle
colors = ["red","yellow","blue","green","orange","purple"]
t = turtle.Pen()
turtle.bgcolor("black")
for i in range(300):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(61)
