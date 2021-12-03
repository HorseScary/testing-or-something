def match(toMatch):
    i = 0

    matching = []
    open = [0, 0]
    paren = []

    for i in range(len(toMatch)):
        a = (list(toMatch[i]))
        matching.append(a)
        matching[i].insert(0, i)
    #tbh this should probably be a for loop
    i = 0

    while i < len(matching):
        if matching[i][1] == '[':
            open[1] = matching[i][0]
            open[0] = i

        elif matching[i][1] == ']':
            paren.append([open[1], matching[i][0]])
            del(matching[i])
            del(matching[open[0]])
            i = 0

        i += 1

    return(paren)


a = ['+', '+', '+', '+', '+', '+', '+', '+', '[', '>', '+', '+', '+', '+', '[', '>', '+', '+', '>', '+', '+', '+', '>', '+', '+', '+', '>', '+', '<', '<', '<', '<', '-', ']', '>', '+', '>', '+', '>', '-', '>', '>', '+', '[', '<', ']', '<', '-', ']', '>', '>', '.', '>',
     '-', '-', '-', '.', '+', '+', '+', '+', '+', '+', '+', '.', '.', '+', '+', '+', '.', '>', '>', '.', '<', '-', '.', '<', '.', '+', '+', '+', '.', '-', '-', '-', '-', '-', '-', '.', '-', '-', '-', '-', '-', '-', '-', '-', '.', '>', '>', '+', '.', '>', '+', '+', '.']
print(match(a))

#expected output:
# [8, 48] [14, 33] [43, 45]
# [0, 6] [2, 3] [4, 5]
