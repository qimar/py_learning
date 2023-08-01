def new_game():
    
    
    
    
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("---------------------------")
        print(key)
        for i  in options[question_num-1]:
            print(i)
            

            

# --------------------------------------------------
def check_answer():
    pass
# --------------------------------------------------
def display_score():
    pass
# --------------------------------------------------
def play_again():
    pass
# --------------------------------------------------    


questions = (
    "Who created python?: ", "A",
    "What year was python created?: ", "B",
    "Python is tributed to which comedy group?: ", "C",
    "Is the earth round?: ", "A"
)

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True", "B. False", "C. sometimes", "D. What's earth?"]]

new_game()


