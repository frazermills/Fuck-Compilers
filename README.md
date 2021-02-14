# Brain Fuck Compiler:

### Introduction
This project will become a compiler that compiles brainfuck code. 

### About the Project:
This project was created so that I compile my brainfuck code for a school project. The other reason I am building this project is to learn more about the brainfuck language. Why use brainfuck for a school project? you may ask, well my Computer Science teacher said that we could "implement this in the language of your choice", and hence I used brainfuck.

### How to use it:
* Run the main.py file.
* Enter the name of the file you would like to compiler. (without the file extention)
* Enter the output mode:
  * char mode will output the ASCII equivalent of the cell values without any separation.
  * int mode will output the cell values (as integers) with single space as separation.
* Enter the number of inputs you want to input: (this is an early version and will be changed)
  * If you don't want to input anything enter 0.
  * If you have entered the number of inputs you want, procede to enter each input at a time.
* If debug mode is activated then the listed items (as shown below) will be outputed:
  * The file name
  * Output mode
  * An array of the user's inputs
* If there are any outputs from the program they will be outputed.
* The program will end.

### Built With:
* python 3
* brainfuck

### Current features:
* Can read and process .bf files.
* Can fully interpret .bf files that do not contain inputs from the user.

### Project's future features:
* Add the capabilities of accepting inputs from the user.
* Refactoring code to improve efficiency.
* Adding proper comments to make code more readable.
* GUI interface.
