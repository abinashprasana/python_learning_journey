"""
Quiz Game

Author: Abinash Prasana

This is a simple terminal-based quiz game that asks the user multiple-choice
questions, takes input, tracks guesses, and calculates the final score.
"""

# Questions and answers
questions = (
    "1. What is the capital of Canada?",
    "2. Which gas do plants absorb from the atmosphere during photosynthesis?",
    "3. Who directed the movie 'Inception'?",
    "4. What does 'HTTP' stand for?",
    "5. In which year did World War II end?"
)

# Multiple-choice options for each question
options = (
    ('a) Toronto', 'b) Vancouver', 'c) Ottawa', 'd) Montreal'),
    ('a) Oxygen', 'b) Carbon Monoxide', 'c) Nitrogen', 'd) Carbon Dioxide'),
    ('a) Martin Scorsese', 'b) Steven Spielberg', 'c) Christopher Nolan', 'd) James Cameron'),
    ('a) Hypertext Transfer Protocol', 'b) Hightext Transmission Protocol',
     'c) Hyper Transfer Text Protocol', 'd) High Transfer Text Protocol'),
    ('a) 1943', 'b) 1944', 'c) 1945', 'd) 1945')
)

# Correct answers
answers = ("c", "d", "c", "a", "c")
guesses = []
score = 0

# Loop through questions
for question_num in range(len(questions)):
    print("---------------------------")
    print(questions[question_num])
    for option in options[question_num]:
        print(option)

    guess = input("Enter your option (a/b/c/d): ").lower()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer was: {answers[question_num]}")

# Final result
print("---------------------------")
print("           Result          ")
print("---------------------------")
print("Answers: ", " ".join(answers))
print("Guesses: ", " ".join(guesses))

# Calculate percentage score
score_percent = int(score / len(questions) * 100)
print(f"Your score is {score_percent}%")