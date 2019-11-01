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
#inquirer
import inquirer

def userInput(a,b):
    choices = [
        inquirer.List('option',
                      message=b,
                      choices=a,
                      ),
    ]
    answers = inquirer.prompt(choices)
    return (answers["option"])

#creating the object
rb = RiceBowl()

#getting the rice type from the user
a1 = userInput(["white", "brown"],"select type of rice:")
rb.addRiceType(a1)

#adding mix veg choice from the user
a1 = userInput(["add","skip"],"want to add mix veg?")
rb.addMixVeg(a1)

#adding meat choice
a1 = userInput(["chicken","beef"],"select type of meat:")
rb.addMeatType(a1)

#adding sauce choice
a1 = userInput(["spicy","sweet"],"select type of sauce:")
rb.addSauceType(a1)

#adding sour cream choice from the user
a1 = userInput(["add","skip"],"want to add sour cream?")
rb.addSourCream(a1)

#adding guacamole choice from the user
a1 = userInput(["add","skip"],"want to add guacamole?")
rb.addGuacamole(a1)

#printing the ricebowl ingredients :

from pprint import pprint
pprint(vars(rb))








