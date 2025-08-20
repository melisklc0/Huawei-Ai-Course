# NLP
![alt text](../notes-images/image-154.png)
![alt text](../notes-images/image-155.png)
![alt text](../notes-images/image-156.png)
Semantic: anlamsal 
Lexical: sözcük bilgisi

![alt text](../notes-images/image-157.png)
![alt text](../notes-images/image-158.png)

## Challanges in NLP
![alt text](../notes-images/image-159.png)
ambiguity: çok anlamlılık

![alt text](../notes-images/image-160.png)
![alt text](../notes-images/image-161.png)
![alt text](../notes-images/image-162.png)
![alt text](../notes-images/image-163.png)

![alt text](../notes-images/image-164.png)

# Language Model
![alt text](../notes-images/image-165.png)

![alt text](../notes-images/image-166.png)
![alt text](../notes-images/image-167.png)

Data çoksa yavaşlar, bunun için neural netwok model kullanılabilir.

![alt text](../notes-images/image-168.png)
![alt text](../notes-images/image-169.png)

![alt text](../notes-images/image-170.png)

# Text Vectorization
![alt text](../notes-images/image-171.png)
![alt text](../notes-images/image-172.png)
![alt text](../notes-images/image-173.png)

![alt text](../notes-images/image-174.png)
word2vec: kelimeleri vektörlere dönüştürür, kelimeler arasındaki ilişkileri gösterir.
Nasıl çalışır? 
![alt text](../notes-images/image-175.png)
doc2vec: cümleleri vektörlere dönüştürür, cümleler arasındaki ilişkileri gösterir.

# Common Algorithms
![alt text](../notes-images/image-176.png)
![alt text](../notes-images/image-177.png)
Hidden state 
![alt text](../notes-images/image-178.png)
![alt text](../notes-images/image-179.png)
![alt text](../notes-images/image-180.png)
![alt text](../notes-images/image-181.png)
![alt text](../notes-images/image-182.png)
GRU can choose to copy all the information to minimize the gradient vanishing problem.
![alt text](../notes-images/image-183.png)

# Key Tasks
![alt text](../notes-images/image-184.png)
![alt text](../notes-images/image-185.png)
![alt text](../notes-images/image-186.png)
![alt text](../notes-images/image-187.png)

![alt text](../notes-images/image-188.png)
![alt text](../notes-images/image-189.png)
Capturing the essence of the text. Cümlede blood kelimesi daha çok geçiyor, daha önemli, mantığıyla çalışır.

![alt text](../notes-images/image-190.png)
![alt text](../notes-images/image-191.png)
Linkleri önem sırasına koyar.

![alt text](../notes-images/image-192.png)
Topicler için.

![alt text](../notes-images/image-193.png)
![alt text](../notes-images/image-194.png)
![alt text](../notes-images/image-195.png)

![alt text](../notes-images/image-196.png)

# QUIZ

## True or False
The TextRank algorithm is based on the PageRank algorithm and can be used for keyword extraction and text abstract.(1.0 points) (T)

```
TextRank, Google’ın PageRank algoritmasının bir türevidir.

Kelimeler veya cümleler düğümler (nodes) olarak alınır, aralarındaki bağımlılıklar kenarlar (edges) ile bağlanır.

PageRank gibi, grafikteki düğümlerin önem derecesi hesaplanır.

Bu sayede önemli kelimeler (keyword extraction) veya temel cümleler (text summarization) seçilebilir.
```

The HMM algorithm is a generative model, and the CRF is a discriminant model. Both can be used for sequence labeling.(1.0 points) (T)
```
TextRank, Google’ın PageRank algoritmasının bir türevidir.

Kelimeler veya cümleler düğümler (nodes) olarak alınır, aralarındaki bağımlılıklar kenarlar (edges) ile bağlanır.

PageRank gibi, grafikteki düğümlerin önem derecesi hesaplanır.

Bu sayede önemli kelimeler (keyword extraction) veya temel cümleler (text summarization) seçilebilir.
```

HMM is composed of two random phenomena, one is from the hidden state to the hidden state, and the other is from the hidden state to the observable state.(1.0 points) (T)
```
HMM’nin yapısı iki olasılıklı süreçten oluşur:

Transition probability (A): Gizli durumdan gizli duruma geçiş olasılığı (ör. POS tagging’de isim → fiil geçişi).

Emission probability (B): Gizli durumdan gözlemlenebilir duruma geçiş (ör. “isim” durumunun “kitap” kelimesini üretme olasılığı).

Bu iki süreç birlikte HMM’yi tanımlar.
```

A language model assumes that all possible sentences of a language obey a probability distribution, and the occurrence probability of each sentence adds up to 1.(1.0 points) (T)
```
Dil modeli, tüm olası cümlelerin olasılık dağılımını tanımlar.
Modeldeki tüm cümle olasılıklarının toplamı 1 olmalıdır (olasılık aksiyomları gereği).
```

A goal of statistical language modeling is to learn the joint probability function of sequences of words in a language.(1.0 points) (T)
```
İstatistiksel dil modelleri, kelime dizilerinin ortak olasılığını öğrenmeyi hedefler.
Pratikte doğrudan bu dağılımı öğrenmek zor olduğundan, genellikle zincir kuralı ve n-gram yaklaşımı ile parçalanır:
Bu da next-word prediction, speech recognition, machine translation gibi birçok uygulamanın temelidir.
```

## Single Choice

Which of the following activation functions is used by the forgetting door in the LSTM? (1.0 points) (A)  
A. Sigmoid  
B. Tanh  
C. ReLU  
D. Softmax  

Which of the following statements about the HMM is incorrect? (1.0 points) (D)       
A. HMM learning refers to training model parameters based on labeled samples.    
B. HMM prediction refers to the prediction of the occurrence probability of observation sequences based on model parameters.  
C. HMM decoding is to solve the most possible hidden state sequences based on model parameters and observation sequences.  
D. The Markov feature of the HMM indicates that the occurrence of the state at the next time point is related to all historical states.   

```
HMM’de Markov özelliği, sadece bir önceki durumun sonraki durumu etkilediğini söyler, tüm geçmişi değil.
Markov özelliği:

HMM’de temel varsayım 1. dereceden Markov varsayımıdır.
Yani, bir sonraki durum yalnızca bir önceki duruma bağlıdır.
```

## Multiple Choices

Which of the following are natural language processing applications? (1.0 points) (Hepsi)  
A. Emotion analysis  
B. Text generation  
C. Intelligent Q&A  
D. Machine translation  

Which of the following are keyword extraction methods? (1.0 points) (A, B, C)  
A. TF-IDF  
B. TextRank  
C. LSI/LSA/LDA  
D. HMM  

```
HMM keyword extraction yöntemi değil, daha çok sequence modeling için kullanılır.

A. TF-IDF (Term Frequency – Inverse Document Frequency):
En basit keyword extraction yöntemlerinden biridir.
Sık geçen ama tüm belgelerde yaygın olmayan kelimeleri öne çıkarır.

B. TextRank:
PageRank algoritmasından türetilmiştir.
Kelimeler/cümleler graf düğümleri olarak modellenir, önemli olanlar öne çıkarılır.

C. LSI/LSA/LDA (Latent Semantic Indexing/Analysis, Latent Dirichlet Allocation):
Konu modelleme ve semantik temsil yöntemleridir.
Anahtar kelime çıkarımı için de kullanılabilir.

D. HMM (Hidden Markov Model):
Keyword extraction için kullanılmaz.
Daha çok sequence labeling (ör. POS tagging, NER, konuşma tanıma) için uygundur.
```

Which of the following problems can be solved by the language model? (1.0 points) (A, B, C)  
A. Article continuation  
B. Predict the next word from above  
C. Measure the probability of a sentence  
D. Semantic analysis  

```
Dil modelleri doğrudan semantik analiz yapmaz, ama dolaylı olarak destek olabilir.

A. Article continuation:
Dil modelleri, bir metnin devamını üretebilir.

B. Predict the next word from above:
En temel işlevi budur (next word prediction).

C. Measure the probability of a sentence:
Bir cümlenin olasılığını hesaplamak dil modelinin matematiksel tanımıdır.
Örn: P(“I am a student”) > P(“Student am I a”).

D. Semantic analysis:
Dil modelleri doğrudan semantik analiz yapmaz.
Ama ürettiği dağılımlar semantik analize destek olabilir.
```