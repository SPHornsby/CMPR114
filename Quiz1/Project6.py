# Create a program that will ask the user to enter a grade score (4 scores) 
# and output the letter grade associated with the average grade. 
# Then using a while loop, if the average is greater than 100, 
# inform the user to re-enter the 4 scores.

NUMBER_OF_SCORES = 4

def get_scores():
    scores = []
    i = 1
    while i <= NUMBER_OF_SCORES:
        score = int(input(f'Enter score {i}:'))
        scores.append(score)
        i += 1
    return scores

def get_letter_grade(average_grade):
    if average_grade >= 90:
        return 'A'
    if average_grade >= 80:
        return 'B'
    if average_grade >= 70:
        return 'C'
    if average_grade >= 60:
        return 'D'
    else:
        return 'F'

def main():
    scores = get_scores()
    
    while sum(scores)/NUMBER_OF_SCORES > 100:
        print('Please re-enter scores')
        scores = get_scores()
    average_grade = sum(scores)/NUMBER_OF_SCORES
    letter_grade = get_letter_grade(average_grade)
    print(f'The average grade is {average_grade} for a letter grade of: {letter_grade}')

main()