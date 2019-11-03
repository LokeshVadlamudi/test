# Rice Bowl Python Program

Adds various ingredients to the object of the rice bowl class and prints the attributes of the object.

**To run the python file:

****cmd -- python RiceBowl.py


**** Package Requirements :

--pip install inquirer

--pip install simple_chalk


**Description:

The functions in the RiceBowl.py:

1. addIngredients(ings)
   This function adds the ings-(dictionary form) to the instance of the class RiceBowl. The ings is the dictionary containing the choices of the user stored.
   
2. show()
   This function prints the ingredients to the terminal.
   
3. askUser(option,question)
   This function returns the choice given by user in a interactive manner. The option list contains the list of choices and question is the message for explaining the user the choices.

4. selecting(a,b,d={})
   This function returns the dictionary containing the choices of user. This function uses askUser to get the input for each ingredient. The output of this function is passed to addIngredients function.
