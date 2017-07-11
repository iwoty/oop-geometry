
import math
import operator


class Shape:
    """
    This is a abstract class representing geometrical shape.
    """
    AREA = ''
    PERIMETER = ''

    def __init__(self):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        pass

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        pass

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        pass

    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information bout shape
        """
        pass

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        pass

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        pass


class Circle(Shape):

    AREA = 'πr^2'
    PERIMETER = '2πr'

    def __init__(self, r):
        """
        Constructs circle object

        Attributes:
            r (float): radius

        Raises:
            ValueError: If r parameter is below 0.
        """
        if r < 0:
            raise ValueError('Radius cannot be lower than 0.')

        self.r = r

    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        return math.pi * self.r ** 2

    def get_perimeter(self):
        """
        Calculates circle perimeter.

        Returns:
            float: perimeter of the circle.
        """
        return 2 * math.pi * self.r


class Triangle(Shape):

    AREA = '\u221A(s(s-a)(s-b)(s-c))'
    PERIMETER = 'a + b + c'

    def __init__(self, a, b, c):
        """
        Constructs triangle object

        Attributes:
            a (float): side of triangle
            b (float): side of triangle
            c (float): side of triangle

        Raises:
            ValueError: If any of the parameters is below 0.
        """

        if a < 0 or b < 0 or c < 0:
            raise ValueError('Every side of triangle has above 0.')

        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """
        Calculates triangle area.

        Returns:
            float: area of the Triangle
        """
        s = (self.a + self.b + self.c)/2

        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    AREA = '3a'
    PERIMETER = '\u221A(s(s-a)(s-b)(s-c))'

    def __init__(self, a):
        """
        Constructs triangle object

        Attributes:
            a (float): side of triangle

        Raises:
            ValueError: If any of the parameters is below 0.
        """

        if a < 0:
            raise ValueError('Sides of traiangle has to have positive value')

        self.a = a
        self.b = a
        self.c = a


class Rectangle(Shape):

    AREA = '2a + 2b'
    PERIMETER = 'ab'

    def __init__(self, a, b):
        """
        Constructs rectangle object

        Attributes:
            a (float): side of rectangle
            b (float): side of rectangle

        Raises:
            ValueError: If any parameter is below 0.
        """

        if a < 0 or b < 0:
            raise ValueError('Sides of rectangle has to have positive value')

        self.a = a
        self.b = b

    def get_area(self):
        """
        Calculates rectangle area.

        Returns:
            float: area of the rectangle
        """
        return self.a * self.b

    def get_perimeter(self):
        """
        Calculates rectangle perimeter.

        Returns:
            float: perimeter of the rectangle.
        """
        return 2 * self.a + 2 * self.b


class Square(Rectangle):

    AREA = 'a\u00b2'
    PERIMETER = '4a'

    def __init__(self, a):
        """
        Constructs square object

        Attributes:
            a (float): side of square

        Raises:
            ValueError: If any parameter is below 0.
        """
        if a < 0:
            raise ValueError('Side of square has to be above 0.')

        self.a = a
        self.b = a


class RegularPentagon(Shape):

    AREA = '0,25*a\u00b2\u221A(5(5+2\u221A5))'
    PERIMETER = '5a'

    def __init__(self, a):
        """
        Constructs regular pentagon object

        Attributes:
            a (float): side of pentagon

        Raises:
            ValueError: If any parameter is below 0.
        """

        if a < 0:
            raise ValueError('Side of pentagon has to have positive value')

        self.a = a

    def get_area(self):
        """
        Calculates pentagon area.

        Returns:
            float: area of the penthagon
        """
        return (self.a ** 2 * math.sqrt(5 * (5 + 2 * math.sqrt(5))))/4

    def get_perimeter(self):
        """
        Calculates pentagon perimeter.

        Returns:
            float: perimeter of the pentagon.
        """
        return 5 * self.a


class ShapeList:

    def __init__(self):
        """
        Constructs list of Shapes objects.
        """
        self.shapes = []

    def add_shape(self, shape):
        """
        Adds Shape object to shapes list.

        Args:
            shape (object): class object with given shape

        Raises:
            TypeError: If a parameter is not an object of class Shape
        """
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError('Wrong shape.')

    def get_shapes_table(self):
        """Method that returns table with data from objects in shapes list

        Returns:
            final_table (str)
        """
        title_list = ['idx', 'Class', 'Perimeter', 'Formula', 'Area', 'Formula']
        table = []
        index = 0

        for element in self.shapes:
            lista = [index,
                     element.__class__.__name__,
                     round(element.get_perimeter(), 2),
                     element.PERIMETER,
                     round(element.get_area(), 2),
                     element.AREA]
            index += 1
            table.append(lista)

        final_table = ''
        table.insert(0, title_list)
        how_wide = [0 for i in range(len(title_list))]
        iterator = [i for i in range(len(title_list))]

        for row in table:
            for element, i in zip(row, iterator):
                if len(str(element)) > how_wide[i]:
                    how_wide[i] = len(str(element))

        row_length = len(title_list) + 1
        rows_separator = "|"

        for i in iterator:
            how_wide[i] += 4
            row_length += how_wide[i]
            rows_separator += "-" * how_wide[i] + "|"
        table_top = "/" + "-" * (row_length - 2) + "\\"
        table_bottom = "\\" + "-" * (row_length - 2) + "/"

        final_table += table_top + '\n'

        counter = 1
        for row in table:
            to_print = "|"

            for element, width in zip(row, how_wide):
                to_print += "{}".format(element).center(width) + "|"
            final_table += to_print + '\n'

            if counter < len(table):
                final_table += rows_separator + '\n'

            else:
                final_table += table_bottom + '\n'
            counter += 1

        return final_table

    def get_largest_shape_by_perimeter(self):
        '''
        Returns:
            Object with the largest perimeter.
        '''

        dictionary = {}

        for shape in self.shapes:
            dictionary[shape] = shape.get_perimeter()

        return max(dictionary.items(), key=operator.itemgetter(1))[0]

    def get_largest_shape_by_area(self):
        '''
        Returns:
            Object with the largest area.
        '''
        dictionary = {}

        for shape in self.shapes:
            dictionary[shape] = shape.get_area()

        return max(dictionary.items(), key=operator.itemgetter(1))[0]
