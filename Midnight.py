import math

# note: does not work with all numbers, since no complex numbers are used!

def midnight_formula(a: float, b: float, c: float, decimal_places: int) -> tuple[float]:
    if a == 0:
        print("'a' cannot be 0!")
        return 0
    else:
        x1 = ((-b) + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
        x1 = round(x1, decimal_places)
        x2 = ((-b) - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
        x2 = round(x2, decimal_places)
    return x1, x2


def main() -> None:
    a = -1
    b = 5
    c = -3
    
    try:
        result = midnight_formula(a, b, c, 4)
        print(f"\nResult:\na = {a} | b = {b} | c = {c}\n"
              + f"\nx1 = {result[0]}\nx2 = {result[1]}\n")
    except:
        print("An error occured. Try again!")


if __name__ == "__main__":
    main()
