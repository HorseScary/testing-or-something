"""
I Couldn't be asked to fix the other attempt at an interprater so im retrying with a different aproch

I am struggling with loops
"""

def brainFuck(pro):
    program = []

    for i in range(len(pro)):
        program.append(pro[i])
    
    pointer = 0
    tape = []

    i = 0
    while i <= len(pro):
        if i == '>':
            pointer += 1
            try:
                tape[pointer]
            except IndexError:
                tape.append(0)

        elif i == '<':
            if pointer == 0:
                tape.insert(0,0)
            else:
                pointer -= 1

        elif i == '+':
            tape[pointer] += 1

        elif i == '-':
            tape[pointer] -= 1

        elif i == '[':
            open += 1

        elif i == ']':
            open -= 1
            if tape[pointer] == 0:
                continue
        elif i == '.':
            print(tape[pointer], end='')