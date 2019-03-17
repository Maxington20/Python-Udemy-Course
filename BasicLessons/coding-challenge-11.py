# Consider a list in python which includes prices of all the itesm in  a store. Build a function
# to discount the price of all products by 10%
# use MAP to apply the function to all the elements of the list so that all the products are discounted

prices = [10.76, 11.76, 34.56, 109.54, 32.67, 38.19]

newprices = list(map(lambda x: (x * 0.9), prices))

print(newprices)