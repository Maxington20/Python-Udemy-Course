def add(x):
    return x + 2


newlist = [10, 20, 30, 40, 50]

result = list(map(add, newlist))

print(result)

# or could use lambdas instead

result = list(map(lambda x: x + 2, newlist))
print(result)