import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
total = 0
khan = 0
correy = 0
li = 0
otooley = 0
mostvotes = 0
winner = "blank"


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    next(csvreader)

    for row in csvreader:

        total = total + 1
        
        if row[2] == "Khan":
            khan = khan + 1

        if row[2] == "Correy":
            correy = correy + 1
        
        if row[2] == "Li":
            li = li + 1

        if row[2] == "O'Tooley":
            otooley = otooley + 1

if khan > mostvotes:
    mostvotes = khan
    winner = "Khan"

if correy > mostvotes:
    mostvotes = correy
    winner = "Correy"

if li > mostvotes:
    mostvotes = li
    winner = "Li"

if otooley > mostvotes:
    mostvotes = otooley
    winner = "O'Tooley"

file = open("output.txt", "w")

file.write("Election Results\n")
file.write("-------------------------\n")
file.write("Total Votes: " + str(total) + "\n")
file.write("-------------------------\n")
file.write("Khan: " + str(round(((khan/total)*100), 1)) + "%" + " (" + str(khan) + ")\n")
file.write("Correy: " + str(round(((correy/total)*100), 1)) + "%" + " (" + str(correy) + ")\n")
file.write("Li: " + str(round(((li/total)*100), 1)) + "%" + " (" + str(li) + ")\n")
file.write("O'Tooley: " + str(round(((otooley/total)*100), 1)) + "%" + " (" + str(otooley) + ")\n")
file.write("-------------------------\n")
file.write("Winner: " + winner + "\n")
file.write("-------------------------")
file.close()

print("")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total))
print("-------------------------")
print("Khan: " + str(round(((khan/total)*100), 1)) + "%" + " (" + str(khan) + ")")
print("Correy: " + str(round(((correy/total)*100), 1)) + "%" + " (" + str(correy) + ")")
print("Li: " + str(round(((li/total)*100), 1)) + "%" + " (" + str(li) + ")")
print("O'Tooley: " + str(round(((otooley/total)*100), 1)) + "%" + " (" + str(otooley) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")