import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')  
print(election_csv)
# Method 2: Improved Reading using CSV module

def vote_percentage(candidate_votes, total_votes):
    candidate_votepercent = {}
    for candidate in candidate_votes.keys():    
        Candidate_percent = round((candidate_votes[candidate]/Total_Votes * 100), 6)
        candidate_votepercent.update({candidate:Candidate_percent})
    return candidate_votepercent

with open(election_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidate_list= []

    Khan_Vote = 0
    Correy_Vote = 0
    Li_Vote = 0
    OTooley_Vote = 0
    Total_Votes = 0

    #Total_Votes = (Khan_Vote + Correy_Vote + Li_Vote + OTooley_Vote)
    # Read each row of data after the header
    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        if row[2] != " ":
            Total_Votes += 1
        
        if row[2] == "Khan":
            Khan_Vote += 1
        elif row[2] == "Correy":
            Correy_Vote += 1
        elif row[2] == "Li":
            Li_Vote +=1
        elif row[2] == "O'Tooley":
            OTooley_Vote +=1


    print(candidate_list)
    Candidate_vote_dict = {"Khan": Khan_Vote, "Correy": Correy_Vote, "Li": Li_Vote, "O'Tooley": OTooley_Vote}

    Final_VoteResults = vote_percentage(Candidate_vote_dict,Total_Votes)
    
    print("--------------------------------------")
    print("Election Results")
    print("--------------------------------------")
    print("Total Votes:", (Total_Votes))
    print("--------------------------------------")
    for candidate in Candidate_vote_dict.keys():
        print(f'{candidate}: {Final_VoteResults[candidate]}% ({Candidate_vote_dict[candidate]})')
    print("--------------------------------------")
    Winner = max(Candidate_vote_dict, key=Candidate_vote_dict.get)
    print("Winner:" " " + (Winner))
    print("--------------------------------------")
   

  


