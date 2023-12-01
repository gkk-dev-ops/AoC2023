def firstNum(arr):
    for i in range(len(arr)):
        if arr[i].isdigit():
            return int(arr[i])
    else:
        raise Exception("No number found in array")

def lastNum(arr):
    for i in range(len(arr)):
        if arr[len(arr)-1 - i].isdigit():
            return int(arr[len(arr)-1 - i])
    else:
        raise Exception("No number found in array")

if __name__ == "__main__":
    with open("./1/input.txt", "r") as f:
        numbers: list[int] = []
        for line in f:
            numbers.append(firstNum(line) * 10 + lastNum(line))
        print("What is the sum of all of the calibration values?")
        print("It's: ", sum(numbers))