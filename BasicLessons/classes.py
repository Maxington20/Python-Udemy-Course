class Students:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print('Accepting data')
        self.name = input('Enter name: ')
        self.contact = input('Enter contact: ')

    def putdata(self):
        #   print(f'The name is: {self.name} This is the contact: {self.contact}')
        print('The name is: {0}. The contact number is: {1}'.format(self.name, self.contact))


John = Students("blank",0)
John.getdata()
John.putdata()

class ScienceStudent(Students): # Inheritance - ScienceStudent inherits from Students
    def __init__(self, age):
        self.age = age

    def science(self):
        print("I am a science student")


class HistoryStudent(Students):

    def __init__(self, subject):
        self.subject = subject
    
    def history(self):
        print('I am a history student')


Rob = ScienceStudent(20)
Rob.science()
Rob.getdata()
Rob.putdata()

Maxwell = HistoryStudent('Ancient History')
Maxwell.history()
Maxwell.getdata()
Maxwell.putdata()