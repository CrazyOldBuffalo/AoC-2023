from race import Race

def split_into_chunks(s, chunk_size):
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]

def parsefile(filename):
    with open(filename) as file:
        for line in file:
            parts = line.split()
            if parts[0] == 'Time:':
                times= [int(x) for x in parts[1:]]
            elif parts[0] == 'Distance:':
                distance = [int(x) for x in parts[1:]]
    times = ''.join([str(time) for time in times])
    distance = ''.join([str(dist) for dist in distance])
    task2arr = [int(times), int(distance)]
    return task2arr

def main():
    filedata = parsefile('./input.txt')
    task2_race : Race = Race(filedata[1], filedata[0])
    winningraces = task2_race.calculate_races()
    print(winningraces)



if __name__ == "__main__":
    main()

