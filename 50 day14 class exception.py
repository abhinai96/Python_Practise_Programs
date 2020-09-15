#Define a custom exception class which takes a string message as attribute.

"""
class MyError(Exception):
    My own exception class

    Attributes:
        msg  -- explanation of the error
    

    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")"""


class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)
