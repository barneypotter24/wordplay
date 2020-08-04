from scipy.spatial.distance import hamming
from read_english_dictionary import load_words
import numpy as np

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

if __name__ == '__main__':

    english_words = load_words()
    print("What maximum Levenshtein threshold should be used?")
    THRESHOLD = int(input())
    while True:
        print("What word should we use next?")
        WORD = input()
        near_words = {str(id) : [] for id in range(THRESHOLD+1)}

        for ref_word in english_words:
            ld = levenshteinDistance(WORD, ref_word)
            if ld <= THRESHOLD:
                near_words[str(ld)].append(ref_word)

        print(near_words)
