def getNumbersAmount() -> int:
    amount = input("How many numbers will be in the list? ")
    return int(amount)


def getNumbers(amount: int) -> list[float]:
    numbers = []
    for i in range(amount):
        numbers.append(float(input(f"Input {i+1}. number: ")))
    return numbers


def getNumbersSum(numbers: list[float]) -> float:
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum


def getMedian(sum: float, numbers: list[float]) -> float:
    divisor = len(numbers)
    return sum / divisor


def main():
    amount = getNumbersAmount()
    numbers = getNumbers(amount)
    sum = getNumbersSum(numbers)
    average = getMedian(sum, numbers)
    print(f"Average value of {numbers} is {average:.3f}")


if __name__ == "__main__":
    main()
