
from shapes import Shape, Frame
from pylab import random as r

####################################################

class MovingShape:
    def __init__(self, frame, shape, diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, frame, diameter)
        
        
        self.dx = 2 + r() * 4
        if r() < 0.5:
            self.dx *= -1
        self.dy = 2 + r() * 4
        if r() < 0.5:
            self.dy *= -1
            
        self.calc_min_max_xy(frame)
        
        self.x = self.minx + r() * (self.maxx - self.minx)
        self.y = self.miny + r() * (self.maxy - self.miny)
        self.goto_curr_xy()
        
    def calc_min_max_xy(self, frame):
        d = self.diameter
        self.minx = d / 2
        self.maxx = frame.width - d / 2
        self.miny = d / 2
        self.maxy = frame.height - d / 2
            
    def goto_curr_xy(self):
        self.figure.goto(self.x, self.y)

    def move_tick(self):
        self.x += self.dx
        self.y += self.dy
        self.goto_curr_xy()
        
        
        if self.x < self.minx or self.x > self.maxx:
            self.dx *= -1
            self.report_bounce()
        if self.y < self.miny or self.y > self.maxy:
            self.dy *= -1
            self.report_bounce()
            
    def report_bounce(self):
        print("I'm a bouncing {0}".format(self.shape), end="")
        print(" - my area is {0} sq units!".format(self.my_area()))
 
####################################################

class Square(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, "square", diameter)
        
    def my_area(self):
        return self.diameter ** 2

####################################################

class Diamond(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, "diamond", diameter)
        
    def calc_min_max_xy(self, frame):
        d = self.diameter * 2 ** 0.5
        self.minx = d / 2
        self.maxx = frame.width - d / 2
        self.miny = d / 2
        self.maxy = frame.height - d / 2
        
    def my_area(self):
        return self.diameter ** 2

####################################################

class Circle(MovingShape):
    def __init__(self, frame, diameter):
        MovingShape.__init__(self, frame, "circle", diameter)
        
    def my_area(self):
        return (self.diameter / 2) ** 2 * 3.141

####################################################

