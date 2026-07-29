import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0
# This starts the try-except logic
        while tries < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        # NOTICE: This is aligned with the 'while' loop, NOT inside the 'try'
        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")



    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")
    if level == 1:
        return random.randint(0,9)
    else:
        start = 10 ** (level - 1)
        end = (10 ** level) - 1
        return random.randint(start,end)


if __name__ == "__main__":

    main()

