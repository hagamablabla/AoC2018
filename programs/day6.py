import math

def main():
    # Get raw input
    file = open("../inputs/day6.txt","r")
    raw_input = file.readlines()
    # DEBUG INPUT
    # raw_input = ["1, 1\n", "1, 6\n", "8, 3\n", "3, 4\n", "5, 5\n", "8, 9\n"]
    file.close()

    coordinates = getCoords(raw_input)
    start = getMinBorder(coordinates)
    end = getMaxBorder(coordinates)
    
    # print(start) # DEBUG
    # print(end) # DEBUG

    closest = [0] * len(coordinates)
    removal = []
    # Part 1
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            closestIndex = getClosest((i, j), coordinates)
            if closestIndex is None:
                continue
            closest[closestIndex] += 1

            # print("(" + str(i) + "," + str(j) + ")", chr(closestIndex + 97)) # DEBUG
            
            # Filters out results that are infinite because they have points on the border
            if (i == start[0]) or (i == end[0]) or (j == start[1]) or (j == end[1]):
                if not (coordinates[closestIndex] in removal):
                    removal.append(coordinates[closestIndex])

    # print(removal) # DEBUG
    # print(closest) # DEBUG

    # Actually remove the flagged coordinates
    for coord in removal:
        ind = coordinates.index(coord)
        coordinates.pop(ind)
        closest.pop(ind)

    area = sorted(closest)
    print("The biggest area is:", area[-1])

    totalCoords = 0
    coordinates = getCoords(raw_input)
    # Part 2
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            if (closeEnough((i, j), coordinates)):
                totalCoords += 1

    print("The total area of close coordinates is:", totalCoords)

def getCoords(input):
    coords = []
    for line in input:
        line = line.strip()
        middle = line.index(',')
        coords.append((int(line[:middle]), int(line[(middle + 2):])))
    return coords

def getMinBorder(coords):
    x = y = 50000 # Arbitrarily large number
    for point in coords:
        if (point[0] < x):
            x = point[0]
        if (point[1] < y):
            y = point[1]
    return (x, y)

def getMaxBorder(coords):
    x = y = 0
    for point in coords:
        if (point[0] > x):
            x = point[0]
        if (point[1] > y):
            y = point[1]
    return (x, y)

def getClosest(point, coordinates):
    smallestDistance = 1500 # Arbitrarily large distance
    sharedDistance = 1500
    closest = (-1, -1)
    for coord in coordinates:
        distance = abs(coord[0] - point[0]) + abs(coord[1] - point[1])

        if (distance < smallestDistance):
            closest = coord
            smallestDistance = distance
        elif (distance == smallestDistance):
            sharedDistance = distance

    # If two or more coordinates share the biggest different, don't return anything, otherwise return the one that was found
    if (smallestDistance == sharedDistance):
        return None
    else:
        return coordinates.index(closest)

def closeEnough(point, coordinates):
    sumDistance = 0
    for coord in coordinates:
        sumDistance += abs(coord[0] - point[0]) + abs(coord[1] - point[1])
        if (sumDistance > 10000):
            return False
    return True

if __name__ == "__main__":
    main()
