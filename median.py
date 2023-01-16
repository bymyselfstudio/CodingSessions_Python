def getNumbers():
  numbers = []
  for i in range(4):
    number = float(input("Input a number: "))
    numbers.append(number)
  return numbers


def addAllNumbers(numbers):
  sum = 0
  for i in range(len(numbers)):
    sum += numbers[i]
  return sum


def median(sum, numbers):
  divisor = len(numbers)
  return sum / divisor
  

def main():
  numbers = getNumbers() 
  sum = addAllNumbers(numbers) 
  average = median(sum, numbers)
  print(f"Average value of {numbers} is {average}")
    

if __name__ == "__main__":
  main()