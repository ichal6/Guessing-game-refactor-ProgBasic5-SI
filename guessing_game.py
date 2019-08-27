import random
COUNT_NUMBER_TO_GUESS = 10
list_random_int = []
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
list_random_int.append(random.randint(1, 99))
for index_of_number in range(COUNT_NUMBER_TO_GUESS):
    guess = int(input("Enter an integer from 1 to 99: "))
    while list_random_int[index_of_number] != guess:
        if guess < list_random_int[index_of_number]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 99: "))
        elif guess > list_random_int[index_of_number]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

list_random_int = []
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
list_random_int.append(random.randint(1, 49))
for index_of_number in range(COUNT_NUMBER_TO_GUESS):
    guess = int(input("Enter an integer from 1 to 49: "))
    while list_random_int[index_of_number] != guess:
        if guess < list_random_int[index_of_number]:
            print("guess is low")
            guess = int(input("Enter an integer from 1 to 49: "))
        elif guess > list_random_int[index_of_number]:
            print("guess is high")
            guess = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
