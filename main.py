print('Welcome to the Quiz Game!')

play = input("Would you like to play?: ").lower()
correct = 0

if play == 'yes':

    print("What is the name of my beautiful girlfriend?:")
    a1 = input().lower()
    if a1 == 'emerson':
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")

    print("What is my favorite fast food?:")
    a2 = input().lower()
    if a2 == 'chipotle':
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")

    print("Where do I work?:")
    a3 = input().lower()
    if a3 == 'dutch bros':
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")

    print(f"You got a score of {correct}/3")

else:
    print("Have an amazing day!")
