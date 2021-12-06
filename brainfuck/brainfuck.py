"""
An attempt at writing a brainfuck interprater
"""
from matchParen import match


def fuck(pro):
    #create variables
    cell = [0]
    program = []
    pointer = 0
    open = 0

    #converts string to list
    for i in range(len(pro)):
        program.append(pro[i])

    loop = match(program)  
    #main loop
    i = 0
    while i < len(program):
        #moves pointer forward
        if program[i] == '>':
            pointer += 1
            #checks if a cell exists at the pointer location, if not adds a cell with value of 0
            try:
                cell[pointer]
            except IndexError:
                cell.append(0)

        #if the pointer is 0 a new cell is added at the 0 position, otherwise pointer is decremented by 1
        elif program[i] == '<':
            if pointer == 0:
                cell.insert(0, 0)
            else:
                pointer -= 1

        #increments cell at pointer by 1
        elif program[i] == '+':
            cell[pointer] += 1

        #decrements cell at pointer by 1
        elif program[i] == '-':
            cell[pointer] -= 1

        #defines start of loop
        elif program[i] == '[':
            open += 1
            
        #defines end of loop
        elif program[i] == ']':
            open -= 1
            if cell[pointer] == 0:
                continue

            for a in range(len(loop)):
                if loop[a][1] == i:
                    i == loop[a][0]
        #prints cell at pointer
        elif program[i] == '.':
            print(f"{cell[pointer]} ", end='')

        else:
            continue

        i += 1

    if open != 0:
        return('LoopError\nYour loops are fucked up')

    return(f'\n{cell}')


print(fuck("+++[>++<-]"))
