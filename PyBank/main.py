# Create a script that contains the following:
print("Financial Analysis")
print("-------------------------")

import csv

with open('PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    fields = next(csvfile)

    date = []
    pl = []
    changes = []
    
    for rows in csvreader:
        date.append(rows[0])
        pl.append(int(rows[1]))

#The total number of months included in the dataset
    total_months = len(date)
    print(f"Total Months: {total_months}")

#The net total amount of "Profit/Losses" over the entire period
    net_total = sum(pl)
    print(f"Total: ${net_total}")

#The changes in "Profit/Losses" over the entire period
    for i in range(1, total_months):
        change = pl[i] - pl[i-1]
        changes.append(change)

#The average of those changes
    average_change = sum(changes) / len(changes)
    round_ac = round(average_change, 2)
    print(f"Average change: ${round_ac}")

#The greatest increase in profits (date and amount) over the entire period
    greatest_incr = max(changes)
    gi_date = date[changes.index(greatest_incr) + 1]
    print(f"Greatest Increase in Profits: {gi_date} (${greatest_incr})")

#The greatest decrease in profits (date and amount) over the entire per
    greatest_decr = min(changes)
    gd_date = date[changes.index(greatest_decr) + 1]
    print(f"Greatest Decrease in Profits: {gd_date} (${greatest_decr})")

#export txt file
    
    file = open("/Users/meichelyoingco/Downloads/Starter_Code 3:19/PyBank/PyBank_Results.txt", "w")
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average change: ${round_ac}\n")
    file.write(f"Greatest Increase in Profits: {gi_date} (${greatest_incr})\n")
    file.write(f"Greatest Decrease in Profits: {gd_date} (${greatest_decr})\n")
