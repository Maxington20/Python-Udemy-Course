# build two functions discounting products on a website. function 1 is for student discount of 10%
# the second discount is additonal 5% of the current discounted price
# design the methods so they can be applied simultaneously

def student_discount(price):
    price = price - (price * 0.10)
    return price

def additional_discount(newprice):
    newprice = newprice - (newprice * 0.05)
    return newprice

selling_price = 100

print(additional_discount(student_discount(selling_price)))
