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


def dpSequenceAlign(filename: str):
    s1, s2 = ipGenerator(filename)
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0]*(len1+1) for _ in range(len2+1)]
    for i in range(1, len1+1):
        dp[0][i] = i*deltaPenalty
    for i in range(1, len2+1):
        dp[i][0] = i*deltaPenalty
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            dp[i][j] = min(dp[i-1][j-1]+getPenalty(s1[j-1], s2[i-1]),
                           dp[i-1][j]+deltaPenalty, dp[i][j-1]+deltaPenalty)
    return dp[len1][len2]


print(dpSequenceAlign("./input/input1.txt"))
# print(ipGenerator("./input/input1.txt"))


# print(getPenalty('A', 'C'))
