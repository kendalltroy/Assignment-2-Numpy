# Assignment-2-Numpy
# Purpose of the Program
The purpose of this program is to analyze basketball player statistics and determine the top 100 players in the following: field goal accuracy, three point accuracy, free throw accuracy, average points per minute, shooting accuracy, and average number of blocks and steals per game. 

# Input
The program takes a csv file that contains data about basketball players. It then asks for a user input between 1-7. Each digit asks for the following information:  
1) field goal accuracy 
 2) three point accuracy 
 3) free throw accuracy 
 4) avg points per minute 
 5) shooting accuracy 
 6) avg # of blocks per game 
 7) avg # of steals per game

# Expected Output
The program is expected to give an output that is relevant to what the user entered. There should be a string that notes what the data analysis is. For example, "Top 100 players in avg. # of blocks per game:". After that, 100 lines will appear of the top 100 players in the respective category and their relevant stats. 

# Type of Execution
File input: reads players and their data from the respective csv file.
Data processing: converts RAW data to a numpy array and performs analysis
Function-based execution: uses a function to compute certain stats based on user inputted metrics
Interactivity: Prompts user for input to determine what type of analysis to perform
Conditional Execution: executes a function with different arguments depending on the user's input
Output/Display: Nicely prints out the top 100 ranked players with their relevant stats

# Possible Improvements
Code for the analysis on overall shooting could be made more efficient. It is a little long currently. A second function that focuses on overall shooting accuracy could be made to make code more organized and readable.
