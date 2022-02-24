def getWords(file):
    wordList = []
    words = open(file, 'r')
    for line in words:
        wordList.append(line.replace('\n', ''))

    return(wordList)


def letterFrequency(file):
    wordList = getWords(file)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in wordList:
        for i2 in range(len(letters)):
            if letters[i2] in i:
                count[i2] += 1

    for i in range(len(letters)):
        print(f'{letters[i]}: {count[i]}')
letterFrequency('wordle/words.txt')