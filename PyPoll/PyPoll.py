# Modules
import os
import csv

# Set path for file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Initialize Variables for Vote Counts for each candidate
Khanvotes = 0
Correyvotes = 0
Livotes = 0
OTooleyvotes = 0
TotalVotes = 0

# Initialize Variables for Vote Percentage for each candidate
Khanvotes = 0
KhanPercent = 0
CorreyPercent = 0
LiPercent = 0
OTooleyPercent = 0

# Open CSV file based on Path information in csvpath variable
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    csv_header = next(csvreader)
    
    # Loop through file until End of File
    for row in csvreader:
        # Add to total Votes across all candidates
        TotalVotes = TotalVotes + 1

        # Check for Candidate Name to add to their individual totals

        if (row[2] == "Khan"):
            Khanvotes = Khanvotes + 1
        elif (row[2] == "Correy"):
            Correyvotes = Correyvotes + 1
        elif (row[2] == "Li"):
            Livotes = Livotes + 1
        elif (row[2] == "O'Tooley"):
            OTooleyvotes = OTooleyvotes + 1
    
    # Once File is completely read
    # Compute Percentage for each Candidate
    KhanPercent = Khanvotes/TotalVotes
    CorreyPercent = Correyvotes/TotalVotes
    LiPercent = Livotes/TotalVotes
    OTooleyPercent = OTooleyvotes/TotalVotes

    # Compare Individual Candidate Totals to Find out Overall Winner
    if Khanvotes > Correyvotes and Khanvotes > Livotes and Khanvotes > OTooleyvotes:
        Winner = "Khan"
    elif Correyvotes > Khanvotes and Correyvotes > Livotes and Correyvotes > OTooleyvotes:
        Winner = "Correy"
    elif Livotes > Khanvotes and Livotes > Correyvotes and Livotes > OTooleyvotes:
        Winner = "Li"
    elif OTooleyvotes > Khanvotes and OTooleyvotes > Correyvotes and OTooleyvotes > Livotes:
        Winner = "O'Tooley"
    
    # Display the Results of Total Votes and Each Individual Candidates' Percentage and Total Votes
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(TotalVotes))
    print("-------------------------")
    print("Khan : " + str(round(KhanPercent*100,2)) +"%  ("+str(Khanvotes) +")")
    print("Correy : " + str(round(CorreyPercent*100,2)) +"% (" + str(Correyvotes) +")")
    print("Li : " + str(round(LiPercent*100,2)) +"%"+ " ("+str(Livotes) +")")
    print("O'Tooley : " + str(round(OTooleyPercent*100,2)) +"%"+ " ("+str(OTooleyvotes) +")")
    print("-------------------------")
    print("Winner: " + Winner)
    print("-------------------------")

    # Write the Results of Total Votes and Each Individual Candidates' Percentage and Total Votes to a Text File
    TextFile = open(r".\PyPoll\PyPoll_Output.txt", "w")
    
    TextFile.write("Election Results")
    TextFile.write("\n")
    TextFile.write("-------------------------")
    TextFile.write("\n")
    TextFile.write("Total Votes: " + str(TotalVotes))
    TextFile.write("\n")
    TextFile.write("-------------------------")
    TextFile.write("\n")
    TextFile.write("Khan : " + str(round(KhanPercent*100,2)) +"%  ("+str(Khanvotes) +")")
    TextFile.write("\n")
    TextFile.write("Correy : " + str(round(CorreyPercent*100,2)) +"% (" + str(Correyvotes) +")")
    TextFile.write("\n")
    TextFile.write("Li : " + str(round(LiPercent*100,2)) +"%"+ " ("+str(Livotes) +")")
    TextFile.write("\n")
    TextFile.write("O'Tooley : " + str(round(OTooleyPercent*100,2)) +"%"+ " ("+str(OTooleyvotes) +")")
    TextFile.write("\n")
    TextFile.write("-------------------------")
    TextFile.write("\n")
    TextFile.write("Winner: " + Winner)
    TextFile.write("\n")
    TextFile.write("-------------------------")
    TextFile.close()