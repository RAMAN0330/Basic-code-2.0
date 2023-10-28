#initialising the player's (W,X,Y,Z) 
data_txt = "CCCDDABFQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCDDABEQCCCDABEFCCCDABEFCCCDDABFQCCDDABEQCCCDABEFCCCDABEFCCCDAAEFZCCDDABEQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCCDABEFCCCDABEFCCCDABEFZCCDDABEQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCCDABEFCCCDABEFCCCDABEFZCCDDABFQCCDDABEQCCCDABEFCCCDABEFCCCDAABFQCCDDABEQCCCDABEQCCCDABEFCCCDABEF"
commentary = open("commentary.txt","w")

candidates = ['A','B','C','D','E','F']
each_player_count = [0 for i in range(len(candidates))]  # take vale for each playuer count
 
no_of_times = 0 
score = 0 
winner_steps = []
maximum = 0
for value in range(len(data_txt)): 
    no_of_times += 1
    if data_txt[value] in candidates:
        if data_txt[value] == 'A':
            each_player_count[0] += 1
        elif data_txt[value] == 'B':
            each_player_count[1] += 1
        elif data_txt[value] == 'C':
            each_player_count[2] += 1
        elif data_txt[value] == 'D':
            each_player_count[3] += 1
        elif data_txt[value] == 'E':
            each_player_count[4] += 1
        elif data_txt[value] == 'F':
            each_player_count[5] += 1
    winner_steps.append(candidates[each_player_count.index(max(each_player_count))])
    if len(winner_steps) < 2:
        commentary.write("After {} vote is counted {} is initiating the lead with {} vote \n".format(no_of_times,winner_steps[0],max(each_player_count)))
    else:
        if winner_steps[-1] != winner_steps[-2]:
            commentary.write("After {} vote is counted {} is now leading with {} votes \n".format(no_of_times,winner_steps[-1],max(each_player_count)))
commentary.write("In the end winner is {} with vote count {} ".format(winner_steps[-1], max(each_player_count)))
commentary.close()