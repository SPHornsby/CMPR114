# Create a program that will ask the user to enter 5 scores 
# (use 60, 70, 80, 90) 
# then sum the scores, and then average the scores as well.
# Expected outcomes is: sum = 300, average = 75
# I think this is supposed to be 4 scores. 4x75 = 300

def sum_of_four_scores():
    scores = []
    for i in range(4):
        score = int(input(f'Enter score {i+1}: '))
        scores.append(score)
    total = sum(scores)
    print(f'sum = {total}, average = {total/len(scores)}')

sum_of_four_scores()
