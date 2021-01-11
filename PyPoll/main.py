#Dependencies
import os
import csv
#File to Load
file_to_load = os.path.join("Resources", "election_data.csv")
#Variables
candidates = {}
#Open File
with open(file_to_load) as data:
    
    csvReader = csv.reader(data,delimiter=',')
    header = next(csvReader)
    for row in csvReader:

        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1

        total = candidates.values()
        total_votes = sum(total)
            
        list_candidates = candidates.keys()
            
        votes_per = [f'{(x/total_votes)*100:.3f}%' for x in candidates.values()]
        
        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        winner
        


print('Election Results')

print('--------------------------------')

print(f'Total votes: {int(total_votes)}')

print('---------------------------------')
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate} , {votes_per[i]} , {(vote)}') 
    i+=1
    
print('------------------------------')

print(f'Winner: {winner}')

print("------------------------------")

output_path = os.path.join("Analysis", "main.txt")
with open(output_path, 'w') as txt:
    txt.write(f'Election Results\n'
    f'------------------\n'
    f'Total votes: {int(total_votes)}\n')
    #f'{candidate} , {votes_per[i]} , {(vote)}\n'
    i = 0
    for candidate, vote in candidates.items():
        txt.write(f'{candidate} , {votes_per[i]} , {(vote)}\n')
        i+=1
    txt.write(f'Winner: {winner}\n'
    f'------------------------------\n')