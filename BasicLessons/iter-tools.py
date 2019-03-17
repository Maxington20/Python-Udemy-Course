from itertools import count, accumulate,takewhile


for i in count(3):  # this will print 3 to 20
    print(i)

    if i >= 20:
        break

numbers = list(accumulate(range(8)))    # this will print out 0,1,3,6,10,15,21,28 (0, then 0+1, then 1+2, 3+3,6+4 etc.
print(numbers)

print(list(takewhile(lambda x: x <= 6,numbers)))    # prints the elements in numbers that are less than or equal to 6
