def sonar (data):
    count = 0
    
    for i in range(len(data)):
        if data[i] > data[i -1]:
            count += 1
        else:
            continue

    return(count)

def sonar2(data):
    count = 0

    for i in range (len(data)):
        try:
            a = data[i] + data[i+1] + data[i+2]
            b = data[i+1] + data[i+2] + data[i+3]
        except IndexError:
            continue
        if a < b:
            count += 1
    return(count)

def read(file):
    data = []
    readData = open(file, 'r')

    for i in readData:
        data.append(int(i))

    return(data)

print(sonar2(read('advent/day-1/data.txt')))
