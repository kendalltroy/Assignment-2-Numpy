import csv #imports csv reader
import os
import numpy as np #imports numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #creates directory for file
details_file = os.path.join(BASE_DIR, 'stats.csv')  #gets file from correct folder

rows = [] #creates empty list to read rows in file
with open(details_file, newline='', encoding='utf-8') as f: #opens data as f
    reader = csv.reader(f) #reads file properly
    next(reader)  # skip header row
    for row in reader:
        rows.append(row) #appends each row to the list of rows

# keep everything as objects (strings)
data = np.array(rows, dtype=object) #opens data in numpy

#defines a function to calculate averages/accuracy with arguments for data, first column (numerator), second column (denominator), player column (identified as column 3), and the top 100.
def top_accuracy(data, made_col, attempted_col, player_col=3, top_n=100):
    made = data[:, made_col].astype(float) #determines numerator column and converts to float
    attempted = data[:, attempted_col].astype(float) #determines denominator column and converts to float
    accuracy = np.divide(made,attempted,out=np.zeros_like(made),where=attempted != 0) #calculates the accuracy by dividing the two columns where the denominator column does not = 0
    acc_dict = {} # creates an empty dictionary to store players and their averages/accuracies
    for player, pct in zip(data[:, player_col], accuracy): #iterates through each player and their percentage and adds to dictionary
        acc_dict[player] = pct
    return sorted(acc_dict.items(), key=lambda x: x[1], reverse=True)[:top_n] #returns the dictionary, sorted from most to least accurate and determines the top n (100) players

while True: #begins loop to ask users for what stats they want to view
    choice = input('Would you like to view the top 100 in: \n 1) field goal accuracy \n 2) three point accuracy \n 3) free throw accuracy \n 4) avg points per minute \n 5) shooting accuracy \n 6) avg # of blocks per game \n 7) avg # of steals per game\n')
    print(choice) #asks users what stats they want
    if choice == '1': #if choice = 1, top_accuracy is called with columns 7 (fg made) and 8 (fg attempted) as arguments
        print('Top 100 players for field goal accuracy:')
        results = top_accuracy(data, 7, 8)
        for player, pct in results: #prints results nicely
            print(player, pct)

        break
    elif choice == '2': #if choice = 2, top_accuracy is called with columns 9 (3 pointers made) and 10 (3 pointers attempted) as arguments
        print('Top 100 players for three point accuracy:')
        results = top_accuracy(data, 9, 10)
        for player, pct in results: #prints results nicely
            print(player, pct)

        break
    elif choice == '3': #if choice = 3, top_accuracy is called with columns 11 (free throws made) and 12 (free throws attempted) as arguments
        print('Top 100 players for free throw accuracy:')
        results = top_accuracy(data, 11, 12)
        for player, pct in results: #prints results nicely
            print(player, pct)

        break
    elif choice == '4': #if choice = 4, top_accuracy is called with columns 21 (total points) and 6 (# of mins played) as arguments
        print('Top 100 players in avg. points per minute:')
        results = top_accuracy(data, 21, 6)
        for player, pct in results: #prints results nicely
            print(player, pct)

        break
    elif choice == '5': #if choice = 5, all shooting accuracies are called and added to their respective dictionaries
        fg = dict(top_accuracy(data, 7, 8, top_n=len(data)))
        tp = dict(top_accuracy(data, 9, 10, top_n=len(data)))
        ft = dict(top_accuracy(data, 11, 12, top_n=len(data)))
        overall_dict = {} #a dictionary for overall accuracy is defined
        for player in fg: #iterates through all players
            accuracies = [] #defines an empty list for all accuracies
            #appends all player accuracies to the list
            if player in fg:
                accuracies.append(fg[player])
            if player in tp:
                accuracies.append(tp[player])
            if player in ft:
                accuracies.append(ft[player])
            if accuracies:  #avoids empty lists
                overall_dict[player] = sum(accuracies) / len(accuracies) #defines each key:value pair as player : total accuracies/the amount of accuracies (overall shooting accuracy)
        top_100_overall = sorted(overall_dict.items(),key=lambda x: x[1],reverse=True)[:100] #sorts overall accuracies by best to worst and identifies the top 100
        print('Top 100 players in overall shooting accuracy:') #prints top 100 players for overall shooting nicely
        for player, pct in top_100_overall:
            print(player, pct)

        break
    elif choice == '6': #if choice = 6, top_accuracy is called with columns 20 (# of blocks) and 5 (# of games) as arguments
        print('Top 100 players in avg. # of blocks per game:')
        results = top_accuracy(data, 20, 5)
        for player, pct in results: #prints results nicely
            print(player, pct)

        break
    elif choice == '7': #if choice = 7, top_accuracy is called with columns 19 (# of steals) and 5 (# of games) as arguments
        print('Top 100 players in avg. # of steals per game:')
        results = top_accuracy(data, 19, 5)
        for player, pct in results:
            print(player, pct)

        break
    else: #prompts user to enter a valid choice if invalid input is entered and keeps program running
        print('Please enter a valid choice.')