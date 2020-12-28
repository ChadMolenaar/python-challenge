# Dependencies
import csv
import os


file_to_load = os.path.join("Resources", "election_data.csv")
print ("election")

# variables
totalVotes = 0
Candidate = []
totalVotesWon = 0
votesWon = 0

#Total Votes Cast
with open(file_to_load) as data:
 
    csvReader = csv.reader(data,delimiter=',')
    
    header = next(csvReader)
    
    for row in csvReader:
        
        totalVotes = totalVotes +1
    
        totalVotesWon = votes_Won + int(row[2])

def print_percentages(votes_won):
    
    votes = int(votes_won[0])
    name = str(candidate[2])
    
    votes_won = votes + candidate

    # Win percent 
    win_percent = (votes_won / total_candidate) * 100

    # If the percentage is greater than 0, print candidate
    print(f'Total Votes:', totalVotes)
    print("Votes Won:", votesWon)
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {str(win_percent)}")
 

