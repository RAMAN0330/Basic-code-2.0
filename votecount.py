#opeing file name "votingdata.txt" in read format 
with open("Votingdata.txt",'r') as Votingdata:
    data = Votingdata.read()
data = data.split("\n\n*********************************\n\n")

# Initializing margin , winner vote , winner candidate name
margin_of_votes = [ 0 for i in range(len(data))]     
winner_of_voting = [0 for i in range(len(data))]
winner_candidate = [0 for i in range(len(data))]

# Initializing candidate list , number of valid & invalid vote and voting for each student candidate
candidates = ['A','B','C','D','E','F']
no_of_votes_for_each_student_candidates = [[0,0,0,0,0,0] for i in range(len(data))]
Valid_votes = [0 for i in range(len(data))]
Invalid_votes = [0 for i in range(len(data))]

# Cleaning the data gather from file 
for i in range(len(data)):
    data[i] = data[i].split(',')
    data[i][0] = data[i][0][17:26]
data.pop(79)
for i in range(len(data)):
    data[i][2] = data[i][2].replace("   follows: \n","")

#Intializing the DataFrame variable
register_no = [data[i][0] for i in range(len(data))]
name_of_student = [data[i][1] for i in range(len(data))]
Voting_lists = [data[i][2] for i in range(len(data))]

# counting valid & invalid votes , and number of votes for each candidates
counter = 0
kounter = 0
for vote_list in Voting_lists:
    for vote in range(len(vote_list)):
        if vote_list[vote] in candidates:
            Valid_votes[kounter] += 1
            if vote_list[vote] == 'A':
                no_of_votes_for_each_student_candidates[counter][0] += 1
            elif vote_list[vote] == 'B':
                no_of_votes_for_each_student_candidates[counter][1] += 1
            elif vote_list[vote] == 'C':
                no_of_votes_for_each_student_candidates[counter][2] += 1
            elif vote_list[vote] == 'D':
                no_of_votes_for_each_student_candidates[counter][3] += 1
            elif vote_list[vote] == 'E':
                no_of_votes_for_each_student_candidates[counter][4] += 1
            elif vote_list[vote] == 'F':
                no_of_votes_for_each_student_candidates[counter][5] += 1
        else:
                Invalid_votes[kounter] += 1
        
    kounter += 1
    counter +=1
    
#  Finding winner name and it's vote and the margin by which it won the voting
for student in range(len(no_of_votes_for_each_student_candidates)):
    for results in no_of_votes_for_each_student_candidates[student]:
        # For winner's vote
        winner_of_voting[student]= max(no_of_votes_for_each_student_candidates[student])
        # For finding the margin by which winner won
        sorted_vote_list = sorted(no_of_votes_for_each_student_candidates[student])
        margin_of_votes[student] = sorted_vote_list[5]-sorted_vote_list[4]
        #for finding the name of the winner candidate
        temp_index = no_of_votes_for_each_student_candidates[student].index(max(no_of_votes_for_each_student_candidates[student]))
        winner_candidate[student] = candidates[temp_index]
null = winner_candidate.pop(79)
null = margin_of_votes.pop(79)
null = winner_of_voting.pop(79)

data_set = {"register_no" : register_no,"name_of_student":name_of_student,"Voting_lists":Voting_lists,"winner_of_voting":winner_of_voting,"margin_of_votes":margin_of_votes,"winner_candidate":winner_candidate}


import pandas as pd
election = pd.DataFrame(data_set)

print(election)
