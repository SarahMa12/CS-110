This repository contains some of my mini python projects I created in my CS 110 class at University of San Francisco.

## Code descriptions

### Image Operation 
Transforms images to flip, blur, rotate, grayscale, swap corners, sharpen, edge detection, and scaling larger.

### Inventory Management
Allows a user to keep track of inventory. They can add a new item, delete an item, or update an item. All of this data collected from the user is written to a csv file. Previous data is also read from the csv file.

### Shopping Cart
Asks user how many pounds of raspberries, strawberries, apples, and mangoes they want to buy. Calculates the total and asks the user to enter an amount of money. If not enough, asks user for more until they enter an amount that is enough. Calculates change that the user needs. Allows user to shop again.

### Stocks API
Uses an API that gets live stocks data. Combined HTML and Python using Flask and coded a website that allows a user to enter the symbol of a stock and click on checkboxes for whether they want to see the opening price, low price, high price, and/or current price of the stock. This works locally as well as through this link through Glitch (https://smstocksapi.glitch.me) for other users/computers to use. 

### Text Analyzer
Part 1: Takes a file input from the command line and uses the text in the file to calculate the number of commas, vowels, and consonants. 
Part 2: Asks user what word to search of in the file and returns the number of times that word appears in the file.


### TMDB CSV
Uses the API of The Movie Database. Takes a movie input from the user and searches The Movie Database for the movie the user entered and if it exists list all of the movies that have what the user enters and lists the movie name, id, popularity, and release date. Additionally it writes this data into a csv file. 
