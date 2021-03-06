import numpy as np
import time
start=time.time()

with open("markovPairs.txt", encoding="utf8") as r:
    contentPairs = r.readlines()

with open("markovFrequency.txt", encoding="utf8") as d:
    contentFrequency = d.readlines()

with open("vocab.txt", encoding="utf8") as v:
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
with open("markovWindowSize1bdResult.txt", 'w', encoding="utf8") as markovResultFile:
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
                if(maskedIndex < len(tmpArray)-1):
                    if((key2,str(tmpArray[maskedIndex+1])) in myDict):
                        bestGuess = contentVocab[int(key2)]
                        bestGuessChance = int(
                            myDict[key2, str(tmpArray[maskedIndex + 1])]) * int(
                            myDict[key1, key2])
                        guessArray.append([bestGuess, bestGuessChance])
                    else:
                        bestGuess = contentVocab[int(key2)]
                        bestGuessChance = int(myDict[key1, key2])
                        guessArray.append([bestGuess, bestGuessChance])
                else:
                    bestGuess = contentVocab[int(key2)]
                    bestGuessChance = int(myDict[key1, key2])
                    guessArray.append([bestGuess, bestGuessChance])

        guessArraysorted = sorted(guessArray, key=lambda item: item[1], reverse=True)[:5]
		#Top-1 icin: 
        #guessArraysorted = guessArraysorted[:1]
        txt = ""
        if (len(guessArraysorted) > 0):
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

