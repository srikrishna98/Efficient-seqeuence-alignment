from collections import defaultdict
from resource import *
import time
import psutil
import sys
import os
from pathlib import Path


class EfficientSeqAl:
    def get_process_memory(self):
        process_mem = psutil.Process(os.getpid())
        return process_mem.memory_info().rss

    def time_wrapper(self, ipFileName, opFileName):
        s1, s2 = self.ipGenerator(ipFileName)
        start_time = time.time()
        ans = self.divAndConq(s1, s2)
        end_time = time.time()
        write_to_op(opFileName, "cost of alignment: "+str(ans[2]))
        write_to_op(opFileName, "S1: "+ans[0])
        write_to_op(opFileName, "S2: "+ans[1])
        time_taken = (end_time - start_time)*1000
        return time_taken

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

    def spaceEfficientAlignment(self, X, Y, flag):
        dp = []
        deltaPenalty = 30
        penalty = defaultdict()
        penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
        penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
        penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
        penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

        for i in range(2):
            dp.append([0] * (len(Y) + 1))
        for i in range(len(Y) + 1):
            dp[0][i] = deltaPenalty * i

        if flag == 0:
            for i in range(1, len(X) + 1):
                dp[1][0] = i * deltaPenalty
                for j in range(1, len(Y) + 1):
                    dp[1][j] = min(dp[0][j - 1] + penalty[X[i - 1]][Y[j - 1]],
                                   dp[0][j] + deltaPenalty,
                                   dp[1][j - 1] + deltaPenalty)
                for j in range(len(Y)+1):
                    dp[0][j] = dp[1][j]
        elif flag == 1:
            for i in range(1, len(X) + 1):
                dp[1][0] = i * deltaPenalty
                for j in range(1, len(Y) + 1):
                    dp[1][j] = min(dp[0][j - 1] + penalty[X[len(X) - i]][Y[len(Y) - j]],
                                   dp[0][j] + deltaPenalty,
                                   dp[1][j - 1] + deltaPenalty)
                for j in range(len(Y) + 1):
                    dp[0][j] = dp[1][j]
        final = dp[1]
        return final

    def seqAlignment(self, string1, string2):
        dp = []
        deltaPenalty = 30
        penalty = defaultdict()
        penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
        penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
        penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
        penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

        for i in range(len(string1) + 1):
            dp.append([0] * (len(string2) + 1))

        for i in range(len(string2) + 1):
            dp[0][i] = i * deltaPenalty
        for i in range(len(string1) + 1):
            dp[i][0] = i * deltaPenalty
        for i in range(1, len(string1) + 1):
            for j in range(1, len(string2) + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + penalty[string1[i-1]][string2[j-1]],
                               dp[i][j - 1] + deltaPenalty,
                               dp[i - 1][j] + deltaPenalty)
        i, j = len(string1), len(string2)
        x = ""
        y = ""
        while i and j:
            if dp[i][j] - penalty[string1[i - 1]][string2[j - 1]] == dp[i - 1][j - 1]:
                x = string1[i - 1] + x
                y = string2[j - 1] + y
                i -= 1
                j -= 1
            elif dp[i][j]-deltaPenalty == dp[i - 1][j]:
                x = string1[i - 1] + x
                y = "_" + y
                i -= 1
            elif dp[i][j]-deltaPenalty == dp[i][j - 1]:
                x = "_" + x
                y = string2[j - 1] + y
                j -= 1

        while i:
            x = string1[i - 1] + x
            y = "_" + y
            i -= 1
        while j:
            x = "_" + x
            y = string2[j - 1] + y
            j -= 1
        return [x, y, dp[len(string1)][len(string2)]]

    def divAndConq(self, str1, str2):
        m = len(str1)
        n = len(str2)
        if m < 2 or n < 2:
            return self.seqAlignment(str1, str2)
        else:
            firstHalf = self.spaceEfficientAlignment(str1[:m // 2], str2, 0)
            secondHalf = self.spaceEfficientAlignment(str1[m // 2:], str2, 1)
            newArray = [firstHalf[j] + secondHalf[n - j] for j in range(n + 1)]
            q = newArray.index(min(newArray))
            callLeft = self.divAndConq(str1[:len(str1) // 2], str2[:q])
            callRight = self.divAndConq(str1[len(str1) // 2:], str2[q:])
            l = [callLeft[r] + callRight[r] for r in range(3)]
        return [callLeft[r] + callRight[r] for r in range(3)]


def write_to_op(opFileName, str):
    obj = Path(opFileName)
    fo = open(opFileName, "a")
    fo.seek(0, 2)
    fo.write(str+"\n")
    fo.close()


if __name__ == "__main__":
    fo = open(sys.argv[2], "w")
    fo.close()
    obj = EfficientSeqAl()
    memory_usage_before = obj.get_process_memory()
    time = obj.time_wrapper(sys.argv[1], sys.argv[2])
    memory_usage_after = obj.get_process_memory()
    write_to_op(sys.argv[2], "time in ms: " + str(time))
    write_to_op(sys.argv[2], "memory in kb: " +
                str((memory_usage_after - memory_usage_before)//1024))
