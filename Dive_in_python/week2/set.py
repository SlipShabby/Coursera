import random
randomm_set = set()

while True:
    new_number = random.randint(1,10)
    if new_number in randomm_set:
        break

    randomm_set.add(new_number)

    print(len(randomm_set)+1)