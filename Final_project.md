# CS50 Final Project by Joe Plankinton
## Learn Spanish 0-10 program

#### Overview


This is the first step in my journey to learning real standardized coding practices.  I have coded for projects and raspberry pies for solutions to problems.  This is the first entry into sharing code with anyone else.  Please provide advise where needed. 

My CS50 Final Project was to code something that could be used by anyone to learn something.  It is designed to translate 0 to 10 into the Spanish translation printed on the screen as well as to hear the pronunciation of the Spanish word.  
To get started, first you will need a compiler for python 3.  I used Visual Studio Code, but you can any compiler like PyCharm. Also, you will need to install some pip packages.
Pip install pyttsx3
Pip install re
Pip install sys
Pip install pytest

The file can be downloaded from github.com
[Github] (https://github.com/JPHoneybadger/CS50_Final_Project.git)

Once you have the program downloaded and the required pip packages, you can open the program in your compiler.
In the program is two classes so I could call the same variable for several functions, global scope. The main() is called and the input is received from the user. The input is checked for correctness in the function check_num() using regular expression. The return is passed to the function converted_num(). This function does several tasks.  First it prints out the users input. Calls the dictionary for the Spanish word for the input and prints it on the screen.  Then speak_num_spanish() function is called.  The speak_num_spanish() function provided the pronunciation of the Spanish word. Once completed the play_again() is called from main() asking the user if they want to play again. 

This provides user recognition of the inputted number, the word in Spanish, and the sound of the word in Spanish. Using both sight and hearing senses to help the user learn Spanish 0 to 10.

A video of the program can be found on YouTube.
[YouTube]  (https://youtu.be/333PsE3qyAQ)
 
The second program is a pytest.  I had several issues trying to make it work.  I called functions within functions which pytest did not like. I tried several ways and failed. I then created the two classes for the same variables to be used by several functions.  

#### Conclusion

In the end, changes I would make would make in the future is to import a CSV file of more Spanish numbers to be used. Otherwise, I think the program does what I wanted to accomplish.