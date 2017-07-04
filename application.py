import sys
import os
from geometry import *


class Application:
    options = ['Learn Geometry.',
               '  What do you want to do?',
               '  (1) Add new shape',
               '  (2) Show all shapes',
               '  (3) Show shape with the largest perimeter',
               '  (4) Show shape with the largest area',
               '  (5) Show formulas',
               '  (0) Exit program']

    def __init__(self):
        self.is_running = True

    def run(self):
        shapes = ShapeList()  # object containing all shapes added by the user

        while self.is_running:
            # os.system('clear')
            self.display_menu()
            option = self.get_input('Enter choice of menu options: ')

            if option == '1':
                pass

            elif option == '2':
                pass

            elif option == '3':
                pass

            elif option == '4':
                pass

            elif option == '5':
                pass

            elif option == '0':
                self.is_running = False

    def get_input(self, message):
        return input(message)

    def display_menu(self):
        print('\n'.join(self.options))
