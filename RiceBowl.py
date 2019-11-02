import inquirer
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

a = [["white", "brown"],["add","skip"],["chicken","beef"],["spicy","sweet"],["add","skip"],["add","skip"]]
b = ["rice?","mix veg?","meat?","sauce?","sour cream?","guacamole?"]
res = []

for i,j in zip(a,b):
    choices = [inquirer.List('option',choices = i,message = j)]
    answer = inquirer.prompt(choices)
    res.append(answer["option"])

a = [rb.addRiceType,rb.addMixVeg,rb.addMeatType,rb.addSauceType,rb.addSourCream,rb.addGuacamole]

for i,j in zip(a,res):
    i(j)

#printing the ricebowl ingredients :
from pprint import pprint
pprint(vars(rb))








