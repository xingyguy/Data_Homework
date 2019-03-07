import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
total = 0
length = 0
difference = 0
previousrow = 0
cumulative_difference = 0
greatestprofit_month = "blank"
greatestprofit_value = 0
greatestdecrease_month = "blank"
greatestdecrease_value = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    next(csvreader)

    for row in csvreader:

        difference = int(row[1]) - previousrow
        
        total = total + int(row[1])

        previousrow = int(row[1])

        length = length + 1
        
        if length > 1:

            cumulative_difference = cumulative_difference + difference

            if difference > greatestprofit_value:

                greatestprofit_value = difference

                greatestprofit_month = row[0]

            if difference < greatestdecrease_value:

                greatestdecrease_value = difference

                greatestdecrease_month = row[0]


file = open("output.txt", "w")

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write("Total Months: " + str(length) + "\n")
file.write("Total: $" + str(total) + "\n")
file.write("Average Change: $" + str(cumulative_difference/(length - 1)) + "\n")
file.write("Greatest Increase in Profits: " + greatestprofit_month + " ($" + str(greatestprofit_value) + ")\n")
file.write("Greatest Decrease in Profits: " + greatestdecrease_month + " ($" + str(greatestdecrease_value) + ")")
file.close()

print("")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(length))
print("Total: $" + str(total))
print("Average Change: $" + str(cumulative_difference/(length - 1)))
print("Greatest Increase in Profits: " + greatestprofit_month + " ($" + str(greatestprofit_value) + ")")
print("Greatest Decrease in Profits: " + greatestdecrease_month + " ($" + str(greatestdecrease_value) + ")")