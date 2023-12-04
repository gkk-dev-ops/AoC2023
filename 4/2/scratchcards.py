from collections import defaultdict
TEST_DATA = False
DEBUG = False


def game_parser(line: str) -> [int, list[int], list[int]]:
    game_separator = line.index(":")
    num_separator = line.index("|")
    id = line[0:game_separator].replace("Card ", "")
    game_num = line[game_separator +
                    1:num_separator].strip().split(" ")
    game_num = [int(x) for x in game_num if x != ""]
    validation_num = line[num_separator + 1:].strip().split(" ")
    validation_num = [int(x) for x in validation_num if x != ""]
    DEBUG and print(id)
    DEBUG and print("Game number: ", game_num)
    DEBUG and print("Validation number: ", validation_num)
    return [id, game_num, validation_num]


if __name__ == "__main__":
    print("How many points are they worth in total?")
    p1 = 0
    N = defaultdict(int)
    with open(f"4/{'/2/test' if TEST_DATA else 'input'}.txt") as f:
        all_cards = []
        for i, line in enumerate(f.readlines()):
            [id, game_num, validation_num] = game_parser(line)
            all_cards.append([game_num, validation_num])
            N[i] += 1
            val = len(set(game_num) & set(validation_num))
            for j in range(val):
                DEBUG and print("d:", N[i+1+j], "plus", N[i])
                N[i+1+j] += N[i]
    print(f"There's: {sum(N.values())}")


# Solution by: https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/4.py
