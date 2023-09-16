"""Exceptions for oppe"""


class OppeError(Exception):
    """Base class for other exceptions"""

    def __init__(self, msg='', data=None):
        self.msg = msg
        self.data = data

    def __str__(self):
        """Return a string representation of the exception"""
        return f'{self.msg}: {self.data}'


class UuidValidationError(OppeError):
    """Uuid Validation Error"""


class EventRequestError(OppeError):
    """Event Request Error"""


class ApiTokenMissingError(OppeError):
    """Api Token Missing Error"""
