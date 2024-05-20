from turtle import Turtle
ALIGNMENT="center"
FONT=("arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score=0
        self.color("white")  
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", align='center',font=("Arial",24,"normal"))


        self.hideturtle()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT,font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)