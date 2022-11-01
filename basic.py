from collections import defaultdict
from curses.ascii import isalpha, isdigit

deltaPenalty = 30


def getPenalty(char1: str, char2: str):
    penalty = defaultdict()
    penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
    penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
    penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
    penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

    return penalty[char1][char2]


def ipGenerator(fileName: str):
    fileObj = open(fileName, "r")
    processedInput = []
    inp = ""
    while (True):
        line = fileObj.readline()
        if not line:
            processedInput.append(inp)
            break
        line = line.strip()

        if (line.isdigit()):
            ind = int(line)
            tempFirst = inp[0:ind+1]
            tempEnd = inp[ind+1:]
            inp = tempFirst + inp + tempEnd
        else:
            processedInput.append(inp)
            inp = str(line)

    return processedInput[1:]


# print(ipGenerator("./input/input1.txt"))


# print(getPenalty('A', 'C'))
