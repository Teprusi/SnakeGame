from turtle import Turtle
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.part = 0
        self.segments = []
        for x in range(3):
            self.add_segment()

        self.head = self.segments[0]

    def add_segment(self):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.back(self.part)
        self.part += 20
        self.segments.append(new_turtle)

    def extend(self):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(self.segments[-1].position())
        self.segments.append(new_turtle)

    def move(self):
        for segment_n in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_n].goto(self.segments[segment_n - 1].pos())
        self.segments[0].forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
