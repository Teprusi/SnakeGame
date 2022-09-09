from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 10, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 270)
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=('Courier', 20, 'normal'))
