DEBUG = False
COLORS = ["red", "green", "blue"]


def game_parser(line: str) -> [int, int, int, int]:
    id = line[0:line.index(":")].replace("Game ", "")
    data = line[line.index(":")+1:].strip()
    max_red, max_green, max_blue = 0, 0, 0
    for color in COLORS:
        for game in data.split(";"):
            if color in game:
                sub = game[:game.index(color)]
                try:
                    comma = sub[::-1].index(",")
                    num = int(sub[::-1][:comma][::-1])
                except:
                    num = int(game[:game.index(color)].strip())
                if color == "red":
                    max_red = max(max_red, num)
                elif color == "green":
                    max_green = max(max_green, num)
                elif color == "blue":
                    max_blue = max(max_blue, num)
                DEBUG and print(color, num)
    return [id, max_red, max_green, max_blue]


if __name__ == "__main__":
    print("Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?")
    print("TLDR: 12 red cubes, 13 green cubes, and 14 blue cubes")
    id_sum = 0
    with open("2/input.txt") as f:
        for line in f.readlines():
            [id, max_red, max_green, max_blue] = game_parser(line)
            DEBUG and print([id, max_red, max_green, max_blue])
            if (max_red <= 12) and (max_green <= 13) and (max_blue <= 14):
                id_sum += int(id)
    print("Sum of ids: ", id_sum)
