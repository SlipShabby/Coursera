import random

number = random.randint(0,101)

while True:
    answer = input("Please, enter a number: ")
    if not answer or answer == "exit":
        break
    if not answer.isdigit():
        print("Please, enter a digit: ")

    user_answer = int(answer)

    if user_answer > number:
        print("The number is smaller than yours")
    elif user_answer < number:
        print("The number is greater than your number:")
    else:
        print("You win!")
        break
