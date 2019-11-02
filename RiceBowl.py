import inquirer
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

#creating the object
rb = RiceBowl()

a = [["white", "brown"],["add","skip"],["chicken","beef"],["spicy","sweet"],["add","skip"],["add","skip"]]
b = ["rice?","mix veg?","meat?","sauce?","sour cream?","guacamole?"]
c = [rb.addRiceType,rb.addMixVeg,rb.addMeatType,rb.addSauceType,rb.addSourCream,rb.addGuacamole]

for option,question,fun in zip(a,b,c):
    choices = [inquirer.List('chose',choices = option,message = question)]
    answer = inquirer.prompt(choices)
    fun(answer["chose"])

#printing the ricebowl ingredients :
from pprint import pprint
pprint(vars(rb))
