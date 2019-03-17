numbers = [0, 100, 200, 300, 400, 500, 600]

print(numbers[2:5]) # List slicing. will print item at pos 2 to pos 4 (5-1) 200,300,400,

print(numbers[:3])  # will print all items before position 3. 0,100,200

print(numbers[3:])  # will print out the items starting at position 3. 300,400,500,600

print(numbers[1:6:2])   # Will print out pos 1 - 6, with an interval of 2. 100,300,500