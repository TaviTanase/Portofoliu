from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.goto(x=0,y=280)
        self.hideturtle()
        self.color("white")
        self.write(f"score={self.points}",move=False,align="center",font=("Arial",15,"normal"))
    def update(self):
        self.points=self.points+1
        self.clear()
        self.write(f"score={self.points}", move=False, align="center", font=("Arial", 15, "normal"))

    def gameover(self):
        self.color("black")
        self.clear()
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER", move=False, align="center", font=("Arial", 25, "normal"))