from turtle import Screen
from paddles import Paddle
import time

screen = Screen()
screen.colormode(255)
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

game_is_on = True

paddle = Paddle()

screen.listen()
screen.onkey(key="Up", fun=paddle.move_up)
screen.onkey(key="Down", fun=paddle.move_down)

while game_is_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()