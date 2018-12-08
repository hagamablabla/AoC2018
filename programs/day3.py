def main():
    # Get raw input
    file = open("../inputs/day3.txt","r")
    raw_input = file.readlines()
    file.close()
    
    fabric = [[0 for x in range(1000 + 1)] for y in range(1000 + 1)]
    overlap = 0

    processed = []
    for line in raw_input:
        # Get the indexes that mark each section
        claimNum = 0
        locX = line.index('@')
        locY = line.index(',')
        sizeX = line.index(':')
        sizeY = line.index('x')
        end = line.index('\n')

        # Claim Number, X location, Y location, X size, Y size
        claim = []
        claim.append(int(line[(claimNum + 1):(locX - 1)]))
        claim.append(int(line[(locX + 2):locY]))
        claim.append(int(line[(locY + 1):sizeX]))
        claim.append(int(line[(sizeX + 2):sizeY]))
        claim.append(int(line[(sizeY + 1):end]))

        processed.append(claim)

    # Part 1
    for claim in processed:
        for i in range(claim[1], (claim[1] + claim[3])):
            for j in range(claim[2], (claim[2] + claim[4])):
                fabric[i][j] += 1
                if (fabric[i][j] == 2):
                    overlap += 1

    print("Number of overlaps:", overlap)

    # Part 2
    for claim in processed:
        noOverlap = True
        for i in range(claim[1], (claim[1] + claim[3])):
            for j in range(claim[2], (claim[2] + claim[4])):
                if (fabric[i][j] > 1):
                    noOverlap = False
        if noOverlap:
            print(claim[0], "did not have any overlap")

if __name__ == "__main__":
    main()
