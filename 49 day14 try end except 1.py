#Write a function to compute 5/0 and use try/except to catch the exceptions.
def abhi():
        return 5/0
try:
        abhi()
except ZeroDivisionError as ze:
        print("you cant divide by zero")


