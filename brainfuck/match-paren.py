def match(thing):
    i = 0

    paren = []
    while i != len(thing):
        if thing[i] == '[':
            paren.append([i, 's'])
        elif thing[i] == ']':
            paren.append([i, 'e'])
        else:
            pass
        i +=1
    return(f'{paren}')

a = '[', '[', ']', '[', ']', ']'
print (match(a))