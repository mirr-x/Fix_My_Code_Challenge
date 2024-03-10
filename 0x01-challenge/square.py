#!/usr/bin/python3
"""
Python script to implement square class.
"""


class Square():
    """ Square class definition """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=None):
        """ My class constructor """

        if height is None:
            height = width
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ Property to return height"""

        return self.__height

    @property
    def width(self):
        """ Property to return width """

        return self.__width

    @height.setter
    def height(self, value):
        """Function to set the height"""

        if type(value) is not int or value < 0:
            raise ValueError("height must be a positive integer")

        self.__height = value

    @width.setter
    def width(self, value):
        """Function to set the width"""

        if type(value) is int or value < 0:
            raise ValueError("width must be a positive integer")

        self.__width = value

    def area_of_my_square(self):
        """ Method to return area of the square """

        return self.__width * self.__width

    def permiter_of_my_square(self):
        """ Function to return perimeter of the square. """

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Function to return the string representation of the square
        """

        if type(self.__width) is not int or type(self.__height) is not int:
            raise ValueError("width and height must be a positive integer")

        for _ in range(self.__height):
            print("*" * self.__width)

        return "{}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    """ creating object of my class. """

    s = Square(width=12, height=8)
    print(s)
    print("Area of the square is: {}".format(s.area_of_my_square()))
    print("Perimeter of the square is: {}".format(s.permiter_of_my_square()))
