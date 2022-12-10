guess_list = []

try:
    # Open the file and check if it was successfully opened
    with open('wordlist.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    # Handle the error if the file is not found
    print("The file 'wordlist.txt' could not be found")
except IOError:
    # Handle any other I/O errors that might occur
    print("An error occurred while reading from the file")
except:
    # Catch any other exceptions that might be raised
    print("An unknown error occurred")


print("Good starter words are: slice, tried, crane")

for guesses in range(6):
    guess = input("\nword:").lower()
    print("g - green, y - yellow, w - wrong / grey")
    feedback = input("Feedback= ").lower()
    if feedback == "ggggg":
        print("Well Done! Guess",guesses+1)
        break

    temp_tuple = tuple(guess_list)
    for word in temp_tuple: 
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:
                guess_list.remove(word)
                break

    counter = 0
    for word in guess_list:
        print(word,end=", ")
        counter= counter +1
        if counter == 8:
            print("")
            counter = 0