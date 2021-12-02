def sonar (data):
    count = 0
    
    for i in range(len(data)):
        if data[i] > data[i -1]:
            count += 1
        else:
            continue

    return(count)

def read(file):
    data = []
    readData = open(file, 'r')

    for i in readData:
        data.append(int(i))

    return(data)

print(sonar(read('advent/data.txt')))