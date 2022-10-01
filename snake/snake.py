from turtle import Turtle
import turtle


MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()




    def add_turtle(self):
        turt = self.segments[len(self.segments)-1]
        x = turt.xcor() - 20
        y = turt.ycor() - 20
        new_turt = Turtle(shape='square')
        new_turt.penup()
        new_turt.color('white')
        new_turt.setx(x)
        self.segments.append(new_turt)
        
    
    def up(self):
        c_h = self.segments[0].heading()
        if c_h != 270 and c_h != 90:
            self.segments[0].setheading(90)

    def down(self):
        c_h = self.segments[0].heading()
        if c_h != 270 and c_h != 90:
            self.segments[0].setheading(270)
        
    def right(self):
        c_h = self.segments[0].heading()
        if c_h != 180 and c_h != 0:
            self.segments[0].setheading(0)

    def left(self):
        c_h = self.segments[0].heading()
        if c_h != 0 and c_h != 180:
            self.segments[0].setheading(180)
        


    

    def create_snake(self):

        turt = Turtle(shape='square')
        turt.color('white')
        turt.penup()
        self.segments.append(turt)
        self.add_turtle()
        self.add_turtle()


    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        self.segments[0].forward(MOVE_DISTANCE)


