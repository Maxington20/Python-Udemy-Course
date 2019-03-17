# Create a superclass named Computer, which has two sub classes named Desktop and Laptop
# define two methods in the computer class named getspecs and displayspecs, to get the specs and dispaly the
# specs of the computer. Desktop class and laptop class shoudl have one spec which is exclusive to them. ex
# laptop can have weight. Make sure sub classes have their own methods to get and display their spec.
#Create an object of laptop/dsektop and make sure to call all the methods from the computer class as well
#as the methods from the own class

class Computer:

    def __init__(self, ram, hardDrive):
        self.ram = ram
        self.hardDrive = hardDrive

    def getspecs(self):
        self.ram = input('Please enter the amount of ram the computer has: ')
        self.hardDrive = input('Please enter the size of the hard drive: ')

    def displayspecs(self):
        print(f'The amount of ram is: {self.ram}, and the size of the hard drive is: {self.hardDrive}')


class Laptop(Computer):

    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Please enter the weight of the laptop in pounds')

    def displayweight(self):
        print(f'The laptop weights {self.weight}')


class Desktop(Computer):

    def __init__(self, towerheight):
        self.towerheight = towerheight

    def gettowerheight(self):
        self.towerheight = input('How tall is the desktop\'s tower in inches: ')

    def displaytowerheight(self):
        print(f'The tower is {self.towerheight} inches tall')


laptop1 = Laptop("blank")

desktop1 = Desktop("blank")

laptop1.getspecs()
laptop1.getweight()
laptop1.displayspecs()
laptop1.displayweight()

desktop1.getspecs()
desktop1.gettowerheight()
desktop1.displayspecs()
desktop1.displaytowerheight()