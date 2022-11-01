from collections import defaultdict
from curses.ascii import isalpha, isdigit
import sys
from resource import *
import time
import psutil


def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed


def time_wrapper():
    s1, s2 = ipGenerator("./input/input1.txt")
    start_time = time.time()
    dp = dpSequenceAlign(s1, s2)
    sequence = getSequence(dp, s1, s2)
    print(dp[len(s1)-1][len(s2)-1])
    print(sequence[0])
    print(sequence[1])
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return time_taken


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


def dpSequenceAlign(s1: str, s2: str):

    penalty = defaultdict()
    penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
    penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
    penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
    penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

    len1 = len(s1)
    len2 = len(s2)
    dp = [[0]*(len1+1) for _ in range(len2+1)]
    for i in range(1, len1+1):
        dp[0][i] = i*deltaPenalty
    for i in range(1, len2+1):
        dp[i][0] = i*deltaPenalty
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            dp[i][j] = min(dp[i-1][j-1]+penalty[s1[j-1]][s2[i-1]],
                           dp[i-1][j]+deltaPenalty, dp[i][j-1]+deltaPenalty)
    return dp


def getSequence(dp, s1: str, s2: str):
    penalty = defaultdict()
    penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
    penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
    penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
    penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

    len1 = len(s1)
    len2 = len(s2)
    seq1 = ""
    seq2 = ""
    i = len2
    j = len1
    while (i > 0 and j > 0):
        if (dp[i][j] - penalty[s1[j-1]][s2[i-1]] == dp[i-1][j-1]):
            seq1 = s1[j-1] + seq1
            seq2 = s2[i-1] + seq2
            i -= 1
            j -= 1
        elif (dp[i][j] - deltaPenalty == dp[i-1][j]):
            seq1 = "_" + seq1
            seq2 = s2[i-1] + seq2
            i -= 1
        elif (dp[i][j] - deltaPenalty == dp[i][j-1]):
            seq1 = s1[j-1] + seq1
            seq2 = "_" + seq2
            j -= 1

    while j != 0:
        seq2 = '_' + seq2
        seq1 = s1[j-1] + seq1
        j -= 1

    while i != 0:
        seq1 = '_' + seq1
        seq2 = s2[i-1] + seq2
        i -= 1

    return seq1, seq2


time = time_wrapper()
print(time)
print(process_memory())
