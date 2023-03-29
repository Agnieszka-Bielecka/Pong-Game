from turtle import Turtle

class Paddle():
    def __init__(self, pos_x, pos_y):
        self.create_paddle(pos_x, pos_y)

    def create_paddle(self, pos_x, pos_y):
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.penup()
        paddle.turtlesize(stretch_wid=4, stretch_len=.8)
        paddle.goto(pos_x, pos_y)
        self.paddle = paddle

    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)

    def computer_play(self, ball):
        if ball.ball.ycor() > self.paddle.ycor():
            self.move_up()
        elif ball.ball.ycor() < self.paddle.ycor():
            self.move_down()

    def reset_paddle(self, pos_x, pos_y):
        self.paddle.goto(pos_x, pos_y)

