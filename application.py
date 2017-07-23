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

    shape_types = ['(1) Circle',
                   '(2) Triangle',
                   '(3) Equilateral triangle',
                   '(4) Rectangle',
                   '(5) Square Class',
                   '(6) Regular pentagon']

    SHAPES_DICTIONARY = {'1': Circle,
                         '2': Triangle,
                         '3': EquilateralTriangle,
                         '4': Rectangle,
                         '5': Square,
                         '6': RegularPentagon}

    def __init__(self):
        self.is_running = True

    def run(self):
        shapes_list = ShapeList()  # object containing all shapes added by the user

        while self.is_running:
            # os.system('clear')
            Application.print_menu(self.options)
            option = Application.get_input('Enter choice of menu options: ')

            if option == '1':
                print('Which shape would you like to add:')
                self.print_menu(self.shape_types)
                option = input('\nSelect a shape: ')

                try:
                    if option == '1':
                        r = float(input("Enter radius: "))
                        shapes_list.add_shape(Circle(r))

                    elif option == '2':
                        a = float(input('Enter size of 1st side: '))
                        b = float(input('Enter size of 2nd side: '))
                        c = float(input('Enter size of 3rd side: '))
                        shapes_list.add_shape(Triangle(a, b, c))

                    elif option == '3':
                        a = float(input('Enter size of sides: '))
                        shapes_list.add_shape(EquilateralTriangle(a))

                    elif option == '4':
                        a = float(input('Enter size of 1st side: '))
                        b = float(input('Enter size of 2nd side: '))
                        shapes_list.add_shape(Rectangle(a, b))

                    elif option == '5':
                        a = float(input('Enter size of sides: '))
                        shapes_list.add_shape(Square(a))

                    elif option == '6':
                        a = float(input('Enter size of sides: '))
                        shapes_list.add_shape(RegularPentagon(a))

                    else:
                        input('\nWrong number. Press Enter to continue')

                except ValueError:
                    print('Wrong option.')

            elif option == '2':
                print(shapes_list.get_shapes_table())

            elif option == '3':
                output_value = shapes_list.get_largest_shape_by_perimeter()
                print(output_value.__class__.__name__)

            elif option == '4':
                output_value = shapes_list.get_largest_shape_by_area()
                print(output_value.__class__.__name__)

            elif option == '5':
                print('\nChoose shape to see formulas:')
                self.print_menu(self.shape_types)
                option = input('\nSelect a shape: ')

                if option in self.SHAPES_DICTIONARY.keys():
                    shape_name = self.SHAPES_DICTIONARY[option].__name__
                    area_formula = self.SHAPES_DICTIONARY[option].AREA
                    perim_formula = self.SHAPES_DICTIONARY[option].PERIMETER
                    print('\n{}\nArea formula = {}\nPerimeter formula = {}\n'.format(shape_name, area_formula, perime_formula))

            elif option == '0':
                self.is_running = False

            else:
                print('==> There is no such an option. <==')

    @staticmethod
    def get_input(message):
        return input(message)

    @staticmethod
    def print_menu(menu_options):
        print('\n'.join(menu_options))
