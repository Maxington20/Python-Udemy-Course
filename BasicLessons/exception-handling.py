try:
    a = 20
    b = 0
    print(a / b)

except ZeroDivisionError:   # This will go for this specific exception
    print("You cannot divide by zero dummy!")

finally:    #  Code to run no matter what
    print("This is going to execute no matter what.")