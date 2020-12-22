# Dependencies
import csv
import os
file_to_load = os.path.join("Resources", "budget_data.csv")
print ("budget")
#Variables
totalMonths = 0
totalAmount = 0
totalProfit = []
netDifference = [] 
greatestIncrease = 0
greatestDecrease = 0
average = []
monthlyProfitChange = []
with open(file_to_load) as data:
    csvreader = csv.reader(data, delimiter=',')
    header = next(csvreader)
    firstRow = next(csvreader) 
    # lets get the first PL value and save it
    firstPLvalue = firstRow[1]
    #goes through every row in the csv file. it ends in the last row
    for row in csvreader:
        totalMonths = totalMonths + 1
        totalAmount = totalAmount + int(row[1])
        nextPLvalue = row[1]
        monthlyProfitChange = int(nextPLvalue) - int(firstPLvalue)
        if greatestIncrease >  monthlyProfitChange: #true
            # our new greatestIncrease value will be the same as the old value
            greatestIncrease = greatestIncrease
            greatestIncreaseMonth = row[0]
            # 0
        else: # for example if monthlyProfitChange = 662642
            # our new greatestIncrease value will be the same value as monthlyProfitChange = 662642
            greatestIncrease = monthlyProfitChange
            greatestIncreaseMonth = row[0]
        if greatestDecrease <  monthlyProfitChange: 
            greatestDecrease = greatestDecrease
        else: 
            greatestDecrease = monthlyProfitChange
        #it is at the end to save the previous value
        firstPLvalue = row[1]
#         greatestIncrease = max(monthlyProfitChange)
#         greatestDecrease = min(monthlyProfitChange)
#         greatestIncrease = monthlyProfitChange.index(max(monthlyProfitChange)) + 1
#         greatestDecrease = monthlyProfitChange.index(min(monthlyProfitChange)) + 1
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {totalMonths}')
print(f'totalAmount: {totalAmount}')
print(f'greatestIncrease: {greatestIncrease}')
print(f'greatestIncreaseMonth: {greatestIncreaseMonth}')
print(f'greatestDecrease: {greatestDecrease}')
# print(f'average: {average}')