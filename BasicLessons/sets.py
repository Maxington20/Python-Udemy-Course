numbers = {1, 2, 3, 4, 5, 6}

print(numbers)  # to print the set

print(5 in numbers)  # Will print true because 5 is in the set

# can add and remove elements from sets
numbers.add(9)  # Will add 9 to the end of the set

print(numbers)

numbers.remove(9)  # Will remove 9 from the set
print(numbers)

# algebraic functions
seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8}

# union
print(seta | setb)  # will combine seta and setb, removing duplicates to print 1,2,3,4,5,6,7,8

# intersection
print(seta & setb)  # will print the common elements between these two sets. 4, 5

# difference
print(seta - setb)  # will print the values in seta that are not in setb 1,2,3


