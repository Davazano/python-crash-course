# When something goes wrong, Python raises an exception. Unhandled, these will cause
# your program to crash. You can handle them using try and except:

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")