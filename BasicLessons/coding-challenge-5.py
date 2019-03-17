# write a function which would divide two numbers. design the function in a manner
# that it handles the divide by zero exception

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except:
        print("You cannot divide strings")
    finally:
        print("Thanks for participating\n")

divide(5, 1)
divide(1, 0)
divide("x", "y")