#write a program that accepts the name of a product and in turn returns their respective prices
#use a dictionary, with at least 5 elements


prices = {
    "apple": 1.00,
    "pear": 1.50,
    "banana": 1.35,
    "orange": 1.47,
    "peach": 2.56
}
userItem = input("What item would you like the price of (Apple, Pear, Banana, Orange, Peach) : ")

item = userItem.lower()
if item in prices:
    price = prices.get(item)
    print("You selected {0}, which has a price of: {1}".format(item, price))
else:
    print("You selected {0}, which is not a valid product".format(item))


