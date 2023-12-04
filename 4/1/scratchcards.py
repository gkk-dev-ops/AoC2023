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
    sum_of_points = 0
    with open(f"4/{'/1/test' if TEST_DATA else 'input'}.txt") as f:
        for line in f.readlines():
            [id, game_num, validation_num] = game_parser(line)
            points_on_a_card = 0
            for i in range(len(game_num)):
                if game_num[i] in validation_num and points_on_a_card == 0:
                    points_on_a_card += 1
                elif game_num[i] in validation_num and points_on_a_card > 0:
                    points_on_a_card *= 2
            DEBUG and print(f"Card {id} is worth {points_on_a_card} points")
            sum_of_points += points_on_a_card
    print(f"There's: {sum_of_points}")
