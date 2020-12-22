# Dependencies
import csv
import os


file_to_load = os.path.join("Resources", "election_data.csv")
print ("election")

# variables
totalVotes = 0

#Total Votes Cast
with open(file_to_load) as data:
 
    csvReader = csv.reader(data,delimiter=',')
    
    header = next(csvReader)
    
    for row in csvReader:
        
        totalVotes = totalVotes +1
        
    print("Total Votes:", totalVotes)
    

#Candidates who Recieved Votes
file_to_load = os.path.join("Resources", "election_data.csv")
print ("election")

# variables
totalVotes = 0
Candidate = input
totalVotesWon = 0

with open(file_to_load) as data:
 
    csvReader = csv.reader(data,delimiter=',')
    
    header = next(csvReader)
    
    for row in csvReader:

       
        totalVotesWon = votesWon + str(row[2])

print("Votes Won:", votesWon)

def print_percentages(votes_won):
    
    votes = int(votes_won[0])
    name = str(candidate[2])
    
    votes_won = votes + candidate

    # Win percent 
    win_percent = (votes_won / total_candidate) * 100

    # If the percentage is greater than 0, print candidate
    
    print(f"Stats for {name}")
    print(f"WIN PERCENT: {str(win_percent)}")
 

