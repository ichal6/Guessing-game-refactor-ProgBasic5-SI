import random


def check_guess_number(end_of_range):
    COUNT_NUMBER_TO_GUESS = 10
    list_random_int = []
    iteration = 0
    while iteration < COUNT_NUMBER_TO_GUESS:
        list_random_int.append(random.randint(1, end_of_range))
        iteration += 1

    command = "Enter an integer from 1 to {}: ".format(str(end_of_range))
    for index_of_number in range(COUNT_NUMBER_TO_GUESS):
        guess = int(input(command))
        while list_random_int[index_of_number] != guess:
            if guess < list_random_int[index_of_number]:
                print("guess is low")
                guess = int(input(command))
            elif guess > list_random_int[index_of_number]:
                print("guess is high")
                guess = int(input(command))
        print("you guessed it!")


first_max_range = 99
second_max_range = 49

check_guess_number(first_max_range)
check_guess_number(second_max_range)
