numbers = [4, 5, 6]

numberDate = [12, 12, 2018]

newstring = "Numbers: {0},{1},{2}".format(numbers[0], numbers[1], numbers[2])

newerString = "Date: {0}/{1}/{2}".format(numberDate[0], numberDate[1], numberDate[2])

print(newstring)
print(newerString)

a = "{x}/{y}".format(x=100, y=200)
print(a)