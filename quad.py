def getQuadDimensions() -> list[str]:
    userInput = input(
        "Type the dimensions in comma separated order [Length,Width,Height]: ")
    dimensions = userInput.split(',')
    return dimensions

def convertToFloat(dimensions: list[str]) -> list[float]:
    dimensionsAsFloat = []
    for dimension in dimensions:
        dimensionsAsFloat.append(float(dimension))
    return dimensionsAsFloat

def getVolume(convertedDimensions: list[float]) -> float:
    volume = 1
    for dimension in range(len(convertedDimensions)):
        volume *= convertedDimensions[dimension]
    return volume

def getSurface(convertedDimensions: list[float]) -> float:
    surface, ground, side, front = 0, 0, 0, 0
    length = convertedDimensions[0]
    width = convertedDimensions[1]
    height = convertedDimensions[2]
    ground = length * width
    side = length * height
    front = width * height
    surface = (ground + side + front) * 2
    return surface

def getSpaceDiagonal(convertedDimensions: list[float]) -> float:
    spaceDiagonal = 0
    length = convertedDimensions[0]
    width = convertedDimensions[1]
    height = convertedDimensions[2]
    spaceDiagonal = (length ** 2 + width ** 2 + height ** 2) ** 0.5
    return spaceDiagonal

def main() -> None:
    dimensions = getQuadDimensions()
    convertedDimensions = convertToFloat(dimensions)
    volume = round(getVolume(convertedDimensions), 3)
    surface = round(getSurface(convertedDimensions), 3)
    spaceDiagonal = round(getSpaceDiagonal(convertedDimensions), 3)
    print(
        f"Dimensions: Length {convertedDimensions[0]} | Width {convertedDimensions[1]} | Height {convertedDimensions[2]}")
    print(f"Volume: {volume}")
    print(f"Surface: {surface}")
    print(f"Space diagonal: {spaceDiagonal}")

if __name__ == "__main__":
    main()
