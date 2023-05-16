# initialize a list of high scores
high_scores = [("Player1", 100), ("Player2", 80), ("Player3", 60)]

# function to insert a new score into the list
def insert_score(player_name, score):
    # create a tuple for the new score
    new_score = (player_name, score)
    
    # insert the new score into the list
    for i in range(len(high_scores)):
        if score > high_scores[i][1]:
            high_scores.insert(i, new_score)
            break
    else:
        high_scores.append(new_score)
    
    # keep only the top 10 scores
    high_scores = high_scores[:10]

# test the function with some sample scores
insert_score("Player4", 90)
insert_score("Player5", 110)
insert_score("Player6", 70)

# print the updated list of high scores
print(high_scores)
