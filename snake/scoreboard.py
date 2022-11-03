from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.current_score = 0
        self.high_score = self.get_highest_score()
        self.score_update()


    def get_highest_score(self):
        with open("high_score.txt", "r") as f:
            highest = int(f.read())
            return highest


    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score

            # open file
            with open("high_score.txt", "w") as highest_score:
                highest_score.write(str(self.high_score))
        
        self.current_score = 0
        self.score_update()
    
    def score_update(self):
        self.clear()
        self.write(f"Score: {self.current_score}  High Score: {self.high_score}", align="center", move=False, font=('Courier', 18, 'normal'))
        

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", move=False, font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.current_score += 1
        self.score_update()
