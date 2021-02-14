#Import CSV
import csv
import os

#Assign a variable for the file to load and the path to the file
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable for the file to write and the path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results file and read it
with open(file_to_load) as election_data:

    #Read & analyze the data here
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV
    #for row in file_reader:
    #    print(row)
    #Perform analysis
    #print(election_data)


# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
    #Write some data to the file
#    txt_file.write("Counties in the Election\n")
#    txt_file.write("-------------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")

#Determine all candidates
#Calculate number of votes per candidate
#Calculate total number of votes
#Calculate winner