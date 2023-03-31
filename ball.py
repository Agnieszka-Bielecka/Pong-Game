from turtle import Turtle
import random

WIDTH = 400
HEIGHT = 300
SPEED = 3

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_speed = SPEED * random.choice([-1, 1])
        self.y_speed = SPEED * random.uniform(-0.5, 0.5)
        self.speed_multiplier = 1.0
        self.wall_coll = False


    def create_ball(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.turtlesize(stretch_wid=.8, stretch_len=.8)


    def wall_collision(self):
        if self.ball.ycor() < -HEIGHT or self.ball.ycor() > HEIGHT:
            self.y_speed = -self.y_speed


    def left_wall_collision(self):
        if self.ball.xcor() < -WIDTH:
            self.x_speed = -self.x_speed
            return True


    def right_wall_collision(self):
        if self.ball.xcor() > WIDTH:
            self.x_speed = -self.x_speed
            return True


    def increase_speed(self):
        self.speed_multiplier += 0.1


    def ball_move(self):
        self.ball.goto(self.ball.xcor() + self.x_speed * self.speed_multiplier, self.ball.ycor() + self.y_speed * self.speed_multiplier)
        self.wall_collision()


    def reset_ball(self):
        self.x_speed = SPEED
        self.y_speed = SPEED
        self.speed_multiplier += 0.1
        self.ball.setpos(0, 0)
