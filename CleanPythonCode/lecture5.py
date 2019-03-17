
# list
a = [1, 2, 3, 4, 5, 6, 7, 8]

result = list (map (lambda x: x * 2, a))

print (result)

# could be done better by using list comprehension:
result = [x * 2 for x in a]
print (result)
# uses less resources


# can use else statement in for loop. else will always run unless you make it not run
for x in range (5):
    print(x)
else:
    print('This is the else block')

# else block will not execute for this one
for x in range(5):
    print(x)
    if x == 4:
        break
else:
    print('This is the else block')