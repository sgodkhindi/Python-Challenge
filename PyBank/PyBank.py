# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Initialize Variables for Total Months, Total Profit & Loss, High Profit and Low Profit
totalmonths = 0
totalPNL = 0

highprofit = 0
lowprofit = 0

currprofit = 0
nextprofit = 0

profitdiff1 = 0
profitdiff2 = 0

allPNL = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip Header
    csv_header = next(csvreader)
    # Store the 1st Row
    firstrow = next(csvreader)

    currprofit = float(firstrow[1])
    # Update Count of the Months and also Add the 1st Row's Profit/Loss into the total
    totalmonths = totalmonths + 1
    totalPNL = totalPNL + float(firstrow[1])

    # Store the 2nd Row
    nextrow = next(csvreader)
    nextprofit = float(nextrow[1])
    # Store the Month Name
    currmonth = nextrow[0]
    # Update Count of the Months and also Add the 1st Row's Profit/Loss into the total
    totalmonths = totalmonths + 1
    totalPNL = totalPNL + float(nextrow[1])
    
    # Compute Profit Difference Between 2nd Row and 1st Row
    profitdiff1 = nextprofit - currprofit

    # Append the Profit Difference to a List as an item for later Average
    allPNL.append(profitdiff1)

    # Store the Profit Difference to temporary Variables for later comparisons
    highprofit = profitdiff1
    highmonth = currmonth
    
    lowprofit = profitdiff1
    lowmonth = currmonth
   
    # Assign the 2nd Rows Profit to a variable for comparison
    currprofit = nextprofit
    
    # Read the file until End of File
    for row in csvreader:
        # Store the current row data into variables
        nextprofit = float(row[1])
        currmonth = row[0]

        #Compute the Profit Difference between the current row and previous row
        profitdiff2 = nextprofit - currprofit

        # Update Count of the Months and also Add the 1st Row's Profit/Loss into the total     
        totalmonths = totalmonths + 1
        totalPNL = totalPNL + float(row[1])

        # if Profit Difference between the current row and previous row is HIGHER than previous profit difference Store the details to HighProfit / HighMonth
        if profitdiff2 > profitdiff1 and profitdiff2 > highprofit:
            highprofit = profitdiff2
            highmonth = currmonth
           
        # if Profit Difference between the current row and previous row is LOWER than previous profit difference Store the details to LowProfit / LowMonth    
        elif profitdiff2 < profitdiff1 and profitdiff2 < lowprofit:
            lowprofit = profitdiff2
            lowmonth = currmonth
        
        # Save Current Row details before reading the next row
        allPNL.append(profitdiff2)
        currprofit = nextprofit
        profitdiff1 = profitdiff2
    
    # Display the Computed Values on Screen
    print ("Total: "+str(totalPNL))
    print ("Total Months: "+ str(totalmonths))
    print ("Greatest Increase in Profits: " + highmonth +" ($"+ str(round(highprofit,0))+ ")")
    print ("Greatest Decrease in Profits: " + lowmonth +" ($"+ str(round(lowprofit,0))+ ")")
    print ("Average Change: "+ str(round(sum(allPNL)/len(allPNL),2)))
    
    # Store the computed values into a text tfile
    TextFile = open(r".\PyBank\PyBank_Output.txt", "w")
    
    TextFile.write("Total: "+str(totalPNL))
    TextFile.write("\n")
    TextFile.write("Total Months: "+ str(totalmonths))
    TextFile.write("\n")
    TextFile.write("Greatest Increase in Profits: " + highmonth +" ($"+ str(round(highprofit,0))+ ")")
    TextFile.write("\n")
    TextFile.write("Greatest Decrease in Profits: " + lowmonth +" ($"+ str(round(lowprofit,0))+ ")")
    TextFile.write("\n")
    TextFile.write("Average Change: "+ str(round(sum(allPNL)/len(allPNL),2)))
    TextFile.close()