# String functions

#Join
print(",,,".join(["Apple","Banana","Mango"]))   # will print the list, with each item separated by ,,,

#Replace
print("Hello there".replace("there","Max")) # Will replace there with Max

newstring = "Hello there"
print(newstring.replace("there","World")) # Same principle using a string variable instead of a string

#startwith
newstring = "This is a string"
print(newstring.startswith("This")) # prints true, because the string does start with "This"

#endswith
print(newstring.endswith("string")) # prints true, because the string does end with string

#upper
print(newstring.upper())    # prints the string in all upper case letters

#lower
print(newstring.lower())    # prints the string in all lower case letters