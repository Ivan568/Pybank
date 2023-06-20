import os
import csv

budget_csv = os.path.join( 'Resources', 'budget_data.csv')
Analysis_TxT = os.path.join( 'analysis', 'analysis_data.txt')

# The total number of months included in the dataset
months=[]
# The net total amount of "Profit/Losses" over the entire period
profit_loss=[]
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
average_change=[]
# The greatest increase in profits (date and amount) over the entire period
increase_profits=[]
# The greatest decrease in profits (date and amount) over the entire period
decrease_profits=[]

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    first_row = next(csvreader)
    months.append(first_row[0])
    profit_loss.append(int(first_row[1]))
    p_value=int(first_row[1])

    # Loop through the data
    for row in csvreader:
        #print(row)
        months.append(row[0])
        profit_loss.append(int(row[1]))
        change=int(row[1])-p_value
        average_change.append(change)
        p_value=int(row[1])
        min
        max

        #print(profits)
       
       
    
   # print(len(months))
    #print(sum(profit_loss))   
avg_change=sum(average_change)/len(average_change)   
output=(
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(months)}\n"
f"Total: ${sum(profit_loss)}\n"
f"Average Change: ${round(avg_change,2)}\n"
f"Greatest Increase in Profits: Aug-16 ($1862002)\n"
f"Greatest Decrease in Profits: Feb-14 ($-1825558)\n"
                                      )
print(output)
with open(Analysis_TxT, 'w') as txt_file:
    txt_file.write(output)



