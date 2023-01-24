def getLetters(words: str) -> list[str]:
    letters = []
    for letter in words:
        letters.append(letter)
    return letters

def getAsciiCode(letters: list[str]) -> list[int]:
    asciiCodes = []
    for i in range(len(letters)):
        correspondingAsciiCode = ord(letters[i])
        asciiCodes.append(correspondingAsciiCode)
    return asciiCodes

def swapToLower(asciiCode: list[int]):
    for i in range(len(asciiCode)):
        if asciiCode[i] >= 65 and asciiCode[i] <= 90:
            print(chr(asciiCode[i] + 32), end="")
        else:
            print(chr(asciiCode[i]), end="")

def swapToUpper(asciiCode: list[int]):
    for i in range(len(asciiCode)):
        if asciiCode[i] >= 97 and asciiCode[i] <= 122:
            print(chr(asciiCode[i] - 32), end="")
        else:
            print(chr(asciiCode[i]), end="")

def main():
    words = "HeLlo WoRLd"
    letters = getLetters(words)
    asciiCode = getAsciiCode(letters)
    swapToUpper(asciiCode)
    print()
    swapToLower(asciiCode)

if __name__ == "__main__":
    main()
