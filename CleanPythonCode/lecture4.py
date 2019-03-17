# Always write import statements at the top of the file

# importing module from package
# package name x, module name y
# from x import y   NOT   import y


# how to test for a condition
name = ''
if len(name) == 0:
    print ('No name found')

# Shoudl actually be
name = ''
if len(name):
    print ('name found')
else:
    print ('No name found')


# I put a question on the lecture to find out of this is ok. Will update this file when I know
if name:
    print ('name found')
else:
    print ('No name found')