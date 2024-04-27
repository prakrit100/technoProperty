Program:

The program should have the following structure:

main.py: The main entry point of the program.
land_management.py: Module containing functions for reading land data, updating land status, and generating invoices/notes.
user_input.py: Module containing functions for getting user input (customer name, kitta numbers, duration, etc.).
data.txt: The text file containing the land data.
invoices/: Directory to store the generated invoices/notes as text files.

The main.py file should have a loop that displays the available lands and gets the user's choice (rent or return land). Based on the choice, it should call the respective functions from the land_management and user_input modules.
The land_management.py module should have functions for:

Reading the land data from the data.txt file.
Updating the land status (available or not available) in the data.txt file.
Generating rent and return invoices/notes as text files in the invoices/ directory.

The user_input.py module should have functions for:

Getting the customer's name.
Getting the kitta number(s) of the land to rent or return.
Getting the rental duration.

You can also include error handling and input validation in these modules.