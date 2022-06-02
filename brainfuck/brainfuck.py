"""
An attempt at writing a brainfuck interprater
"""

def fuck(pro):
    #create variables
    cell = [0]
    program = []
    pointer = 0
    open = 0

    #converts string to list
    for i in range(len(pro)):
        program.append(pro[i])

    #main loop
    i = 0
    while i < len(program):
        if program[i] == '>':
            pointer += 1

            try:
                cell[pointer]

            except IndexError:
                cell.append(0)

        elif program[i] == '<':
            if pointer == 0:
                cell.insert(0, 0)

            else:
                pointer -= 1

        elif program[i] == '+':
            cell[pointer] += 1

        elif program[i] == '-':
            cell[pointer] -= 1

        elif program[i] == '.':
            print(f"{cell[pointer]} ", end='')

        elif program[i] == '[':
            open += 1

        elif program[i] == ']':
            if open == 0:
                print("LoopError\nA loop has an end, but no start!")

            elif cell[pointer] == 0:
                pass


        i += 1

        print(i)

    if open != 0:
        return('LoopError\nYour loops are fucked up')

    return(f'\n{cell}')


print(fuck("+++[>++<-]"))
