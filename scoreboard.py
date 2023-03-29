from turtle import Turtle, Screen

PLAYERS = [None, None]
POSITIONS = [(-50, 230), (50, 230)]

class Scoreboard():
    def __init__(self):
        #points
        self.player_score = 0
        self.computer_score = 0
        self.all_points = [self.player_score, self.computer_score]
        self.count_points()


        #game board
        scoreboard = Screen()
        scoreboard.colormode(255)
        scoreboard.tracer(0)
        scoreboard.setup(width=800, height=600)
        scoreboard.bgcolor("black")
        scoreboard.title("Pong")
        self.scoreboard = scoreboard

        #the line between players boards
        line = Turtle()
        line.setpos(0, 300)
        line.setheading(270)
        line.color("white")
        line.hideturtle()
        for i in range(20):
            line.pendown()
            line.forward(15)
            line.penup()
            line.forward(15)

    #display points on scoreboard
    def count_points(self):
        #create player score
        for i in range(2):
            PLAYERS[i] = Turtle()
            PLAYERS[i].color("white")
            PLAYERS[i].penup()
            PLAYERS[i].hideturtle()
            PLAYERS[i].setpos(POSITIONS[i])
            PLAYERS[i].write(self.all_points[i], align="center", font=("Consolas", 40, "normal"))

    def update_points(self):
        for i in range(2):
            PLAYERS[i].clear()
            PLAYERS[i].write(self.all_points[i], align="center", font=("Consolas", 40, "normal"))



    def screen_update(self):
        if self.player_score != self.all_points[0] or self.computer_score != self.all_points[1]:
            self.all_points = [self.player_score, self.computer_score]
            self.update_points()
        return self.scoreboard.update()

    def exitonclick(self):
        return self.scoreboard.exitonclick()

    def control_paddle(self, player_paddle):
        self.scoreboard.listen()
        self.scoreboard.onkeypress(key="Up", fun=player_paddle.move_up)
        self.scoreboard.onkeypress(key="Down", fun=player_paddle.move_down)
