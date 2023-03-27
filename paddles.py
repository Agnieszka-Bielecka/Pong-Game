from turtle import Turtle

class Paddle:
    def __init__(self):
        self.paddle_parts = []
        self.positions = [(-380, 0), (-380, -20), (-380, -40)]
        self.create_paddle()

    def create_paddle(self):
        for part in range(3):
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.penup()
            paddle.goto(self.positions[part])
            self.paddle_parts.append(paddle)

    def move_up(self):
        y = self.paddle_parts[0].ycor()
        if y < 280:
            for part in self.paddle_parts:
                part.sety(part.ycor() + 20)

    def move_down(self):
        y = self.paddle_parts[-1].ycor()
        if y - 280:
            for part in self.paddle_parts:
                part.sety(part.ycor() - 20)
