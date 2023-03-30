from scoreboard import Scoreboard
from paddles import Paddle
from ball import Ball
import time

scoreboard = Scoreboard()

game_is_on = True
MAX_SCORE = 1

player_paddle = Paddle(pos_x=-360, pos_y=0)
computer_paddle = Paddle(pos_x=360, pos_y=0)
scoreboard.control_paddle(player_paddle)

ball = Ball()

def game_reset():
    ball.reset_ball()
    player_paddle.reset_paddle(pos_x=-360, pos_y=0)
    computer_paddle.reset_paddle(pos_x=360, pos_y=0)

while game_is_on:
    scoreboard.screen_update()
    ball.ball_move()
    time.sleep(.01)

    #move computer paddle
    computer_paddle.computer_play(ball)

    # detect collision with wall, count points and reset game
    if scoreboard.player_score < MAX_SCORE and scoreboard.computer_score < MAX_SCORE:
        if ball.left_wall_collision() is True:
            scoreboard.player_score += 1
            game_reset()

        elif ball.right_wall_collision() is True:
            scoreboard.computer_score += 1
            game_reset()
    else:
        game_is_on = False
        ball.ball_hide()
        scoreboard.final_result()



    #detect collision with paddle
    if (ball.ball.xcor() > 340 and ball.ball.xcor() < 350) and (
            ball.ball.ycor() < computer_paddle.paddle.ycor() + 40 and ball.ball.ycor() > computer_paddle.paddle.ycor() - 40):
        ball.x_speed *= -1

    if (ball.ball.xcor() < -340 and ball.ball.xcor() > -350) and (
            ball.ball.ycor() < player_paddle.paddle.ycor() + 40 and ball.ball.ycor() > player_paddle.paddle.ycor() - 40):
        ball.x_speed *= -1

scoreboard.exitonclick()

# TODO: get rid of white screen before program starts to work