print('Welcome to the Quiz Game!')

questions = {
    "What is the name of my beautiful girlfriend?:": "emerson",
    "What is my favorite fast food?:": "chipotle",
    "Where do I work?:": "dutch bros"
}

while True:
    playing = input("Would you like to play?: ").lower().strip()

    if playing in ('y', 'yes'):
        score = 0
        question_num = 1

        for question, answer in questions.items():
            print(f'Question {question_num} of {len(questions)}')
            user_answer = input(question).lower().strip()

            if user_answer == answer:
                print('Correct!')
                score += 1
            else:
                print('Incorrect!')

            question_num += 1

        print(
            f"Thank you for playing! You're final score was ({score}/{len(questions)})!")
        break

    elif playing in ('n', 'no'):
        print("Come back soon!")
        break

    else:
        print("That is not an option, please try again!")
