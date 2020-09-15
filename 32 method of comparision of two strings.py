#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
def length():
        a=input("enter name")
        b=input("enter name")
        if len(a)>len(b):
                print(a)
        elif len(b)>len(a):
                print(b)
        else:
                print(a)
                print(b)
length()
