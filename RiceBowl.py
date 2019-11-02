import inquirer
class RiceBowl:
    def addIngredients(self, ings):
        self.ingredients = ings
    def show(self):
        print(self.ingredients)
rb = RiceBowl()
a = [["white", "brown"],["add","skip"],["chicken","beef"],["spicy","sweet"],["add","skip"],["add","skip"]]
b = ["rice","mix veg","meat","sauce","sour cream","guacamole"]
d = {}
for option,question in zip(a,b):
    choices = [inquirer.List('chose',choices = option,message = question)]
    answer = inquirer.prompt(choices)
    d[question] = (answer["chose"])
rb.addIngredients(d)
rb.show()







