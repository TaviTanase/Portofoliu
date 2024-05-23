from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on=True
while game_on:
    screen.update()
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.point()
        scoreboard.update()
        screen.update()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        scoreboard.gameover()

    for segment in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment)<15:
            game_on=False
            scoreboard.gameover()












screen.exitonclick()