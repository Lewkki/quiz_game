import random

print('Welcome to the Quiz Game!')

questions = {
    "What is the name of my beautiful girlfriend?:": "emerson",
    "What is my favorite fast food?:": "chipotle",
    "Where do I work?:": "dutch bros"
}

while True:
    playing = input("Would you like to play?: ").lower().strip()
    num_of_q = input("How many questions do you want to answer?: ")

    if not num_of_q.isdigit():
        print("Please enter a number.")
        continue

    num_of_q_int = int(num_of_q)

    if num_of_q_int > len(questions):
        print("There are not enough questions, try again.")
        continue

    if playing in ('y', 'yes'):
        score = 0
        question_num = 1

        keys = list(questions.keys())
        random.shuffle(keys)
        selected_questions = keys[:num_of_q_int]

        for question in selected_questions:
            answer = questions[question]

            print(f'Question {question_num} of {num_of_q_int}')
            user_answer = input(question).lower().strip()

            if user_answer == answer:
                print('Correct!')
                score += 1
            else:
                print('Incorrect!')

            question_num += 1

        print(
            f"Thank you for playing! You're final score was ({score}/{num_of_q_int})!")
        break

    elif playing in ('n', 'no'):
        print("Come back soon!")
        break

    else:
        print("That is not an option, please try again!")
