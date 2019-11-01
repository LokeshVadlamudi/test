import inquirer #for getting user input through interactive method.
#  Rice bowl class
class RiceBowl:
    def addRiceType(self,ricetype):
        self.riceType = ricetype

    def addMixVeg(self,mixveg):
        self.mixVeg = mixveg

    def addMeatType(self,meattype):
        self.meatType = meattype

    def addSauceType(self,saucetype):
        self.sauceType = saucetype

    def addSourCream(self,sourcream):
        self.sourCream = sourcream

    def addGuacamole(self,guacamole):
        self.Guacamole = guacamole

#code for user input
def userInput(a,b):
    choices = [inquirer.List('option',choices = a,message = b)]
    answer = inquirer.prompt(choices)
    return answer["option"]

#creating the object
rb = RiceBowl()

#adding the rice choice
rb.addRiceType(userInput(["white", "brown"],"select type of rice:"))

#adding mix veg choice
rb.addMixVeg(userInput(["add","skip"],"want to add mix veg?"))

#adding meat choice
rb.addMeatType(userInput(["chicken","beef"],"select type of meat:"))

#adding sauce choice
rb.addSauceType(userInput(["spicy","sweet"],"select type of sauce:"))

#adding sour cream choice
rb.addSourCream(userInput(["add","skip"],"want to add sour cream?"))

#adding guacamole choice
rb.addGuacamole(userInput(["add","skip"],"want to add guacamole?"))

#printing the ricebowl ingredients :
from pprint import pprint
pprint(vars(rb))
