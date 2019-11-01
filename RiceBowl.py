#  Rice bowl class
class RiceBowl:
    def addRiceType(self,ricetype):
        self.riceType = "white" if ricetype == "w" else "brown"

    def addMixVeg(self,mixveg):
        self.mixVeg = "yes" if mixveg == "y" else "skip"

    def addMeatType(self,meattype):
        self.meatType = "chicken" if meattype == "c" else "beef"

    def addSauceType(self,saucetype):
        self.sauceType = "spicy" if saucetype == "s1" else "sweet"

    def addSourCream(self,sourcream):
        self.sourCream = "yes" if sourcream == "y" else "skip"

    def addGuacamole(self,guacamole):
        self.Guacamole = "yes" if guacamole == "y" else "skip"

#code to get user input and modify it into lower case
def userInput(a,b):
    response = ''
    while response.lower() not in a:
        response = input(b)
    return (response.lower())

#creating the object
rb = RiceBowl()

#getting the rice type from the user
a1 = userInput({"w", "b"},"please enter type of rice. (w/b) w for white / b for brown \n")
rb.addRiceType(a1)

#adding mix veg choice from the user
a1 = userInput({"y","n"},"please enter 'y' to add mix veg or 'n' to skip \n")
rb.addMixVeg(a1)

#adding meat choice
a1 = userInput({"c","b"},"please enter type of meat. (c/b) c for chicken / b for beef \n")
rb.addMeatType(a1)

#adding sauce choice
a1 = userInput({"s1","s2"},"please enter type of sauce. (s1/s2) s1 for spicy / s2 for sweet \n")
rb.addSauceType(a1)

#adding sour cream choice from the user
a1 = userInput({"y","n"},"please enter 'y' to add sour cream or 'n' to skip \n")
rb.addSourCream(a1)

#adding guacamole choice from the user
a1 = userInput({"y","n"},"please enter 'y' to add guacamole or 'n' to skip \n")
rb.addGuacamole(a1)

#printing the ricebowl ingredients :

from pprint import pprint
pprint(vars(rb))








