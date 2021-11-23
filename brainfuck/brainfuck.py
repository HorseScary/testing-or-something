"""
An attempt at writing a brainfuck interprater
"""

def fuck(pro):
    cell = [0]
    program = []
    pos = 0
    open = 0
    loop = []
    for i in range(len(pro)):
        program.append(pro[i])

    for i in program:
        if i == '>':
            pos += 1
            try:
                cell[pos]
            except IndexError:
                cell.append(0)

        elif i == '<':
            if pos == 0:
                cell.insert(0,0)
            else:
                pos -= 1

        elif i == '+':
            cell[pos] += 1

        elif i == '-':
            cell[pos] -= 1

        elif i == '[':
            open += 1

        elif i == ']':
            open -= 1

            if pos == 0:
                continue
            else:
                fuck(pro)

        elif i == '.':
            print(cell[pos], end='')

        else:
            continue
    
    if open != 0:
        return('LoopError\nYour loops are fucked up')

    return(f'\n{open}')

print(fuck("+++[>+<-]>."))