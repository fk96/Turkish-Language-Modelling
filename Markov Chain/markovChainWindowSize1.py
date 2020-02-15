import numpy as np
import time
start=time.time()

with open("markovPairs.txt", encoding="utf8") as r: #1.kelime,2.kelime kaç defa geçiyor değerleri sözlük yapısında tutuluyor 
    contentPairs = r.readlines()

with open("markovFrequency.txt", encoding="utf8") as d:#1. ve 2. kelimenin birlikte gelme sayısı
    contentFrequency = d.readlines()

with open("vocab.txt", encoding="utf8") as v:#kelimeler
    contentVocab = v.readlines()

with open("testDataMasked.txt", encoding="utf8") as f:
    contentData = f.readlines()

contentData = [x.strip() for x in contentData]
contentVocab = [x.strip() for x in contentVocab]
contentFrequency = [x.strip() for x in contentFrequency]
contentPairs = [x.strip() for x in contentPairs]

vocabArray = []

rowArray = []
colArray = []
frequencyArray = []

myDict = {}

for line in contentVocab:
    vocabArray.append(line)

for line in contentFrequency:
    tmpArray = line.split()
    for tmpData in tmpArray:
        frequencyArray.append(tmpData)

dictIndex = 0
for line in contentPairs:
    tmpArray = line.split()
    for tmpTuple in tmpArray:
        tmpTupleArray = tmpTuple.split(',')
        myDict[tmpTupleArray[0],tmpTupleArray[1]] = frequencyArray[dictIndex]
        dictIndex += 1


count = 0
lineIndex = 1
with open("markovWindowSize1Result.txt", 'w', encoding="utf8") as markovResultFile:
    for line in contentData:
        tmpArray = line.split()
        maskedIndex = tmpArray.index('[MASK]')

        for i in range (len(tmpArray)):
            if(i != maskedIndex):
                try:
                    tmpArray[i] = contentVocab.index(tmpArray[i])
                except:
                    count += 1
            i+=1

        bestGuess = "----"
        bestGuessChance = 0
        i=0
        guessArray = []

        for key1, key2 in myDict:
            if((int(key1) == tmpArray[maskedIndex-1]) and (int(myDict[key1,key2]) > bestGuessChance)):
                bestGuess = contentVocab[int(key2)]
                bestGuessChance = int(myDict[key1, key2])
                guessArray.append([bestGuess, bestGuessChance])

        guessArraysorted = sorted(guessArray, key=lambda item: item[1], reverse=True)[:5]
		#Top-1 icin: 
        #guessArraysorted = guessArraysorted[:1]
        txt = ""
        if(len(guessArraysorted) > 0):
            for guess in guessArraysorted:
                txt += guess[0] + " "
            txt += "\n"
        else:
            txt += "----\n"
        print(str(lineIndex) +". " + str(line) + "\nPredictions: " + str(txt))
        lineIndex+=1
        markovResultFile.write(txt)



end = time.time()
print("Total exec time:")
print(end-start)
