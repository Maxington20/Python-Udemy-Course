list = [x**2 for x in range(5)] # [0,1,4,9,16]
print(list)

list = [x**2 for x in range(10) if x**2 % 2 == 0]   # [0,4,16,36,64] only add numbers that are divisible by 2
print(list)