def match(toMatch):
    i = 0

    open = 0
    paren = []

    for i in range(len(toMatch)):
        toMatch[i] = list(toMatch[i])
        toMatch[i].insert(0, i)

    #tbh this should probably be a for loop
    
    while i != len(toMatch):


        i +=1
    
    return(f'Thing: {toMatch}\nParen: {paren}')


a = ['[', '[', ']', '[', ']', ']']
print (match(a))