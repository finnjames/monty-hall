import random as r

def play(repetitions: int, switch: bool) -> int:
    wins = 0
    for _ in range(repetitions):
        correct = r.randint(0,2)
        guess = r.randint(0,2)

        def find_door(*doors):
            return r.choice(list(filter(lambda a: a not in doors, [0,1,2])))
        shown = find_door(guess, correct)
        if switch:
            guess = find_door(guess, shown)
            # print(f"{correct=} {shown=} {guess=}")
        if guess == correct:
            wins += 1

    return wins

def main():
    REPETITIONS = 100000
    wins = play(REPETITIONS, switch=False)
    print(f"KEEP:   {wins} wins after {REPETITIONS} games ({wins/REPETITIONS})")
    wins = play(REPETITIONS, switch=True)
    print(f"SWITCH: {wins} wins after {REPETITIONS} games ({wins/REPETITIONS})")


if __name__ == "__main__":
    main()
