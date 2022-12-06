from collections import defaultdict
from resource import *
import time
import psutil
import sys
import os


def get_process_memory():
    process_mem = psutil.Process(os.getpid())
    return process_mem.memory_info().rss


class basicSeqAl:
    def time_wrapper(self, ipFileName):
        s1, s2 = self.ipGenerator(ipFileName)
        # print("length of input: " + str(len(s1)+len(s2)))
        start_time = time.time()
        dp = self.dpSequenceAlign(s1, s2)
        sequence = self.getSequence(dp, s1, s2)
        end_time = time.time()
        # print(dp[len(s2)-1][len(s1)-1])
        # print(sequence[0])
        # print(sequence[1])
        time_taken = (end_time - start_time)*1000
        return time_taken

    deltaPenalty = 30

    def getPenalty(self, char1: str, char2: str):
        penalty = defaultdict()
        penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
        penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
        penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
        penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

        return penalty[char1][char2]

    def ipGenerator(self, fileName: str):
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

    def dpSequenceAlign(self, s1: str, s2: str):

        penalty = defaultdict()
        penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
        penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
        penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
        penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

        len1 = len(s1)
        len2 = len(s2)
        dp = [[0]*(len1+1) for _ in range(len2+1)]
        for i in range(1, len1+1):
            dp[0][i] = i*self.deltaPenalty
        for i in range(1, len2+1):
            dp[i][0] = i*self.deltaPenalty
        for i in range(1, len2+1):
            for j in range(1, len1+1):
                dp[i][j] = min(dp[i-1][j-1]+penalty[s1[j-1]][s2[i-1]],
                               dp[i-1][j]+self.deltaPenalty,
                               dp[i][j-1]+self.deltaPenalty)
        return dp

    def getSequence(self, dp, s1: str, s2: str):
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
            elif (dp[i][j] - self.deltaPenalty == dp[i-1][j]):
                seq1 = "_" + seq1
                seq2 = s2[i-1] + seq2
                i -= 1
            elif (dp[i][j] - self.deltaPenalty == dp[i][j-1]):
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


if __name__ == "__main__":
    memory_usage_before = get_process_memory()
    obj = basicSeqAl()
    time = obj.time_wrapper(sys.argv[1])
    memory_usage_after = get_process_memory()
    # print("time: " + str(time))
    print((memory_usage_after - memory_usage_before)//1024)
