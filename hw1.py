f = open("dict.txt","r")
f.seek(0)
words = f.readlines()#size is 72412
f.close()

import numpy as np

pts = [1,1,2,1,1,2,1,2,1,3,3,2,2,1,1,2,3,1,1,1,1,2,2,3,2,3]
#the scores for each character in lexicographic

freq = np.zeros((len(words), 26))
#a 1*26 vector, shows how many time each char appears in the corresponding word

scores = np.zeros(len(words))
#scores is the vector word scores in dict

for i in range(len(words)):
    for j in range(26):
        freq[i][j] = words[i].count(chr(65+j))+words[i].count(chr(97+j))
    scores[i] = np.multiply(np.inner(freq[i],pts) + 1, np.inner(freq[i],pts) + 1)

freq_ = freq.transpose()
freq_ = np.append(freq_,[np.array(range(len(words)))], axis = 0)
freq_ = freq_.transpose()

s_ = np.append([scores],[np.array(range(len(words)))],axis = 0)
s_ = s_.transpose()
# x is a 72412*2 matrix, with scores in first column, dictionary index in second column


def HighScoreAnagram(A):


    A = A.split(' ')

    freqA = np.zeros(26)
    for i in range(26):
        freqA[i] = A.count(chr(65+i))+A.count(chr(97+i))

    freqA =  np.append(freqA,[len(words)+1])

    AnagramIndex = np.array(list(filter(lambda z: (z <= freqA ).all(), freq_)))[:,26]

    set1 = freq_[AnagramIndex.astype(int),:][:,26]
    #set1 is the indices of the words that are Anagrams or sub-anagram

    set11 = []
    for i in list(set1):
        set11 = set11 + [int(i)]
	
    set1_point = s_[set11]

    HighestScoreIndex  = set1_point[set1_point.argmax(axis=0)[0]][1]

    result = words[int(HighestScoreIndex)]

    return result




for i in range(9):
    B = input("enter 16 char, use space to split:")
    print(HighScoreAnagram(B))
