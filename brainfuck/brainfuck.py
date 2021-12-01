"""
An attempt at writing a brainfuck interprater
"""


def fuck(pro):
    cell = [0]
    program = []
    pointer = 0
    open = 0
    loop = []

    for i in range(len(pro)):
        program.append(pro[i])

    for i in program:
        if i == '>':
            pointer += 1
            try:
                cell[pointer]
            except IndexError:
                cell.append(0)

        elif i == '<':
            if pointer == 0:
                cell.insert(0, 0)
            else:
                pointer -= 1

        elif i == '+':
            cell[pointer] += 1

        elif i == '-':
            cell[pointer] -= 1

        elif i == '[':
            open += 1

        elif i == ']':
            open -= 1
            if cell[pointer] == 0:
                continue
        elif i == '.':
            print(cell[pointer], end='')

        else:
            continue

    if open != 0:
        return('LoopError\nYour loops are fucked up')

    return(f'\n{cell}')


print(fuck(
    "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."))
