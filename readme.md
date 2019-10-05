The code will run idefinitely checking for prices on amazon. When the price of the product gets lower than what you want it for then it will send the specified email id a mail 

**How to create a list of products**
\nThe list of products needs to be created in product_list.py file. there is one dummy entry. You need to specify all the product entries in that format
It is basically a dictionary of all the products. The key is the name of the product itself and the dictionary contains another dictionary corresponding to the key .
The second dictionary specifies some attributes . You need to copy those attributes exactly for each new entry in the dictionary.

**How to run the code**
1. Create the list of products as specified above.
2. Enter values in FROM_MAIL_ID, TO_MAIL_ID AND APPPASSWORD located in config.py
3. python main.py
The code will start running and will update every 60 seconds and if it finds that one of the products listed by you have a price lower than what you specified then it will send a mail once