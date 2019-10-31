#  Rice bowl class
class RiceBowl:
    def addRiceType(self,ricetype):
        if ricetype == "w":
            self.riceType = "white"
        else:
            self.riceType = "brown"
    def addMixVeg(self,mixveg):
        if mixveg == "y":
            self.mixVeg = "yes"
        else:
            self.mixVeg = "skip"
    def addMeatType(self,meattype):
        if meattype == "c":
            self.meatType = "chicken"
        else:
            self.meatType = "beef"
    def addSauceType(self,saucetype):
        if saucetype == "s1":
            self.sauceType = "spicy"
        else:
            self.sauceType = "sweet"
    def addSourCream(self,sourcream):
        if sourcream == "y":
            self.sourCream = "yes"
        else:
            self.sourCream = "skip"
    def addGuacamole(self,guacamole):
        if guacamole == "y":
            self.Guacamole = "yes"
        else:
            self.Guacamole = "skip"


#creating the object
rb = RiceBowl()

#getting the rice type from the user
response = ''
while response.lower() not in {"w","b"}:
    response = input("please enter type of rice. (w/b) w for white / b for brown \n")
rb.addRiceType(response.lower())

#adding mix veg choice from the user
response = ''
while response.lower() not in {"y","n"}:
    response = input("please enter 'y' to add mix veg or 'n' to skip \n")
rb.addMixVeg(response.lower())

#adding meat choice
response = ''
while response.lower() not in {"c","b"}:
    response = input("please enter type of meat. (c/b) c for chicken / b for beef \n")
rb.addMeatType(response.lower())

#adding sauce choice
response = ''
while response.lower() not in {"s1","s2"}:
    response = input("please enter type of sauce. (s1/s2) s1 for spicy / s2 for sweet \n")
rb.addSauceType(response.lower())

#adding sour cream choice from the user
response = ''
while response.lower() not in {"y","n"}:
    response = input("please enter 'y' to add sour cream or 'n' to skip \n")
rb.addSourCream(response.lower())

#adding guacamole choice from the user
response = ''
while response.lower() not in {"y","n"}:
    response = input("please enter 'y' to add guacamole or 'n' to skip \n")
rb.addGuacamole(response.lower())



#printing the ricebowl ingredients :
print("\n\nThe Rice bowl ingredients are:\n")
print("Rice Type : {}".format(rb.riceType))
print("Mixed Vegetables : {}".format(rb.mixVeg))
print("Meat Type : {}".format(rb.meatType))
print("Sauce Type : {}".format(rb.sauceType))
print("Sour Cream : {}".format(rb.sourCream))
print("Guacamole : {}".format(rb.Guacamole))










