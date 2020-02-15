import random
# Test dosyasının yolu girilmelidir. 
with open("testData.txt",encoding="utf-8") as fi: 
    sentences = fi.readlines()

# Maskelenmiş kelimelerin cevaplarını içerecek dosya  
with open("testDataMaskedAnswer.txt", "w",encoding="utf-8") as a:
# Maskelenmiş test verisini içerecek dosya 
  with open("testDataMasked.txt", "w",encoding="utf-8") as fo: 
    for line in sentences:
          tmpWords = line.split()
          length = len(tmpWords)
          maskedIndex = random.randrange(length)
          maskedWord = tmpWords[maskedIndex]
          tmpWords[maskedIndex] = "[MASK]"
          maskedLine = ''
          for i in tmpWords:
            maskedLine += i + ' '
          maskedLine = maskedLine.strip(' ')      
          a.write(maskedWord + "\n")
          fo.write(maskedLine + "\n")