import turtle
import color 

# Global configuration constants
SN = 3
DIST = 20
UP = 90
DOWN = 270
RGT = 0
LFT = 180

class Snake:
    
    def __init__(self):
        self.seg = []
        self.create_snake()
        
    def create_snake(self):
        # Start at the center and build the initial body moving left
        for i in range(SN):
            # Calculate the starting position for the first 3 segments
            initial_position = (-20 * i, 0)
            self.add_seg(initial_position)
            
    def add_seg(self, position):
        """Creates a segment at a specific (x, y) coordinate tuple."""
        snake_segment = turtle.Turtle("square")
        snake_segment.penup()
        snake_segment.color(color.get_random_color())
        snake_segment.goto(position)  # Expects a tuple like (x, y)
        self.seg.append(snake_segment) 
            
    def extend(self):      
        # Pass the position of the very last segment to add_seg
        self.add_seg(self.seg[-1].position())
    
    def move(self):
        # Use len(self.seg) so the entire body moves, no matter how long it gets!
        for segn in range(len(self.seg) - 1, 0, -1):
            xcor = self.seg[segn - 1].xcor()
            ycor = self.seg[segn - 1].ycor()
            self.seg[segn].goto(xcor, ycor)
        
        self.seg[0].fd(DIST)
        
    def up(self):
        if self.seg[0].heading() != DOWN:
            self.seg[0].setheading(UP)
        
    def down(self):
        if self.seg[0].heading() != UP:
            self.seg[0].setheading(DOWN)
    
    def lft(self):
        if self.seg[0].heading() != RGT:
            self.seg[0].setheading(LFT)
            
    def rgt(self):
        if self.seg[0].heading() != LFT:
            self.seg[0].setheading(RGT)