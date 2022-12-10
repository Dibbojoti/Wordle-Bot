# Wordle-Bot
It solves wordle game from The New Yorks Time
This code is for Wordle  where the user has to guess a five-letter word. The user is given six chances to guess the word, and for each guess, the user is given feedback in the form of "g" for correct letters in the correct position, "y" for correct letters in the wrong position, and "w" for incorrect letters. Based on this feedback, the user has to make a new guess.

The code first tries to open the file wordlist.txt and read each line from it, appending each line to the guess_list list. If the file is not found or any other I/O error occurs, it will print an error message.

Next, the code suggests some starter words that the user can use for their first guess, and then enters a loop where it asks the user to make a guess and provide feedback. For each guess, the code updates the guess_list list by removing any words that do not match the feedback. It then prints the remaining words in the list, up to a maximum of eight words per line.
