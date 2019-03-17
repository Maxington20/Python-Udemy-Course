# Dictionaries (key value pairs)
# Can store any kind of value in a dictionary

people = {"Max": 31, "Kim": 34}

print(people["Max"])  # will print 31. The value associted with the key Max

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

thePeople = [{'age' : 31, 'name' : 'Max', 'eyes' : 'blue'}, 
             {'age' : 35, 'name' : 'Kim', 'eyes' : 'brown'},
             {'age' : 23, 'name' : 'Taylor', 'eyes' : 'blue'}]

# dictionary functions
print("\n", 1 in numbers)  # Will check if 1 is present in the list

print(numbers.get(2))   # Will print the value for the key

print(numbers.get(5))   # Will print "none" as there is no key 5

print(numbers.get(5, "Key not found sucka!"))  # Will print the string typed in if the key is not found

for person in thePeople:
    if person.get('name') == 'Taylor' or person.get('name') == 'Max':
        print(f"\nHere we go. This person's name is {person.get('name')}.", \
        f"He is a handsome {str(person.get('age'))} year old man with", \
        f"{person.get('eyes')} eyes.")
    else:
        continue

print(numbers.keys())
print(numbers.values())

for person in thePeople:
    print(person)

