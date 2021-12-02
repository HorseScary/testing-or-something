def read(file):
    data = []
    readData = open(file, 'r')

    for i in readData:
        data.append(i)

    return(data)

def control(data):
    depth = 0
    horizontal = 0
    aim = 0

    for i in data:
        if i[0] == 'u':
            aim -= int(i[3])
        elif i[0] == 'd':
            aim += int(i[5])
        elif i[0] == 'f':
            horizontal += int(i[8])
            depth += (aim * int(i[8]))
        else:
            print("Some weird shit happend")
    return(f'Depth: {depth}\nThe other one: {horizontal}\nCombined: {depth * horizontal}')

print(control(read("advent/day-2/data.txt")))