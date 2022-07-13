import os
import csv

budget_data_csv = os.path.join("Resources","budget_data.csv")

profit = []
profit_losses_changes = []
date = []
 
total_profit = 0
total_change_profits = 0
monthly_change_profits = 0
count = 0

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:    
        if count > 0:

            count = count + 1 
            date.append(row[0])
            profit.append(row[1])
            total_profit = total_profit + int(row[1])
            final_profit = int(row[1])
            monthly_change_profits = final_profit - initial_profit
            profit_losses_changes.append(monthly_change_profits)

            total_change_profits = total_change_profits + monthly_change_profits
            initial_profit = final_profit
            
            greatest_increase_profits = max(profit_losses_changes)
            greatest_decrease_profits = min(profit_losses_changes)

            increase_date = date[profit_losses_changes.index(greatest_increase_profits)]
            decrease_date = date[profit_losses_changes.index(greatest_decrease_profits)]

        else:

            count = count + 1 
            date.append(row[0])
            profit.append(row[1])
            total_profit = total_profit + int(row[1])
            final_profit = int(row[1])
            monthly_change_profits = final_profit - int(row[1])
            profit_losses_changes.append(monthly_change_profits)

            total_change_profits = total_change_profits + monthly_change_profits
            initial_profit = final_profit
            
            greatest_increase_profits = max(profit_losses_changes)
            greatest_decrease_profits = min(profit_losses_changes)

            increase_date = date[profit_losses_changes.index(greatest_increase_profits)]
            decrease_date = date[profit_losses_changes.index(greatest_decrease_profits)]
    print("")  
    print("Financial Analysis")
    print("") 
    print("----------------------------")
    print("") 
    print("Total Months: " + str(count))
    print("") 
    print("Total Profits: " + "$" + str(total_profit))
    print("") 
    print("Average Change: " + "$" + str(int(total_change_profits/(count-1))))
    print("") 
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("") 
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("") 
    print("----------------------------")

with open("analysis/analysis.txt", "w") as text:
    text.write("\n"+"Financial Analysis"+ "\n\n")
    text.write("----------------------------\n\n")
    text.write("Total Months: " + str(count) + "\n\n")
    text.write("Total Profits: " + "$" + str(total_profit) +"\n\n")
    text.write("Average Change: " + '$' + str(int(total_change_profits/(count-1))) + "\n\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n\n")
    text.write("----------------------------\n\n") 