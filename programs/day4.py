def main():
    # Get raw input
    file = open("../inputs/day4.txt","r")
    raw_input = file.readlines()
    file.close()

    timeAction = {}
    # Seperate timestamp from action and process the results
    for line in raw_input:
        raw_input_list = line.split('] ')
        timeAction[parseTime(raw_input_list[0])] = parseAction(raw_input_list[1])

    # print(timeAction) # DEBUG

    sleepTime = 0
    wakeTime = 0
    onDuty = 0
    guardList = {}
    # Catalogue guard sleeping times
    for time in sorted(timeAction.keys()):
        if (timeAction[time] == -1):
            sleepTime = int(time[10:12])
        elif (timeAction[time] == -2):
            wakeTime = int(time[10:12])

            # If the guard is already registered, update his times, otherwise create a new sheet for him
            if onDuty in guardList:
                minutes = guardList[onDuty]
            else:
                minutes = [0] * 60

            # Edit the list with the sleep and wake times
            for i in range(sleepTime, wakeTime):
                minutes[i] += 1

            # Save the time sheet back to the list of guards, or add it if this is a new guard
            guardList[onDuty] = minutes
        else:
            onDuty = timeAction[time]
            sleepTime = 0
            wakeTime = 0

    # print(guardList) # DEBUG

    guardID = 0
    max = 0
    # Part 1
    # Find the guard with the most time spent sleeping
    for guard in guardList.keys():
        timeSheet = guardList[guard]
        total = sum(timeSheet)
        if (total > max):
            max = total
            guardID = guard

    # print(guardList[guardID]) # DEBUG

    minute = 0
    max = 0
    # Find the minute with the most minutes slept
    for i in range(len(guardList[guardID])):
        if (guardList[guardID][i] > max):
            max = guardList[guardID][i]
            minute = i

    print("The ID of the guard that sleeps the most times the minute he is asleep the most is:", (guardID * minute))

    guardID = 0
    minute = 0
    max = 0
    # Part 2
    # Find the minute with the most time spent asleep
    for guard in guardList.keys():
        timeSheet = guardList[guard]
        for i in range(len(timeSheet)):
            if (timeSheet[i] > max):
                max = timeSheet[i]
                guardID = guard
                minute = i

    print("The ID of the guard that slept the most times times the minute he slept the most times is:", (guardID * minute))


def parseTime(dateTime):
    # Year, Month, Day, Hour, Minute
    #record = []
    #record.append(int(dateTime[1:5]))
    #record.append(int(dateTime[6:8]))
    #record.append(int(dateTime[9:11]))
    #record.append(int(dateTime[12:14]))
    #record.append(int(dateTime[15:]))

    # Compresses time into one string
    record = dateTime[1:5] + dateTime[6:8] + dateTime[9:11] + dateTime[12:14] + dateTime[15:]

    return record

def parseAction(action):
    if 'falls' in action:
        return -1
    elif 'wakes' in action:
        return -2
    else:
        end = action.find('begin') - 1
        guard = action[7:end]
        return int(guard)

if __name__ == "__main__":
    main()
