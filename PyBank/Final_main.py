# Dependencies
import csv
import os


file_to_load = os.path.join("Resources", "budget_data.csv")
print ("budget")


#Variables
totalMonths = 0
totalAmount = 0
totalProfit = 0
greatestIncrease = 0
greatestDecrease = 0
average = 0
monthlyProfitChange = 0
delta_total = 0


with open(file_to_load) as data:
    csvreader = csv.reader(data, delimiter=',')
    header = next(csvreader)
    firstRow = next(csvreader)
    
    firstPLvalue = firstRow[1]
    totalAmount = int(firstRow[1])

    
    for row in csvreader:
        totalMonths = totalMonths + 1
        totalAmount = totalAmount + int(row[1])
        nextPLvalue = row[1]
        monthlyProfitChange = int(nextPLvalue) - int(firstPLvalue)
        delta_total = delta_total + monthlyProfitChange
        
        if greatestIncrease <  monthlyProfitChange: 
            greatestIncrease = monthlyProfitChange
            greatestIncreaseMonth = row[0]
        elif greatestDecrease >  monthlyProfitChange: 
            greatestDecrease = monthlyProfitChange
            greatestDecreaseMonth = row[0]

        firstPLvalue = row[1]
        
average = round(delta_total/totalMonths, 2) # calculated after for loop for final values

totalMonths = totalMonths + 1 # offset by one month after average determined 

       
print(f'Financial Analysis')
print(f'------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: ${totalAmount}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})')
print(f'Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})')