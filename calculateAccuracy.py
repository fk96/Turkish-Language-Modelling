#Başarı oranı hesaplanmak istenen sonuç dosyasının ismi girilmelidir.
with open("markovWindowSize3Top1Result.txt",encoding="utf-8") as fi:
    predictions = fi.readlines()

with open("testDataMaskedAnswers.txt",encoding="utf-8") as fi:
    answers = fi.readlines()

tCount = 0

for i in range(len(predictions)):
	line = predictions[i]
	tmp = line.split('\n')	
	tmpPr = tmp[0].split()
	j = 0 
	flag = 0
	line2 = answers[i]
	tmp2 = line2.split('\n')
	answer = tmp2[0]

	while j < len(tmpPr) and flag == 0:		
		if tmpPr[j] == answer:
			flag = 1
		else:
			j = j + 1	
		
	if j < len(tmpPr):
		tCount += 1

print(tCount)
acc = tCount / len(predictions)
print("Accuracy: " + str(acc))