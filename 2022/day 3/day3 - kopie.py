with open("C:\\Users\\EC\\Downloads\\the maps\\vinegar\\knowledge-skill and trade\\adventofcode challenge\\2022\\day 3\\data.txt", "r") as file:
    map = file.read()
    A = map.split('\n') 

B = [item.split() for item in A]
print(B)

#rounds = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
rounds = B

A, B, C, X, Y, Z = 1, 2, 3, 1, 2, 3 

win, draw, lose = 6, 3, 0

player_1 = A, B, C
player_2 = X, Y, Z

score_map = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}
total = 0

for p1, p2 in rounds:
    p1_val = score_map[p1]
    p2_val = score_map[p2]
    if p1_val == p2_val:
        total += p2_val + draw
    elif (p2_val - p1_val) % 3 == 1:
        total += p2_val + win
    else:
        total += p2_val + lose

print(total)  

#now there is an additional step on top of the existing code of rock-papper-scissors. 
# the player with X needs to lose, Y needs to draw and Z needs to win.

# --- New Rule: X/Y/Z indicate desired outcome ---
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
total_outcome = 0

for p1, outcome in rounds:
    p1_val = score_map[p1]
    
    if outcome == 'X':  
        p2_val = (p1_val - 2) % 3 + 1
    elif outcome == 'Y':  
        p2_val = p1_val
    elif outcome == 'Z':  
        p2_val = p1_val % 3 + 1

    total_outcome += p2_val + outcome_score[outcome]

print("Outcome-based scoring:", total_outcome)