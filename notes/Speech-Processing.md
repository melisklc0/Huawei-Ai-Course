# Intro
![alt text](../notes-images/image-86.png)
Sol kısım speech processing, sağ kısım natural language processing (NLP).

Speech processing, ses sinyallerinin işlenmesi ve analizi ile ilgilenir. Bu, konuşma tanıma, konuşma sentezi ve sesli komut sistemlerini içerir.

NLP ise doğal dilin (yazılı veya sözlü) işlenmesi ve analizi ile ilgilenir. Bu, metin madenciliği, duygu analizi ve dil modelleme gibi görevleri içerir.

![alt text](../notes-images/image-87.png)
![alt text](../notes-images/image-88.png)
![alt text](../notes-images/image-89.png)

Speech synthesis, metin verilerini sesli hale getirme işlemidir. Bu, text-to-speech (TTS) sistemleri ile gerçekleştirilir.

![alt text](../notes-images/image-90.png)
![alt text](../notes-images/image-91.png)

# GMM

![alt text](../notes-images/image-92.png)
Gaussian Distribution, sürekli bir rastgele değişkenin dağılımını modellemek için kullanılır. GMM, birden fazla Gaussian dağılımının bir kombinasyonudur ve karmaşık veri setlerini modellemek için kullanılır.

Probability Density Function (PDF), bir sürekli rastgele değişkenin belirli bir değeri alma olasılığını gösterir. GMM'de, her bir Gaussian dağılımının PDF'si, modelin toplam PDF'sini oluşturur.

![alt text](../notes-images/image-100.png)
Standart deviation (standart sapma), bir dağılımın ne kadar yayıldığını gösteren bir ölçüdür. Standart sapma düşükse, grafik daha dar ve yüksekse daha geniş olur.

![alt text](../notes-images/image-93.png)
Maximum Likelihood Estimation (MLE), model parametrelerini, verilerin olasılığını maksimize edecek şekilde tahmin etmek için kullanılır. GMM'de, MLE, her bir Gaussian dağılımının parametrelerini (ortalama ve varyans) tahmin etmek için kullanılır.

Çünkü gerçek bir projede yalnızca veriye sahip olup parametreleri bilmeyebiliriz. Bu noktada bu parametre tahminini nasıl yaptığımız önemlidir. 

Mean and varience iki önemli parametredir. Mean, dağılımın ortalamasını, varyans ise dağılımın ne kadar yayıldığını gösterir.

![alt text](../notes-images/image-94.png)
Genellikle tek noktanın olasılığı düşüktür, 0.5, 0.3 gibi. Birçok çarpım sonrası veriseti iyice küçülür. Bu yüzden verinin logaritması alınır. Buna log likelihood denir.

Log likelihood, extreme point in konumunu değiştirmez.

![alt text](../notes-images/image-95.png)
Likelihood, autnenticity ölçüsüdür. Modelin veriyi ne kadar iyi açıkladığını gösterir. Likelihood, modelin parametrelerini optimize etmek için kullanılır.
Probability, 

![alt text](../notes-images/image-96.png)

![alt text](../notes-images/image-97.png)
Mixture model, k-sub distribution'un bir araya gelerek tek bir model oluşturduğu bir yapıdır. GMM, bu tür bir modeldir ve her bir bileşen Gaussian dağılımı olarak temsil edilir.

![alt text](../notes-images/image-98.png)
GMM, Mixture of Gaussians (MOG) olarak da tanımlanabilir. MOG, birden fazla Gaussian dağılımının bir araya gelerek karmaşık bir dağılım oluşturduğu bir yapıdır. 

![alt text](../notes-images/image-99.png)

Peki parametleri bilmiyorsak?

![alt text](../notes-images/image-101.png)
Parametreleri bilmiyorsak likelihood kullanamayız. Çünkü likelihood, parametrelerin bilindiği varsayımıyla çalışır. Bu durumda, Expectation-Maximization (EM) algoritması kullanılır.
![alt text](../notes-images/image-102.png)
İteratif bir algoritmadır. Gizli değişkenler kullanır.

![alt text](../notes-images/image-103.png)
- E-step: Şuanki parametrelere bakarak her verinin hangi dağılıma ait olduğunu tahmin ederiz.   
- M-step: Tahmin edilen dağılımlara göre parametreleri tekrar hesaplar ve güncelleriz.  
- Iteration: E ve M adımlarını tekrarlayarak parametreleri optimize ederiz.  
   
Bu yöntem, maksimum global value nun bulunabileceğini garanti etmez. Ancak, genellikle iyi sonuçlar verir.

![alt text](../notes-images/image-104.png)
![alt text](../notes-images/image-105.png)

# HMM
![alt text](../notes-images/image-106.png)
Random walk: A series of processing algorithm for a long sequence.
![alt text](../notes-images/image-107.png)
![alt text](../notes-images/image-108.png)
![alt text](../notes-images/image-109.png)
Markov Chain, bir sistemin gelecekteki durumunun yalnızca mevcut duruma bağlı olduğu bir modeldir. Yani, geçmiş durumlar gelecekteki durumu etkilemez.
![alt text](../notes-images/image-110.png)
![alt text](../notes-images/image-111.png)

![alt text](../notes-images/image-112.png)
Hidden Markov Model (HMM), gözlemlenemeyen (gizli) durumların olduğu bir Markov modelidir. HMM, gözlemlenen verilerin gizli durumlar tarafından üretildiği varsayımıyla çalışır.

![alt text](../notes-images/image-113.png)
![alt text](../notes-images/image-114.png)
Three issues of HMM:
1. **Evaluation**: Gözlemlenen verilerin gizli durumlar tarafından nasıl üretildiğini değerlendirmek için kullanılır. 
2. **Decoding**: Gizli durumların gözlemlenen verilerle nasıl eşleştirileceğini bulmak için kullanılır. 
3. **Learning**: Gizli durumların ve model parametrelerinin nasıl öğrenileceğini bulmak için kullanılır.

## HMM Evaluation
![alt text](../notes-images/image-115.png)
![alt text](../notes-images/image-116.png)

## HMM Learning

![alt text](../notes-images/image-117.png)
Bu algoritma, hidden state varsa kullanılır.

![alt text](../notes-images/image-118.png)
Hidden state squence bilinmiyorsa kullanılır.

## HMM Decoding
![alt text](../notes-images/image-119.png)

# GMM-HMM
![alt text](../notes-images/image-120.png)
![alt text](../notes-images/image-121.png)
GMM is responsible for finding the probability of which state a frame of data belongs to. And HMM finds the most likely word sequence accoring to the observation sequence of multi frame state.

![alt text](../notes-images/image-122.png)

# DNN
![alt text](../notes-images/image-123.png)
![alt text](../notes-images/image-124.png)
![alt text](../notes-images/image-125.png)
![alt text](../notes-images/image-126.png)
![alt text](../notes-images/image-127.png)

![alt text](../notes-images/image-128.png)
Overfitting problemi için dropout kullanabiliriz.

![alt text](../notes-images/image-129.png)
![alt text](../notes-images/image-130.png)
LR, direkt olarak öğrenme algoritmasının performansını etkiler.

![alt text](../notes-images/image-131.png)

# Mixed Models
![alt text](../notes-images/image-132.png)
![alt text](../notes-images/image-133.png)

![alt text](../notes-images/image-134.png)
![alt text](../notes-images/image-135.png)

# RNN
![alt text](../notes-images/image-136.png)
![alt text](../notes-images/image-137.png)
Geleneksel GMM-HMM modeli için, MFCC sıklıkla kullanılır. Ama bu, model boyutlarını düşürür.

![alt text](../notes-images/image-138.png)
![alt text](../notes-images/image-139.png)

RNN, can save a context state and even store, learn and express relative information about the context, instead of being limited to space boundries.

Has timing characteristics. Hidden layers between different timings are connected. So it can be used for sequential data. 

![alt text](../notes-images/image-140.png)
![alt text](../notes-images/image-141.png)
There is a link between each hidden layer. 

![alt text](../notes-images/image-142.png)
Burada tanh'yi, hangi bilgilerin tutulacağını ve hangi bilgilerin unutulacağını belirlemek için kullanırız.

![alt text](../notes-images/image-143.png)
Back propagation through time (BPTT), RNN'in öğrenme sürecidir. Bu süreç, zaman içinde geriye doğru yayılma yaparak ağırlıkları günceller.

Sequence length problem, RNN'in uzun dizilerle çalışırken karşılaştığı bir sorundur. Bu, uzun dizilerin öğrenilmesini zorlaştırır ve modelin performansını düşürebilir.

Bu, gradient loss ve gradient explosion problemlerine yol açabilir. 

Bu problemler ortaya çıkarsa, ağırlıklar değişmemiş gibi olur. Öğrenme etkisi olmaz.

# LSTM

![alt text](../notes-images/image-144.png)
LSTM, RNN'in bir türüdür ve uzun dizilerle çalışırken karşılaşılan sorunları çözmek için tasarlanmıştır. LSTM, hücre (cell) durumu ve kapılar kullanarak bilgiyi daha etkili bir şekilde saklar ve işler.

![alt text](../notes-images/image-145.png)
Hücre durumu, LSTM'in temel bileşenidir ve zaman içinde bilgiyi saklar.

![alt text](../notes-images/image-146.png)
Forgot gate, hücre durumundan hangi bilgilerin unutulacağını belirler. 0-1 arası değerler alır. 0, tüm bilgilerin unutulması anlamına gelirken, 1 tüm bilgilerin saklanması anlamına gelir.

![alt text](../notes-images/image-147.png)
Input gate, yeni bilgilerin hücre durumuna eklenmesini kontrol eder. Output gate ise hücre durumunun çıktısını belirler.

![alt text](../notes-images/image-148.png)
Information update, hücre durumunun güncellenmesini sağlar. Bu, unutma ve yeni bilgi ekleme işlemlerini içerir.

![alt text](../notes-images/image-149.png)
Output gate, hücre durumunun çıktısını belirler. Bu, hangi bilginin sonraki katmanlara iletileceğini kontrol eder.

![alt text](../notes-images/image-150.png)

# Overview

![alt text](../notes-images/image-151.png)
![alt text](../notes-images/image-152.png)
![alt text](../notes-images/image-153.png)


# QUIZ

## True/False
Speech processing is TTS.(1.0 points)  (F)
```
Speech processing genel bir alan; sadece TTS (Text-to-Speech) değil, aynı zamanda ASR (Automatic Speech Recognition) gibi konuları da kapsar.
```

probability and likelihood are the same？(1.0 points)  (F)
```
Probability olasılığı ifade eder, likelihood ise model parametreleri verildiğinde gözlenen verinin uygunluğunu ölçer. İkisi farklı kavramdır.
```

An HMM is created for each state. Training samples of the word are used.(1.0 points) (T)

```
HMM’de her state için model oluşturulur, eğitimde örnekler üzerinden geçilir.
```

The DNN is a discrimination model. It can better discriminate annotation categories.(1.0 points) (T)
```
DNN genelde discriminative modeldir (ör. sınıflandırmada), kategorileri ayırt etmede etkilidir.
```

All RNNs have a chain formed by a repeated neural network module.(1.0 points) (T)

```
RNN yapısında tekrar eden hücreler (chain structure) vardır, bu nedenle doğrudur.
```

Initial probability, Transition probability and Transition probability matrix are the three important elements of Markov Chain？(1.0 points) (T)
```
Markov Chain tanımı için başlangıç olasılığı, geçiş olasılıkları ve geçiş matrisi temel bileşenlerdir.
```

## Single Choice
AM means ( ).(1.0 points) (B)  
A. Language Model  
B. Acoustic Model  
C. Analog Model  

The biggest difference between SGD and BGD is ( ). (1.0 points) (B)  
A. loss function  
B. batch size   
C. learning rate  
```
SGD tek örnekle, BGD tüm batch ile güncelleme yapar. Fark batch size’dır.
```

## Multiple Choices
which of the follows belong to Text analysis? (1.0 points) (?)  
A. Text normalization  
B. parameter synthesis  
C. speech analysis  
D. rhythmic analysis   

which of the follows belong to the advantages of GMM? (1.0 points) (A, B, C)  
A. Strong fitting capability  
B. Maximum probability of speech feature matching  
C. The sequence factor cannot be processed.  
D. Linear or approximate linear data cannot be processed 

```
(A) Güçlü fitting yeteneği ✔
(B) Konuşma özelliklerinde olasılık tahmini ✔
(C) Sequence faktörünü işleyememesi dezavantajdır → Bu yanlış, doğru olan sadece (A) ve (B).
(D) Lineer veriyi işleyemez → bu da yanlış.
```

The three issues of the HMM are ( )? (1.0 points) (A, B, C)  
A. Evaluation  
B. Decoding  
C. Learning  
D. Regression   

Which of the followings belong to LSTM? (1.0 points) (B, C, D)  
A. update gate  
B. input gate  
C. output gate  
D. forget gate  

```
Which belong to LSTM → (B. input gate, C. output gate, D. forget gate)
→ LSTM hücrelerinde bu üç gate vardır. 
Update gate GRU’da vardır, LSTM’de yoktur.
```



