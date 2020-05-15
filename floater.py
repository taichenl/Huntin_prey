# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


"""from PIL.ImageTk import PhotoImage"""
from prey import Prey
import random


class Floater(Prey): 
    radius = 5
    def __init__(self,x,y):
        self.randomize_angle()
        Prey.__init__(self, x, y, 2*5, 2*5, self._angle, 5)

        
    def update(self, model):
        if random.random() <= 0.3:
            a = self._angle
            change = (random.random() - 0.5)*3.14
            a += change
            if a >= 3 and a <= 7:
                self.set_angle(a)
        self.move()
        self.wall_bounce()
        
        
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius, self._x+Floater.radius, self._y+Floater.radius, fill = 'red')
