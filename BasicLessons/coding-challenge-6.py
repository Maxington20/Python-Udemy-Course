# Write code to opena  file and write some data into it
# open the file, read the content and display it
# write code to add additional text to the existing file

file = open("coding-challenge-6.txt",'w')
file.write("This is my coding challenge 6 content")
file.close()

file = open("coding-challenge-6.txt",'r')
content = file.read()
print(content)
file.close()

file = open("coding-challenge-6.txt", 'a')
file.write("\nThis is the appended content")
file.close()

file = open("coding-challenge-6.txt",'r')
content = file.read()
print(content)
file.close()