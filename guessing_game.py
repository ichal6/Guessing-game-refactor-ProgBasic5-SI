import random
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
for i in range(10):
    g = int(input("Enter an integer from 1 to 99: "))
    while list_random_int[i] != g:
        if g < list_random_int[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > list_random_int[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
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
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while list_random_int[i] != g:
        if g < list_random_int[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > list_random_int[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
