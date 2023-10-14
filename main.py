# from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
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

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_num in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_num)

# colors = ['blue', 'red', 'green', 'purple', 'orange', 'yellow']

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


#
# directions = [0, 90, 180, 270]
# tim.speed("slow")
# tim.pensize(10)
# for _ in range(100):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)
screen = t.Screen()
screen.exitonclick()
