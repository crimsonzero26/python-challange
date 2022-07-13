import os
import csv

election_data_csv = os.path.join("Resources","election_data.csv")

count = 0
candidates = []
unique_candidate = []
vote_count = []
vote_percentage = []

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        count = count + 1
        candidates.append(row[2])
    for x in set(candidates):
        unique_candidate.append(x)
        y = candidates.count(x)
        vote_count.append(y)
        z = (y/count)*100
        vote_percentage.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
 
print("")
print("Election Results")   
print("")
print("-------------------------")
print("")
print("Total Votes :" + str(count))    
print("")
print("-------------------------")
print("")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str("{:.3f}".format(vote_percentage[i])) +"% (" + str(vote_count[i])+ ")")
print("")
print("-------------------------")
print("")
print("The winner is: " + winner)
print("")
print("-------------------------")

with open('analysis/analysis.txt', 'w') as text:
    text.write("\nElection Results\n\n")
    text.write("-------------------------\n\n")
    text.write("Total Vote: " + str(count) + "\n\n")
    text.write("-------------------------\n\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str("{:.3f}".format(vote_percentage[i])) +"% (" + str(vote_count[i]) + ")\n\n")
    text.write("-------------------------\n\n")
    text.write("The winner is: " + winner + "\n\n")
    text.write("-------------------------\n\n")