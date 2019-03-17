file = open("demo.txt", 'r')
#   Do something with the file
content = file.read()   # Reads the whole file
#   file.read(10)       Reads the first 10 bytes
#   file.readline()     # Reads a single line
print(content)
file.close()

# Writing content to a file
file = open("demo.txt", 'w')    # This will overwrite the file's content
file.write("This is the text to write into the file")
file.close()

# Appending to a file
file = open("demo.txt", 'a')    # append mode
file.write("\nthis is the new line")
file.close()

file = open("demo.txt", 'r')
content = file.read()
print(content)
file.close()
