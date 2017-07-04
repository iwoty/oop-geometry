import sys
import os
from geometry import *


class Application:
    options = ['Learn Geometry.'
               'What do you want to do?'
               '(1) Add new shape'
               '(2) Show all shapes'
               '(3) Show shape with the largest perimeter'
               '(4) Show shape with the largest area'
               '(5) Show formulas'
               '(0) Exit program']

    def __init__(self):
        self.is_running = True

    def run(self):
        shapes = ShapeList()  # object containing all shapes added by the user
