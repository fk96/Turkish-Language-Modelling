import time

start=time.time()

with open("trainData.txt",encoding="utf-8") as a: #Train dosyasının yolu girilmelidir
    sentences = a.readlines()

with open("vocab.txt", encoding="utf8") as v: #Vocabulary dosyasının yolu
    contentVocab = v.readlines()

contentVocab = [x.strip() for x in contentVocab]

myDict = {}

for line in sentences:
	tmpArray = line.split()
	for i in range(len(tmpArray)-1):
		word1 = tmpArray[i]
		word2 = tmpArray[i+1]
		index1 = contentVocab.index(word1)
		index2 = contentVocab.index(word2)	
		if (index1,index2) not in myDict:
			myDict[index1,index2] = 1					
			#print(word1,word2)
		else:
			myDict[index1,index2] += 1
		
with open("markovPairs.txt","w",encoding="utf-8") as p:
	with open("markovFrequency.txt","w",encoding="utf-8") as f:
		for key1, key2 in myDict:
			p.write(str(key1) + "," + str(key2) + "\n")
			f.write(str(myDict[key1,key2]) + "\n")

end=time.time()
print("Total exec time:")
print(end-start)
