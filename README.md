# Turkish-Language-Modelling

Train ve test işlemleri öncesinde yapılması gerekenler:
1)Veri setinin indirilebilecek haldeki indirme linki aşağıdaki gibidir.
"http://www.kemik.yildiz.edu.tr/data/File/42bin_haber.rar" linkten veri seti 
indirilmeli ve tek bir dosya olarak birleştirilmelidir.

2)BERT dizini altındaki BertTrain.ipynb dosyası bir Google Colab sayfası 
açılarak upload edilmeli ve burda yer alan komutlar yardımıyla dataset 
temizlenmelidir.

3)Veri seti, test ve train olarak ayrılmalıdır.

4)Test verisi maskTestData.py dosyası çalıştırılarak
test cümlelerindeki rastgele bir kelime maskelenmelidir.Bu işlem sonunda
testDataMasked.txt ve testDataMaskedAnswers.txt dosyaları oluşmalıdır.
 
***Markov Chain***

Markov Chain yönteminin çalışması için aşağıdaki adımların sırayla uygulanması gerekir.
1)Markov Chain dizini altındaki produceVocab.py dosyası train verisinin yolu 
verilerek çalıştırılmalıdır.Bu işlemin sonunda vocab.txt isimli dosya oluşacaktır.
2)Markov Chain dizini altındaki producePairs.py dosyası train verisinin ve
vocab.txt dosyasının yolu verilerek çalıştırılmalıdır.Bu işlemin sonunda 
markovPairs.txt ve markovFrequency.txt isimli dosyalar oluşacaktır.
3)Markov Chain dizini altında markovPairs.txt, markovFrequency.txt,vocab.txt,
testDataMasked.txt dosyaları bir arada olmalıdır.
Daha sonra bu dizindeki istenilen Markov Chain yöntemi çalıştırılabilir. 

***BERT***

BERT yönteminin çalışması için aşağıdaki adımların sırayla uygulanması gerekir.
1)BERT dizini altındaki BertTrain.ipynb dosyası bir Google Colab sayfası 
açılarak upload edilmeli ve buradaki kod parçaları sırasıyla hatasız şekilde 
çalıştırılarak BERT yönteminin eğitim işlemi tamamlanmalıdır.Bu işlemler sonucunda
vocab.txt, tokenizer.model, tokenizer.vocab, bert_config.json dosyaları oluşacaktır.
Aynı zamanda eğitim işlemi sonucunda model dosyalarını oluşturacağımız
checkpoint dosyaları oluşacaktır.

2)Öncelikle bert_model isimli bir dizin oluşturulmalıdır. Daha sonra bu dizinin 
içerisinde model ve working isimli iki dizin oluşturulmalıdır.
Ardından vocab.txt, tokenizer.model ve tokenizer.vocab dosyaları model dizininin
altına kopyalanmaldır.Checkpoint dosyaları ve bert_config.json dosyası working
dizininin altına kopyalanmalıdır.

3)BERT dizini altındaki createModelFile.py dosyası bir önceki adımda oluşturulan
bert_model dizininin altına kopyalanmalıdır. Checkpoint dosyalarında 
model.ckpt ifadesinden sonra yazan training step değerleri silinmelidir.Ardından
createModelFile.py dosyası çalıştırılarak working dizini altında model dosyasının 
oluşturulması sağlanır. Artık BERT yöntemi çalışmaya hazır hale gelmiştir.

4)BERT dizini altındaki bertTest.py dosyası bert_model dizini altına
kopyalanarak çalıştırılıp BERT yöntemi test edilebilir.

***BAŞARI ÖLÇÜMLERİ***
Markov Chain ve BERT yöntemlerinin test kodları çalıştırıldığında her bir maskelenmiş
kelime için en yüksek olasılığa sahip 5 tahmin sonuç dosyalarına yazdırılmaktadır.
Başarı oranları calculateAccuracy.py dosyasına ilgili sonuç
dosyasının yolu verilerek hesaplanabilir.






