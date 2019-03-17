import re   # module for regular expressions

# match function

pattern = r"eggs"

if re.match(pattern, "eggseggseggsbacon"):  # this will match
# if re.match(pattern, "baconeggseggsbacon"): this will not match
    print('Match found')
else:
    print('No match found')


# Search function

if re.search(pattern, "baconeggseggseggsbacon"): # returns match found because it does when found ANYWHERE in the string
    print("match found")

else:
    print("match not found")


# find-all function

print(re.findall(pattern, "baconeggseggseggsbacon"))    # will print eggs each time it shows up in the string (3)


# Find and replace function

string = "My name is John, Hi I'm John"

pattern = r"John"

newstring = re.sub(pattern, "Rob", string)  # what to look for, replace with, where to look

print(newstring)


# The dot metacharacter

pattern = r"gr.y"   # the . signifies any character that you want (1 character)

if re.match(pattern, "gray"):   # this will match
#if re.match(pattern, "graay"):  # this will not match
    print("match found")
else:
    print("match not found")


#   Caret ^ and dollar sign $
#   caret signifies start, $ signifies the end of the string

pattern = r"^gr.y$"

if re.match(pattern, "grey"):   # this will match "brey" will not "grbp" will not
    print("match 1")


#   character class
#AA1
pattern = r"[A-Z][A-Z][0-9]"    # the first character needs to be upper letter, second a upper letter, third a number 0-9

if re.search(pattern, "AA1"):
    print("match found")

if re.search(pattern, "aa1"):   # This will not match, because they are lower case letters
    print ("match foundssss")



#   Star metacharacter *    repeated 0 to many times
pattern = r"eggs(bacon)*"   # () is how you make a group

if re.match(pattern, "eggs"):   # this will match because there are 0 - many instances of bacon in the string
                                # eggsbacon will match
                                #eggsbaconbacon will match
                                #bacon will not match
    print("match found")


# Groups
pattern = r"bread(eggs)*bread"  # between breads can have as many eggs as you want

if re.match(pattern, "breadbread"): # this will match
                                    # breadeggsbread this will match
                                    # breadeggseggseggsbread this will match
                                    #eggsbreadeggsbread this will not match
    print("match")



# NEW CONTENT BELOW





#                   REVISTED            ****

# Special characters
print('hello \n world') # Not a pure string

print(r'hello \n world') # pure string/raw string will print the \n instead of doing it


string = 'abc'
pattern = 'a'

if re.match(pattern, string):   # Will only match if the beginning matches
    print('Match Found')
else:
    print('Match not found')


string = 'babc'
pattern = 'a'

if re.search(pattern, string):  # Will search the whole string and find ANY matches
    print('Match Found')
else:
    print('Match not found')
    


# META CHARACTERS
# special set of characters that don't match. they create a pattern that should be matched
# List of meta characters:

    #   * character - takes 0 or more of the previous character
string = "ac"
pattern = "ab*c"
if re.match(pattern, string):
    print('Match Found')


    #   + character - character before must be present 1 or more times
string = "ac"   # This will be not found
pattern = "ab+c"
if re.match(pattern, string):
    print('Match Found')

else:
    print('not found')


    # {} character - repeating the preceding character, x number of times e.g. {2}
string = "abb"  # This will match
pattern = r"ab{2}"   # b should be repeated at least twice
if re.match(pattern, string):
    print ("match found")
else:
    print("no match found")


    # . character (wildcard) - any character except line breaks
string = 'acb'
pattern = r"a.b"
if re.match(pattern, string):
    print("match found")
else:
    print("match not found")


    # ? character  (optional) - any character preceding this is optional
string = 'pythonfile'   # matches because the - is optional
pattern = r"python-?file"
if re.match(pattern, string):
    print("match found")
else:
    print("match not found")


    # ^ character (carrot) - sets up the position for match. tells computer that match must start from this point
string = "91123456"
pattern = r"^91"    # only going to match up with all strings that start with 91
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")


    # d character class - pattern should match any digit character
string = "91123456"
pattern = r"\d{5}"    # should only be digits with a minimum of 5
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")


    # D character class - any non digit character
string = "aaaaa"
pattern = r"\D{5}"    # should only non digit chars with a minimum of 5
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")


    # w character class - any alpha numeric character
string = "111aaaaa"
pattern = r"\w{5}"    # should only alpha numeric chars with a minimum of 5
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")


    # [] square bracket notation - match specific characters
string = "Python"
pattern = r"^[Pp]ython"    # Will accept Python or python. starting with upper case p or lower case p
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")


    # [] - match a range of chars
string = "zython"
pattern = r"^[a-z]ython"    # must be lower case    upper and lower [a-zA-Z]
if re.match(pattern, string):
    print("match found")
else:
    print("no match found")