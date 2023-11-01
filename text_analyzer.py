# Sarah Ma
# Project 1  - Analyzing Text Files

# Imports
import re # To use Regular Expressions
import sys # To access the input provided at the command line (command line parameters)

# Print the number of parameters / arguments provided by the user at the command line
print ("Number of arguments:", len(sys.argv), "arguments")

# Print the parameters printed at the command line
print ("Argument List:", str(sys.argv))

# The name of the text file is provided as the 2nd parameter and is accessed using index 1
# Index 0 contains the first element (name of the program) 
# Index 1 contains the second element (name of the text file)
filename = sys.argv[1]

# Print the name of the text file to make sure that we're reading the correct text file
print(filename)

# Open the text file
file_handler = open(filename, "r", encoding="utf8") # The file is opened in READ mode using the "r" parameter

# Create empty lists
all_words = [] # This list will contain all the words in the text file
all_characters = [] # This list will contain all the characters in the text file

# Read the text file into the program one line at a time using a for loop
for one_line in file_handler:
    
    # Add all the characters in the file to the allcharacters list, one line at a time 
    all_characters.extend(one_line)

    # split the line with a regular expression on spaces
    # For example, "Hello, How are you?" is split into six strings: "Hello", ",", "How", "are", "you", "?"
    chunks = re.findall( r'\w+|[^\s\w]+', one_line)

    # If a line is empty, then do not add any words to the allwords list 
    if len(chunks) > 0:
        all_words.extend(chunks)

# This is to check that the contents of the file have been read into the all_characters and all_words lists
# For tiny_file.txt, len(all_characters) prints 20, len(all_words) prints 6
print(len(all_characters))
print(len(all_words))

# PART 1

# Initialize 3 variables to zero - one to count commas, one to count vowels, one to count consonants,
# comma_counter = 0
# vowel_counter = 0
# consonant_counter = 0

# Helper code: The following snippet of code prints each character in the file on a separate line
#for character in all_characters:
#    print(character)

# Iterate over the all_characters list to count the number of commas, the number of vowels, and the number of consonants
# for character in all_characters:
#     if character == ",":
#         comma_counter = comma_counter + 1
#     elif character.isalpha():
#         if character.lower() in "aeiou":
#             vowel_counter = vowel_counter + 1
#         else:
#             consonant_counter = consonant_counter + 1

# # Print the number of commas, vowels, and consonants
# print(f"The file contains {comma_counter} commas.")
# print(f"The file contains {vowel_counter} vowels.")
# print(f"The file contains {consonant_counter} consonants.")

# PART 2
# (a) Count the number of times a user-specified word (the search key) is found in the file and display the count

#Initialize a variable to store the word the user inputs.
search_word = input("Search for a word in this file: ") 
#Initialize a running variable to counter the number of times the word is mentioned as the text is iterated over.
counter = 0

#Iterates of all the words in the text file.
for word in all_words:
    #Check if the word is equal to searchWord (the word the user input)
    if word.lower() == search_word.lower():
        #Then adds the word to the counter if it's a match.
        counter += 1

#Prints how many times the word was found in the file.
print(f'The word "{search_word}" was found {counter} times in the text file.')

# (b) Extend this using a loop to allow the user to keep entering words until the enter "exit" as the search key to exit the program

#Initialize a variable to store the word the user inputs.
search_word = input("Search for a word in this file: ")

#As long as the user doesn't input "exit" or "Exit" the loop will keep going
while search_word.lower() != "exit":
    #Counter is inside the while loop this time so it resets everytime the loop repeats so the numbers from the previous search aren't added.
    counter = 0
    #Iterates of all the words in the text file.
    for word in all_words:
        #Check if the word is equal to searchWord (the word the user input)
        if word.lower() == search_word.lower():
            #Then adds the word to the counter if it's a match.
            counter += 1
    #Prints how many times the word was found in the file.
    print(f'The word "{search_word}" was found {counter} times in the text file.')
    #Ask the user the same question again but in the loop this time so it keeps asking.
    #Also introduce the choice of exitting the program.
    search_word = input('Search for another word OR type "Exit" to exit the program: ')

#If the user enters "exit" or "Exit" then the program will print this and stop running. 
print("Exiting the program.")
