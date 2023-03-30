from turtle import Turtle

WIDTH = 400
HEIGHT = 300
SPEED = 3

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

        # TODO: improve SPEED, after every round ball should be faster
        self.x_speed = SPEED
        self.y_speed = SPEED
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

    def ball_move(self):
        self.ball.goto(self.ball.xcor() + self.x_speed, self.ball.ycor() + self.y_speed)
        self.wall_collision()

    def reset_ball(self):
        self.ball.setpos(0, 0)

# TODO: repair ball_hide
    def ball_hide(self):
        self.ball.setpos(500, 500)

