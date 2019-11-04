### `Dependencies`

- \$pip install inquirer simple_chalk
  > Note: Assuming that python3 is already installed.

### `How To Run`

- \$python RiceBowl.py

### `Description`:

Adds various ingredients to the object of the rice bowl class and prints the attributes of the object.

> Note : Please refer OutputCase`x`.png for different usecase.

The functions in the RiceBowl.py:

- addIngredients(ings) This function adds the ings-(dictionary form) to the instance of the class RiceBowl. The ings is the dictionary containing the choices of the user stored.

- show() This function prints the ingredients to the terminal.

- askUser(option,question) This function returns the choice given by user in a interactive manner. The option list contains the list of choices and question is the message for explaining the user the choices.

- selecting(a,b,d={}) This function returns the dictionary containing the choices of user. This function uses askUser to get the input for each ingredient. The output of this function is passed to addIngredients function.
