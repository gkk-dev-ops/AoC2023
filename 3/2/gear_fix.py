DEBUG = False


def check_neighbours(matrix: list[list[str]], i: int, j: int) -> (bool, int, int):
    if i-1 >= 0 and i-1 < len(matrix) and j >= 0 and i < len(matrix[i]):
        DEBUG and print(matrix[i-1][j])
        if matrix[i-1][j] == "*":
            return (True, i-1, j)
    if i-1 >= 0 and i-1 < len(matrix) and j-1 >= 0 and j-1 < len(matrix[i]):
        DEBUG and print(matrix[i-1][j-1])
        if matrix[i-1][j-1] == "*":
            return (True, i-1, j-1)
    if i >= 0 and i < len(matrix) and j-1 >= 0 and j-1 < len(matrix[i]):
        DEBUG and print(matrix[i][j-1])
        if matrix[i][j-1] == "*":
            return (True, i, j-1)
    if i+1 >= 0 and i+1 < len(matrix) and j-1 >= 0 and j-1 < len(matrix[i]):
        DEBUG and print(matrix[i+1][j-1])
        if matrix[i+1][j-1] == "*":
            return (True, i+1, j-1)
    if i+1 >= 0 and i+1 < len(matrix) and j >= 0 and j < len(matrix[i]):
        DEBUG and print(matrix[i+1][j])
        if matrix[i+1][j] == "*":
            return (True, i+1, j)
    if i+1 >= 0 and i+1 < len(matrix) and j+1 >= 0 and j+1 < len(matrix[i]):
        DEBUG and print(matrix[i+1][j+1])
        if matrix[i+1][j+1] == "*":
            return (True, i+1, j+1)
    if i >= 0 and i < len(matrix) and j+1 >= 0 and j+1 < len(matrix[i]):
        DEBUG and print(matrix[i][j+1])
        if matrix[i][j+1] == "*":
            return (True, i, j+1)
    if i-1 >= 0 and i-1 < len(matrix) and j+1 >= 0 and j+1 < len(matrix[i]):
        DEBUG and print(matrix[i-1][j+1])
        if matrix[i-1][j+1] == "*":
            return (True, i-1, j+1)
    return (False, 0, 0)


if __name__ == "__main__":
    print("hat is the sum of all of the part numbers in the engine schematic?")
    saved_numbers = []
    with open(f"3/{'2/test' if DEBUG else 'input'}.txt") as f:
        matrix = [list(row.strip()) for row in f.readlines()]
        isNum = False
        isSave = False
        star_pos = None
        for i, row in enumerate(matrix):
            num = []
            for j, item in enumerate(row):
                DEBUG and print("row: ", i, "col:", j, "item:", item)
                try:
                    num.append(int(item))
                    if check_neighbours(matrix, i, j)[0]:
                        isSave = True
                        star_pos = check_neighbours(matrix, i, j)[
                            1], check_neighbours(matrix, i, j)[2]
                    if len(row)-1 == j:
                        if isSave:
                            if num != []:
                                saved_numbers.append([num, star_pos])
                        num = []
                        isSave = False
                except ValueError:
                    if isSave:
                        if num != []:
                            saved_numbers.append([num, star_pos])
                    num = []
                    isSave = False
        DEBUG and print("raw saved_numbers: ", saved_numbers)
        for num in saved_numbers:
            new = ""
            for n in num[0]:
                new += str(n)
            num[0] = int(new)

        d = {}
        gear_sum = 0
        for num in saved_numbers:
            if d.get(num[1], False):
                d[num[1]] = d.get(num[1]) * num[0]
                gear_sum += d[num[1]]
            else:
                d[num[1]] = num[0]
            DEBUG and print(num)
        DEBUG and print("dict: ", d)
        print(f"Gear is: {gear_sum}")
