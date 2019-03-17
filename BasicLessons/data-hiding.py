class Myclass:
    __hiddenvariable = 0    # the __ (dunder sign) make this a hidden variable

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)


objectone = Myclass()
objectone.add(5)
# print(objectone.__hiddenvariale) This will not work, because you cannot access this var outside the class

