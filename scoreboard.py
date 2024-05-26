from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.goto(x=0,y=280)
        self.hideturtle()
        self.color("white")
        self.write(f"score={self.points}    highscore={self.highscore}",move=False,align="center",font=("Arial",15,"normal"))
    def update(self):
        self.points=self.points+1
        self.clear()
        self.write(f"score={self.points}    highscore={self.highscore}", move=False, align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
            with open("highscore.txt",mode="w") as file:
                file.write(f"{self.highscore}")
        self.points = 0
        self.clear()
        self.write(f"score={self.points}    highscore={self.highscore}", move=False, align="center",font=("Arial", 15, "normal"))

