
def bmiCalc(h, w):
    return w / (h * h)

h = float(input("Please enter your height: "))
w = float(input("Please enter your weight: "))

bmi = bmiCalc(h, w)

print("Your bmi is : ", bmi)