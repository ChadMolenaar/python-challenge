# Dependencies
import csv
import os


file_to_load = os.path.join("Resources", "budget_data.csv")
print ("budget")

# variables
totalAmount = 0
totalMonths = 0
Profit = 0
Losses = 0
valuePrevious = 0
valueCurrent = 0
valueChange = 0
Average =0

with open(file_to_load) as data:
 
    csvReader = csv.reader(data,delimiter=',')
    
    header = next(csvReader)
    
    for row in csvReader:
       
        totalMonths = totalMonths +1
       
        totalAmount = totalAmount + int(row[1])
        

    print("Total Months:", totalMonths)
    print("Total Amount:", totalAmount)

with open(file_to_load) as data:
 
    csvReader = csv.reader(data,delimiter=',')
    
    header = next(csvReader)
    
        for header in csvReader:

        #int(totalMonths[0::],totalAmount[1::])

        #print(totalMonths,totalAmount,totalAmount-totalMonths)
        
        #count[totalAmount-totalMonths] +=1

        #Profit = valuePrevious + int(row[1])
        #Losses = valueCurrent + int(row[1])
        #change = valueCurrent/valuePrevious
        #Sum = sum(numbers) 
        #averageChange = totalAmount/totalMonths  
        #print (average) 

with open(file_to_load) as data:
    header = next(csvReader)  #->next row 
    firstRow = next(csvReader) # -> jan-2010 row 2
    previousPLvalue = firstRow[1] # just the profit/losses '867884'
    previousChange = 0
    #for every row in the file
    for row in csvReader: # starts in 3 
        #goes through the for loop second time -  what does it do in row 4? (B4 -B3)
        #remember in excel the formula is "=B3-B2"
        

        currentPLvalue = row[1] # just the profit/losses
        #/-currentChange = int(currentPLvalue) - int(previousPLvalue) # it isn't B3 it hasn't change it is still b2
        if currentPLvalue > previousvalue:
            greatestIncrease = currentChange
        else:
            greatestIncrease = previousChange3

    csvReader = csv.reader(data,delimiter=',')
    
    header = next(csvReader)
    
    firstRow = next(csvReader) 
    secondRow = next(csvReader)
    thirdRow = next(csvReader)
    
    profitChange = int(secondRow[1])-int(firstRow[1])
    

    print(header)
    print(firstRow)
    print(secondRow)
    print("profitChange:", profitChange)
    print("valueChange2:", valueChange)

    if valueChange1 > valueChange2:
        
        greatestIncrease = valueChange1
    
    else:
        
        greatestIncrease = valueChange2
    
    print("Value Change2:", valueChange2)

    #
def budgetAudit(budgetData):
    global totalMonths
    global totalAmount
    global netDifference
    global greatestIncrease
    global greatestDecrease
    global average
    global monthlyProfitChange
    
    totalMonths = totalMonths + 1
    
    totalAmount = totalAmount + int(row[1])

for row in csvreader: 
        
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for b in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[b+1]-total_profit[b])