#Import CSV
import csv
import os

#Assign a variable for the file to load and the path to the file
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable for the file to write and the path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total votes to zero
total_votes = 0

#Determine all candidates
candidate_options = []
#Create a dictionary for candidate + vote count
candidate_votes = {}

#Winner variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results file and read it
with open(file_to_load) as election_data:

    #Read & analyze the data here
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    #Print each row in the CSV
    for row in file_reader:
        #Calculate total number of votes
        total_votes +=1
        #Determine all candidates
        candidate_name = row[2]
        #Add unique candidate names to the list & track their votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    #Iterate through candidate list, retrieve vote count & calculate % of vote
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine the winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

#Print results
#print(total_votes)

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    #Write some data to the file
#    txt_file.write("Counties in the Election\n")
#    txt_file.write("-------------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")



#Calculate number of votes per candidate
#Calculate winner