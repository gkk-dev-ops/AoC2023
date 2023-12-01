DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}


def firstNum(arr):
    for i in range(len(arr)):
        for key in DIGITS.keys():
            if key in arr[:i]:
                return DIGITS[key]
        if arr[i].isdigit():
            return int(arr[i])
    else:
        raise Exception("No number found in array")


def lastNum(arr):
    for i in range(len(arr)):
        for key in DIGITS.keys():
            if key in arr[len(arr)-1 - i:]:
                return DIGITS[key]
        if arr[len(arr)-1 - i].isdigit():
            return int(arr[len(arr)-1 - i])
    else:
        raise Exception("No number found in array")


if __name__ == "__main__":
    with open("./1/input.txt", "r") as f:
        numbers: list[int] = []
        for line in f:
            numbers.append(firstNum(line) * 10 + lastNum(line))
        print(numbers)
        print("What is the sum of all of the calibration values?")
        print("It's: ", sum(numbers))
