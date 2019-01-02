def main():
    # Get raw input
    file = open("../inputs/day5.txt","r")
    raw_input = file.read().strip()
    file.close()

    # print(raw_input) # DEBUG

    # Generate pairs
    polymerPairs = generatePairs()

    # Part 1
    fullPolymer = reaction(raw_input, polymerPairs)
                
    print("The polymer has", len(fullPolymer), "units left.")

    removedLength = {}
    # Part 2
    for i in range(ord('a'), ord('z') + 1):
        # Create a new polymer with lower and upper case of one unit removed
        newPolymer = raw_input.replace(chr(i), '').replace(chr(i - 32), '')
        finishedPolymer = reaction(newPolymer, polymerPairs)
        removedLength[chr(i)] = len(finishedPolymer)

    shortest = sorted(removedLength.values())[0]
    print("The polymer with the shortest length has length:", shortest)

def generatePairs():
    pairs = []
    for i in range(ord('a'), ord('z') + 1):
        pairs.append(chr(i) + chr(i - 32))
        pairs.append(chr(i - 32) + chr(i))
    return pairs

def reaction(basePolymer, polymerPairs):
    noChanges = True
    while (noChanges):
        noChanges = False
        for pair in polymerPairs:
            if pair in basePolymer:
                # print("Pair found:", pair) # DEBUG
                basePolymer = basePolymer.replace(pair, '')
                noChanges = True
    return(basePolymer)

if __name__ == "__main__":
    main()
