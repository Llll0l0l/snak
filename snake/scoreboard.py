from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.current_score = 0
        self.score_update()

    
    def score_update(self):
        self.clear()
        self.write(f"Score: {self.current_score}", align="center", move=False, font=('Courier', 18, 'normal'))
        self.current_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", move=False, font=('Courier', 20, 'normal'))
