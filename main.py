print('Welcome to the Quiz Game!')

score = 0
questions = {
    "What is the name of my beautiful girlfriend?:": "emerson",
    "What is my favorite fast food?:": "chipotle",
    "Where do I work?:": "dutch bros"
}

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

print(f"Thank you for playing! You're final score was ({score}/3)!")
