from turtle import Turtle
import random

list_of_colors = ["#5d8aa8", "#e32636", "#9966cc", "#a4c639", "#6e7f80"]
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVING_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(list_of_colors))
            random_y_pos = random.randint(-250, 250)
            new_car.goto(300, random_y_pos)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
