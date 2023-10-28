#initialising the player's (W,X,Y,Z) 
data_txt = "BBBBDDDAEBBBBDDDAEBBBBDDDCEBBBBDDDCEBBBBDDDCFBBBBDDDCFBBBBDDDCFBBBBDDACFBBBBDDACFBBBBDDACFBBBBDDACRBBBBDDACRBBBBDDACRBBBBDDACRBBBBDDACRBBBBDDAERBBBBDDAERBBBBDDAERBBBBDDAEZBBBBDDAEZBBBDDDAEBBBBDDDAEBBBBDDDAEBBBBDDDCEBBBBDDDCFBBBBDDDCFBBBBDDDCFBBBBDDDCFBBBBDDACFBBBBDDACFBBBBDDACFBBBBDDACRBBBBDDACRBBBBDDACRBBBBDDACRBBBBDDAERBBBBDDAERBBBBDDAERBBBBDDAEZBBBBDDAEZBBBBDDAE"
len_of_data = len(data_txt)
factor_check = len_of_data/4
if isinstance(factor_check,float) == True:
    factor_check = round(factor_check)
    W = data_txt[:factor_check]
    X = data_txt[factor_check:factor_check*2]
    Y = data_txt[factor_check*2:factor_check*3]
    Z = data_txt[factor_check*3:len_of_data]
    

set_each_data = [W,X,Y,Z]  #list contain palyer data for further analysis
set_each_data_str = ["w","X","Y","Z"]  #list containing name of eacb player for recognation
no_of_valid_by_each_player = [[0,0,0,0,0,0] for i in range(len(set_each_data))]  # take vale for valid throws for each count
candidates = ['A','B','C','D','E','F'] 

counter = 0
score = 0 
winner_steps = []
for data in set_each_data:
    no_of_times = 0
    target = True
    for value in range(len(data)): 
        no_of_times += 1
        if data[value] in candidates:
            if data[value] == 'A':
                no_of_valid_by_each_player[counter][0] += 1
            elif data[value] == 'B':
                   no_of_valid_by_each_player[counter][1] += 2
            elif data[value] == 'C':
                no_of_valid_by_each_player[counter][2] += 3
            elif data[value] == 'D':
                no_of_valid_by_each_player[counter][3] += 4
            elif data[value] == 'E':
                no_of_valid_by_each_player[counter][4] += 5
            elif data[value] == 'F':
                no_of_valid_by_each_player[counter][5] += 6
                
        if target == True:
            if sum(no_of_valid_by_each_player[counter]) >= 50:
                target = False
                winner_steps.append(no_of_times)
                
    counter += 1
    
win_lis = winner_steps.copy()
cpy_set_each_data_str = set_each_data_str.copy()

winner = win_lis.pop(win_lis.index(min(winner_steps)))
cpy_data_str = cpy_set_each_data_str.pop(winner_steps.index(min(winner_steps)))

    
if winner == min(winner_steps):
    print("joint winner's score are  {} , {} with minimum number steps of {}".format(set_each_data_str[winner_steps.index(min(winner_steps))],cpy_set_each_data_str[win_lis.index(min(win_lis))],winner))   
else:    
    print("the winner is {} by achieving target of 50 in {} steps".format(set_each_data_str[winner_steps.index(min(winner_steps))],min(winner_steps)))
     
print("Total score of each player are W : {} , X : {} , Y : {} , Z : {} ".format(sum(no_of_valid_by_each_player[0]),sum(no_of_valid_by_each_player[1]),sum(no_of_valid_by_each_player[2]),sum(no_of_valid_by_each_player[3])))