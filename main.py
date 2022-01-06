from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

is_game_on = True
i = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    carManager.create_car()
    carManager.move()

    if player.ycor() >= 290:
        player.reset()
        score_board.level_up()
        carManager.level_up()

    for car in carManager.all_cars:
        if player.distance(car) <= 30:
            is_game_on = False
            score_board.game_over()


screen.exitonclick()
