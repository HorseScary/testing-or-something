def read(file):
    data = []
    readData = open(file, 'r')

    for i in readData:
        data.append(i)

    return(data)
    
def rates(data):
    newData = data[:]
    # for a in range(12):
    #     for i in data:
    #         if i[a] == '1':
    #             count[a] += 1
    #     if count[a] > 500:
    #         common.append(1)
    #     else:
    #         common.append(0)
    binPos = 0

    while len(newData) > 1:
        zero = 0
        one = 0
        for i in range(len(newData)):
        
            if newData[i][binPos] == '1':
                  one += 1
            elif newData[i][binPos] == '0':
                zero +=1

    return(newData)
#110111001011
# 3531
#001000110111
# 567
print(rates(read('advent/day-3/data.txt')))