import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass
a = random.randint(1,level)

while True:
    try:
        n = int(input("Guess: "))
        if n > 0:
            if n < a:
             print("Too small! ")
            elif n > a:
             print("Too large!")
            else:
             print("Just right! ")
             break
    except ValueError:
        pass
