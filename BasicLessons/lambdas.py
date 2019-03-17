def square(x):  # This is a normal function
    return x**2

print(square(4))

#Using lambdas intead

result = (lambda x: x**2)(30)   # 30 is the argument being passed in

print(result)

