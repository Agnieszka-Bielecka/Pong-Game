from turtle import Turtle

WIDTH = 400
HEIGHT = 300

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_speed = 3
        self.y_speed = 3
        self.wall_coll = False

    def create_ball(self):
        ball = Turtle()
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.turtlesize(stretch_wid=.8, stretch_len=.8)
        self.ball = ball

    def wall_collision(self):
        # if self.ball.xcor() < -WIDTH or self.ball.xcor() > WIDTH:
        #     self.wall_coll = True
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

            # for i in range(300):
            #     self.ball.backward(.01)

    # def wall_collistion(self):
    #     if self.ball.xcor() < -WIDTH or self.ball.xcor() > WIDTH or self.ball.ycor() < -HIGHT or self.ball.ycor() > HIGHT:
    #         return True

    # self.x_speed = -self.x_speed