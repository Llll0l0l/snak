import time
from turtle import Screen
from scoreboard import Score
from snake import Snake
from food import Food


def game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()



    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # collision detection with food
        if snake.segments[0].distance(food) < 15:
            food.random_locate()
            snake.add_turtle()
            score.score_update()

        
        # detect collision with wall
        if snake.segments[0].xcor()>=300 or snake.segments[0].xcor()<=-300 or snake.segments[0].ycor()>=300 or snake.segments[0].ycor()<=-300:
            game_is_on = False
            score.game_over()

        

        # detect collision with itself
        for s in snake.segments[1:]:
            
            if snake.segments[0].distance(s)<=10:
                game_is_on = False
                score.game_over()

            

    screen.exitonclick()



if __name__ == "__main__":
    game()