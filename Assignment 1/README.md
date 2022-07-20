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

![picture alt](https://github.com/Aminho09/Yektanet-Supplementary-School/blob/main/Assignment%201/Images/Example%20Table.jpg)

 * Searching by ID 

   The program contains a module called MemoryClient. With this module, we can implement the search funcitonality
  
   * The program stores the data of users in this module using DICT data structure. The keys of the structure are the ID of the users and the values of it are the mapped user objects
   * Then, it prints the User Object
   * Printing the User object uses the dunder method of User Object called \_\_STR__().

 * Aggregate on skill

   Yektanet's HR team needs the functionality to see which people have a specific skill.
   The user skills have already stored in an array in the User Object which was splitted by dash (-) in the CSV file.
   So in this functionality user enters an skill (e.g Python) and you should print all User Objects having "Python" skills.
   
 * Setting new data 
   
   HRs should be able to insert new data into the system. When new data of a user is inserted, other functionalities supports it and it appends to the CSV file.
 
 * Merging with other CSV
   
   Another way of inserting new data is by merging a CSV whose path is provided by HR in input to the CSV we already have.
