from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(10):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']
for shape_side_num in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_num)

screen = Screen()
screen.exitonclick()
