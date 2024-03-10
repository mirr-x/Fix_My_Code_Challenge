#!/usr/bin/python3
"""
User class implementation.
"""


class User():
    """ User class definition. """

    __email = ''

    def __init__(self, email=None):
        """ User class constructor. """

        if email is not None:
            self.__email = email

    @property
    def email(self):
        """ Function to return user email. """

        return self.__email

    @email.setter
    def email(self, value):
        """ User email setter function. """

        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """ Cleating User object in the main function. """

    u = User()
    u.email = 'john@snow.com'
    print(u.email)
