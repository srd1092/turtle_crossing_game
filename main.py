import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_one = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player_one.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive_cars()

    for car in car_manager.all_cars:
        if car.distance(player_one) < 20:
            game_is_on = False
            score.game_over()

    if player_one.crossing_success():
        player_one.go_to_starting_position()
        score.increase_level()
        car_manager.drive_speed_increment()



screen.exitonclick()
