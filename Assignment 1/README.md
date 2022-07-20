# First Assignment
We want to write a Python program  to help Yektanet's HR staff when working with CSV files.
The program should read a CSV file from the file system and provide some functionalities.

Our CSV file contain information about people with the following fields:
  * ID (int)
  * First Name (String)
  * Last Name (String)
  * Address (String)
  * Phone Number (String)
  * Country (String)
  * Age (int)
  * Skills (String)

The Program Supports the following features:
 1. Printing the CSV file on terminal
 2. Search by ID
 3. Aggregation on skills
 4. Setting new data on CSV file 
 5. Merging with other CSV file

Details of each feature:
 * Printing
   It prints the given CSV in the terminal like the example.
   
    * All contents of a cell are in the middle of the cell
    * Address cell of the CSV file may be more than 80 characters so the program breaks it into two or more rows and doesn't let any of the printed row cells get bigger than 80 characters.
![picture alt](blob:https://web.telegram.org/f4693265-d485-4291-b056-1e02cbef648f)
