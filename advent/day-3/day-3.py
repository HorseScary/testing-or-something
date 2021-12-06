def read(file):
    data = []
    readData = open(file, 'r')

    for i in readData:
        data.append(i)

    return(data)

def rates(data):
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    final = []

    for a in range(12):
        for i in data:
            if i[a] == '1':
                count[a] += 1
        if count[a] > 500:
            final.append(1)
        else:
            final.append(0)

    return(f'{count}\n{final}')

