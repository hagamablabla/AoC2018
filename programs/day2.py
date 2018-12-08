import os

def main():
    # Get raw input
    file = open("../inputs/day2.txt","r")
    raw_input = file.readlines()
    file.close()

    twos = threes = 0
    letCounts = [0] * 26
    letHistory = []

    # Part 1
    for box in raw_input:
        # Remove newline at the end of the string
        label = box.strip()

        # Get a count of each letter on the label
        for letter in label:
            letCounts[getAsc(letter)] += 1

        # Add one if the box has either two or three repeating letters
        if 2 in letCounts:
            twos += 1
        if 3 in letCounts:
            threes += 1

        # Save and reset letter counts
        letHistory.append(letCounts.copy())
        letCounts = [0] * 26

    print("The checksum is", twos * threes)

    # Part 2
    for i in range(0, len(letHistory)):
        for j in range(i, len(letHistory)):
            # Found a pair of counts that have on changed letter
            if (compareCounts(letHistory[i], letHistory[j])):
                results = deepCompare(raw_input[i].strip(), raw_input[j].strip())
                if (results != ""):
                    print("The common letters are:", results)
                    input()
                    exit()


def getAsc(letter):
    return ord(letter) - 97; # Hardcoded to make 'a' index 0

def compareCounts(list1, list2):
    totalChanges = 0
    pairFound = False

    for i in range(0, len(list1)):
        # Check if there is a difference between the lists
        difference = (list1[i] - list2[i])
        totalChanges += difference

        # If the difference is now greater than 2, that means there are at least two letters off
        if (totalChanges > 1) or (totalChanges < -1):
            return False
        # If there was already a difference found, but another is found, then there are now more than two difference(Edge case)
        elif pairFound and ((difference == 1) or (difference == -1)):
            return False
        # If the difference has gone from 1/-1 back to 0, we have one letter off, so a pair has been found
        elif (totalChanges == 0) and ((difference == 1) or (difference == -1)):
            pairFound = True

    # If there was a pair found, the function returns true, otherwise they are the same string and will return false.
    return pairFound

# Something causes slicing to work incorrectly, but it's close enough to do by hand
def deepCompare(string1, string2):
    index = 0
    for i in range(0, len(string1)):
        if (string1[i] != string2[i]):
            if (index > 0):
                return("");
            else:
                index = i
    return(string1[:i] + string1[(i + 1):])

if __name__ == "__main__":
    main()