from turtle import *
t=Turtle()
t.shape("turtle")
t.color("Sea Green")

color('red', 'yellow')
begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
