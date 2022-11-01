from collections import defaultdict

deltaPenalty = 30


def getPenalty(char1: str, char2: str):
    penalty = defaultdict()
    penalty['A'] = {'A': 0, 'C': 110, 'G': 48, 'T': 94}
    penalty['C'] = {'A': 110, 'C': 0, 'G': 118, 'T': 48}
    penalty['G'] = {'A': 48, 'C': 118, 'G': 0, 'T': 110}
    penalty['T'] = {'A': 94, 'C': 48, 'G': 110, 'T': 0}

    return penalty[char1][char2]


print(getPenalty('A', 'C'))
