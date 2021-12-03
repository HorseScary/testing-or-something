def match(toMatch):
    i = 0

    matching = []
    open = 0
    paren = []

    for i in range(len(toMatch)):
        a = (list(toMatch[i]))
        matching.append(a)
        matching[i].insert(0, i)
    #tbh this should probably be a for loop
    
    while i < len(matching):
        if matching[i][1] == '[':
            open = matching[i][0]

        elif matching[i][1] == ']':
            paren.append([open, matching[i][0]])
            del(matching[i])
            i = 0
            print('Close')
        i += 1
    
    return(paren)


a = ['+', '+', '+', '+', '+', '+', '+', '+', '[', '>', '+', '+', '+', '+', '[', '>', '+', '+', '>', '+', '+', '+', '>', '+', '+', '+', '>', '+', '<', '<', '<', '<', '-', ']', '>', '+', '>', '+', '>', '-', '>', '>', '+', '[', '<', ']', '<', '-', ']', '>', '>', '.', '>', '-', '-', '-', '.', '+', '+', '+', '+', '+', '+', '+', '.', '.', '+', '+', '+', '.', '>', '>', '.', '<', '-', '.', '<', '.', '+', '+', '+', '.', '-', '-', '-', '-', '-', '-', '.', '-', '-', '-', '-', '-', '-', '-', '-', '.', '>', '>', '+', '.', '>', '+', '+', '.']
print (match(a))

#expected output: 
# [0, 6] [2, 3] [4, 5]