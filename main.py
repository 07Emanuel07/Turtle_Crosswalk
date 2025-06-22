# Emanuel Biruk Seifegebreal - 2024 --> This project is for learning purposes

from turtle import Screen
from user import User
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = User()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user.user_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()
    # Detect Collision with Car
    for car in cars.all_cars:
        if car.distance(user) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Finish Line
    if user.is_at_finish_line():
        user.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

screen.exitonclick()
