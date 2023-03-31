from turtle import Turtle, Screen

PLAYERS = [None, None]
PLAYERS_NAME = ["Player", "Computer"]
POSITIONS = [(50, 230), (-50, 230)]
ALIGNMENT = "center"
FONT = ("Consolas", 40, "normal")

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
        self.line = Turtle()
        self.line.setpos(0, 300)
        self.line.setheading(270)
        self.line.color("white")
        self.line.hideturtle()
        for i in range(20):
            self.line.pendown()
            self.line.forward(15)
            self.line.penup()
            self.line.forward(15)

    #display points on scoreboard
    def count_points(self):
        #create player score
        for i in range(2):
            PLAYERS[i] = Turtle()
            PLAYERS[i].color("white")
            PLAYERS[i].penup()
            PLAYERS[i].hideturtle()
            PLAYERS[i].setpos(POSITIONS[i])
            PLAYERS[i].write(self.all_points[i], align=ALIGNMENT, font=FONT)

    def update_points(self):
        for i in range(2):
            PLAYERS[i].clear()
            PLAYERS[i].write(self.all_points[i], align=ALIGNMENT, font=FONT)

    def screen_update(self):
        if self.player_score != self.all_points[0] or self.computer_score != self.all_points[1]:
            self.all_points = [self.player_score, self.computer_score]
            self.update_points()
        return self.scoreboard.update()

    def control_paddle(self, player_paddle):
        self.scoreboard.listen()
        self.scoreboard.onkeypress(key="Up", fun=player_paddle.move_up)
        self.scoreboard.onkeypress(key="Down", fun=player_paddle.move_down)

    def exitonclick(self):
        return self.scoreboard.exitonclick()

    def game_result(self):
        result = Turtle()
        result.color("white")
        result.penup()
        result.hideturtle()
        result.setpos(0, 150)
        if self.player_score > self.computer_score:
            result.write(f"Game over. {PLAYERS_NAME[1]} wins.", align=ALIGNMENT, font=FONT)
        else:
            result.write(f"Game over. {PLAYERS_NAME[0]} wins.", align=ALIGNMENT, font=FONT)

    def final_result(self):
        self.game_result()
        self.line.clear()
        self.line.color("black")
