DEBUG = False


def check_neighbours(matrix: list[list[str]], i: int, j: int) -> bool:
    if i-1 >= 0 and i-1 < len(matrix) and j >= 0 and i < len(matrix[i]):
        DEBUG and print(matrix[i-1][j])
        if matrix[i-1][j] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    if i-1 >= 0 and i-1 < len(matrix) and j-1 >= 0 and j-1 < len(matrix[i]):
        DEBUG and print(matrix[i-1][j-1])
        if matrix[i-1][j-1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    if i >= 0 and i < len(matrix) and j-1 >= 0 and j-1 < len(matrix[i]):
        DEBUG and print(matrix[i][j-1])
        if matrix[i][j-1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    if i+1 >= 0 and i+1 < len(matrix) and j-1 >= 0 and j-1 < len(matrix[i]):
        DEBUG and print(matrix[i+1][j-1])
        if matrix[i+1][j-1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    if i+1 >= 0 and i+1 < len(matrix) and j >= 0 and j < len(matrix[i]):
        DEBUG and print(matrix[i+1][j])
        if matrix[i+1][j] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    if i+1 >= 0 and i+1 < len(matrix) and j+1 >= 0 and j+1 < len(matrix[i]):
        DEBUG and print(matrix[i+1][j+1])
        if matrix[i+1][j+1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    if i >= 0 and i < len(matrix) and j+1 >= 0 and j+1 < len(matrix[i]):
        DEBUG and print(matrix[i][j+1])
        if matrix[i][j+1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    if i-1 >= 0 and i-1 < len(matrix) and j+1 >= 0 and j+1 < len(matrix[i]):
        DEBUG and print(matrix[i-1][j+1])
        if matrix[i-1][j+1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
            return True
    return False


if __name__ == "__main__":
    print("hat is the sum of all of the part numbers in the engine schematic?")
    saved_numbers = []
    with open(f"3/{'1/test' if DEBUG else 'input'}.txt") as f:
        matrix = [list(row.strip()) for row in f.readlines()]
        isNum = False
        isSave = False
        for i, row in enumerate(matrix):
            num = []
            for j, item in enumerate(row):
                DEBUG and print("row: ", i, "col:", j, "item:", item)
                try:
                    num.append(int(item))
                    if check_neighbours(matrix, i, j):
                        isSave = True
                    if len(row)-1 == j:
                        if isSave:
                            if num != []:
                                saved_numbers.append(num)
                        num = []
                        isSave = False
                except ValueError:
                    if isSave:
                        if num != []:
                            saved_numbers.append(num)
                    num = []
                    isSave = False
        DEBUG and print("raw saved_numbers: ", saved_numbers)
        saved_numbers = [int("".join(map(str, n))) for n in saved_numbers]
        DEBUG and print(saved_numbers)
        print(f"Sum of all of the part numbers: {sum(saved_numbers)}")
