import inquirer
class RiceBowl:
    def addIngredients(self, ings):
        self.ingredients = ings
    def show(self):
        print(self.ingredients)

#model function for getting choice from the user
def askUser(option,question):
    choices = [inquirer.List('selected', choices=option, message=question)]
    answer = inquirer.prompt(choices)
    return answer["selected"]

def selecting(a,b,d):
    #asking user about the ingredients for first time
    for i,j in zip(a[:-1],b[:-2]):
        d[j] = askUser(i,j)

    #asking the user for confirmation
    c = askUser(a[-1],b[-2])

    #if not confirm, we get the changes from the user or show the review of choices.
    while c is not a[-1][0]:
        if c is a[-1][2]:
            print("{} \n".format(d))
        else:
            f = askUser(b[:-2], b[-1])
            d[f] = askUser(a[b.index(f)],f)
        c = askUser(a[-1], b[-2])
    return d

a = [["white", "brown"],["add","skip"],["chicken","beef"],["spicy","sweet"],["add","skip"],["add","skip"],["confirm","edit","review"]]
b = ["rice","mix veg","meat","sauce","sour cream","guacamole","want any change?","which one?"]

#instance of ricebowl class
rb = RiceBowl()
rb.addIngredients(selecting(a,b,d={}))
rb.show()
