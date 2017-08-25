import random
import sys

question = 0 # holds question number
answer = 0  # holds the answer
playerInput = 0 # holds the players answer
score = 0  # gives score
limit = 4   #sets the limit of questions
min_range = 0 # holds range
max_range = 10# holds min range


'''
Easy,Medium,and Hard Fuctions:
Behavior: Creates random math questions, according to each levels.
Input: The variables (question) and (answer) make random questions within the given range.
Output: The fuctions return the Questions and Answers.
'''

def easy(): 
    max_range = 5
    n1 = random.randint(min_range,max_range) 
    n2 = random.randint(min_range,max_range) 
    n3 = random.randint(min_range,max_range)
    question = 'Solve, %d + %d + %d = ' %(n2, n1, n3) 
    answer = n1 + n2 + n3
    return question, answer 

def medium(): 
    max_range = 10
    n1 = random.randint(min_range,max_range) 
    n2 = random.randint(min_range,max_range) 
    n3 = random.randint(min_range,max_range)
    question = 'Solve, %d + %d - %d = ' %(n2, n1, n3) 
    answer = n1 + n2 - n3
    return question, answer 

def hard(): 
    max_range = 5
    n1 = random.randint(min_range,max_range) 
    n2 = random.randint(min_range,max_range) 
    n3 = random.randint(min_range,max_range)
    question = 'Solve, %d * %d * %d = ' %(n2, n1, n3) 
    answer = n1 * n2 * n3
    return question, answer 

'''
play_game Fuction:
Behavior: This fuction prompts user to choose the level of the Game.
Input: There are three arguments; Easy, Medium, and Hard, else typo and try again.
The user is propted to choose level.
Output: When level is chosen the we run the play_() fuction, pulling the respective level questions.
'''
def play_game():  #this prompts the user to choose what level to play
    difficulty_level = raw_input("Choose your Difficulty level, Easy, Medium, Hard: ")   
    if difficulty_level == 'Easy':
        print ('Alright lets do the ' + difficulty_level + ' level!')
        current_question, current_answer = easy()
        play_(current_question,current_answer,difficulty_level)
    elif difficulty_level == 'Medium':
        print('Alright lets do the ' + difficulty_level + ' level!')
        current_question, current_answer = medium()
        play_(current_question,current_answer,difficulty_level)
    elif difficulty_level == 'Hard':
        print('Alright lets do the ' + difficulty_level + ' level!')
        current_question, current_answer = hard()
        play_(current_question,current_answer,difficulty_level)
    else: 
        print"Didn't catch that, try again...", "\n"
        play_game()

'''
play_() Fuction:
Behavior: Runs the Game.
Input: While the number of questions is less then the limit the game continues to run.
If the players answer is correct then the player is promted with another randomly generated question.
If players answer is wrong the player is promted to try again.
Output: Finally the game prints players score, and then runs the game_options() fuction.
'''

def play_(current_question,current_answer,difficulty_level): 
    question = 0
    score = 0
    limit = 4
    while True: 
        try:
            if question >= limit:
                break
            playerInput = int(raw_input(current_question))
            if int(playerInput) == (current_answer):
                print ("Correct!\n")
                score += 1
                question += 1
                question_generators = [easy(), medium(), hard()]
                generator_index = ['Easy', 'Medium', 'Hard'].index(difficulty_level)
                current_question, current_answer = question_generators[generator_index] 
            else:
                if playerInput != current_answer:
                    print ("Incorrect! Please try again!\n")
                    question += 1  
        except ValueError:
            print("Invalid input...")   
    print("Alright, you scored, " , score , " out of 4!")
    game_options()

'''
game_options() Function:
Behavior: When the game ends gives the player the option to play again or exit.
Input: While True, the player is promted with two choices, either to exit or to replay.
Output: If player plays again a new set of numbers are generated.
'''

def game_options(): #this loop gives you options after finishing the game
    score = 0
    exit_game = 1
    play_again = 2
    while True:
        try:
            choose = int(input('''

            Enter '1' to exit game,
            Enter '2' to replay game,
            : '''))
        except ValueError:
            print("Invalid input...")
        if choose == exit_game: #exits
            sys.exit()
        elif choose == play_again: #play again
            n1 = random.randint(min_range,max_range) 
            n2 = random.randint(min_range,max_range) 
            n3 = random.randint(min_range,max_range)
            play_game() 
        else:
            print('''Didn't catch that, try again.''')
            print()
            game_options()

play_game()



