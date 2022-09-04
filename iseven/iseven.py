from asyncio import WriteTransport


def writeToFile(file, toWrite):
    writeTo = open(file, 'a')
    writeTo.write(toWrite)

def main():
    writeToFile("program.py", "number = int(input('input: '))\nmatch number:\n")

    for i in range(10000):
        if i % 2 == 0:
            state = "Even"
        else:
            state = "Odd"
        
        writeToFile("program.py", f"\n    case {i}:\n        print('{i} is {state}!')")

main()