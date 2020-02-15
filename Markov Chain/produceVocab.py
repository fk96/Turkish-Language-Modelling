#Aşağıdaki dosya ismi train dosyasının ismi olmalıdır.
with open("trainData.txt",encoding="utf-8") as a: 
    sentences = a.readlines()

myDict = {}

for line in sentences:
	tmpArray = line.split()
	for i in range(len(tmpArray)):
		word = tmpArray[i]		
		if word not in myDict:
			myDict[word] = 1					
		else:
			myDict[word] += 1

myDict_sorted = {k: v for k, v in sorted(myDict.items(), key=lambda x: x[1], reverse = True)}

#print(myDict_sorted)

with open("vocab.txt","w",encoding="utf-8") as f:
	for key in myDict_sorted:
		f.write(key + "\n")
#myDict = dict(l)

