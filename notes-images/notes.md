# Huawei Ai Kurs Notları

# Ai Overview

Symbolism:   
Connectionism: Simple processing yerine nöronlar kullanılmalı.  
Behaviorism: Çevreyle etkileşim yaptıkça ai kendini geliştirebilir.

**Strong AI:** Bu görüş gerçek problemi çözebilen makineler olabilir der, self aware ve zeki modeller.  
**Weak AI**: Zeki görünürler ama aslında gerçek problemleri çözemezler. Self awareness yoktur.

**4 element:** data, algorithm, computing power, scenario.  
Bunlar için de ai ile cloud computing, big data, IoT gibi konuları birleştirmeliyiz.

Genel olarak AI teknolojileri:
- Computer vision
- Speech processing
- Natural language processing (NLP)

Bazı kullanım alanları: medikal, retail(market), autonomous driving vs.

**Full Stack:**  
ModelArts workflow, Mindspore (ai computing network), CANN (chip operator library), Da vinci core mimarisi (+ ARM CPU), 

**Endişeler:**  
Privacy issues: Verilerin nerden geldiği ile ilgili gizlilik endişeleri  
Fake images: Görüntülerin gerçek mi fake mi olduğunu anlayamamak  
İşsizlik: Bazı işler ai tarafından devralınabilir  

**Yazılım trendleri:**   
- Frameworks: MindSpore, Tensorflow, Pytorch  
Akademik çalışmalarda pytorch daha çok öne çıkarken, endüstride tensorflow taşıma kolaylığı ile daha çok ön plana çıkmış.  
- Computer vision: GAN algoritması görüntü üretme   
- NLP field: transformer mimarisi  
-Reinforcement learning field: Alphastar etc.

-> By "all AI scenarios", Huawei means different deployment scenarios for AI, including public clouds, private clouds, edge computing in all forms, industrial IoT devices, and consumer devices.


# Machine Learning Overview

Coverage rate: kurallar gerçek dünya verilerine her zaman uyumlu olmayabilir, how much data do the rules can fit?

**Rule-based method:** elimizde değişen bi veriseti varsa kurallar da buna göre sürekli değişmelidir, bu da çok karmaşık olabilir.  
**Machine learning:** model, verisetini öğrenerek karar verme mekanizmasını, yani kuralları kendi kendine öğrenir.

Kompleks ya da açıklanamayan kurallar, değişen senaryolar, değişen veriler vs. gibi durumlarda makine öğrenmesi tercih edilir.

Fonksiyonun bir ideal mapping function u olmalıdır. source domain X ile target domain Y yi eşler.
Objective function (f): Bu fonksiyon öğrenilir, direkt olarak elde edilemez. 

Başka bir (g) fonksiyonu tanımlayarak f i olabildiğince tahmin etmeye çalışabiliriz. Bu fonksiyon f'e yaklaşan bir tahmini fonksiyondur.

## **Temel Kavramlar**
**AI (Artificial Intelligence), Machine Learning (ML), ve Deep Learning (DL) arasındaki fark nedir?**

1. **Artificial Intelligence (AI):**
   - **Tanım:** Bilgisayarların insan gibi düşünme, öğrenme ve karar verme becerilerine sahip olmasını sağlayan geniş bir teknoloji alanıdır.
   - **Kapsam:** ML ve DL de dahil olmak üzere tüm zeka tabanlı sistemleri içerir.
   - **Örnekler:** Oto-pilot araba, sanal asistanlar (Siri, Alexa), oyun veya strateji oyuncuları.

2. **Machine Learning (ML):**
   - **Tanım:** AI'nin bir alt kümesidir. Bilgisayarların veriden öğrenme ve model oluşturma süreçlerini otomatikleştirir.
   - **Yöntemler:**
     - **Gözlemli Öğrenme (Supervised Learning):** Etiketlenmiş veriler ile eğitilir (ör. spam tespiti).
     - **Gözlemsiz Öğrenme (Unsupervised Learning):** Veri içinde örüntüleri tespit eder (ör. müşteri segmentasyonu).
     - **Takviyeli Öğrenme (Reinforcement Learning):** Ödüller ve cezalar ile öğrenir (ör. AlphaGo).
   - **Örnekler:** Spam filtreleri, tavsiye sistemleri, kredi skoru tahminleri.

3. **Deep Learning (DL):**
   - **Tanım:** ML'nin bir alt kümesidir. Yapay sinir ağları (YSA) kullanarak veriden çözümleri otomatik olarak öğrenir.
   - **Özellikler:**
     - **Derin Ağlar:** Çoklu katmanlı ağlar (ör. CNN, RNN) kullanır.
     - **Otomatik Öznitelik Çıkarımı:** Veri içinden özelliği kendiliğinden öğrenir (ör. resimdeki bir kedinin yüz özelliklerini).
   - **Örnekler:** Görüntü tanıma (DeepFace), konuşma tanıma (Siri), öneri sistemleri.

### **Özet:**
- **AI:** Tüm zeka tabanlı sistemleri kapsar.
- **ML:** AI'nin bir alt kümesidir, veriden öğrenmeyi otomatikleştirir.
- **DL:** ML'nin bir alt kümesidir, derin sinir ağları kullanır ve veriden özelliği kendiliğinden öğrenir.

**Not:** Deep learning, özellikle büyük veri miktarlarında ve karmaşık görevlerde (ör. görüntü ve dil işleme) avantaj sahiptir, ancak geleneksel ML yöntemleri küçük veri setlerinde daha verimli olabilir.


## **Three Major Schools of Thought in AI** (Huawei Confidential belgesine göre):

1. **Symbolism**
   - **Temel Düşünce:** Zekanın sembol işleme (matematiksel kurallar, mantık) ve bilgi temelli bir sürecin ürünü olduğu öne sürülür.
   - **Temsilcileri:** Sembolik sistemler, mantıksal çıkartma, traditional rule-based AI.
   - **Özellik:** Bilgi, kavramlar ve kurallar sembollerle temsil edilir.

2. **Connectionism**
   - **Temel Düşünce:** Zeka, beyin gibi sinir ağları (neuronlar) ve bağlarla çalışır. Sembol işlemine karşı çıkılır.
   - **Temsilcileri:** Yapay sinir ağları (ANN), deep learning.
   - **Özellik:** Otomatik özelliğe çıkarma ve büyük veri miktarı gereklilikleri.

3. **Behaviorism**
   - **Temel Düşünce:** Zeka, algı ve eylem arasındaki doğrudan etkileşim ile oluşur. Bilgi temsili veya çıkartma gerekmez.
   - **Temsilcileri:** Takviyeli öğrenme (RL), adaptasyon mekanizmaları.
   - **Özellik:** Gerçek dünya etkileşimi ve deneyimsellik odaklıdır.

### **Kısaca:**
- **Symbolism:** Kurallar ve sembollerle çalışır (geleneksel AI).
- **Connectionism:** Sinir ağları ve derin öğrenmeyi öne çıkarır.
- **Behaviorism:** Algı-eylem döngüsü ve çevresel etkileşime dayalıdır.

Bu düşünce okulları, AI'nin farklı yaklaşımlarını temellendirir.

## **Ana AI Teknolojileri (Huawei Confidential belgesine göre):**

1. **Bilgisayar Görümü (Computer Vision):**
   - Makinelerin görsel verileri (resimler, videolar) "görerek" anlaması.
   - **Örnekler:** Nesne tespiti, yüz tanıma, otomatik sürüş.

2. **Konuşma İşleme (Speech Processing):**
   - Ses sinyallerini işleme, tanıma ve sentezleme.
   - **Örnekler:** Konuşma tanıma (Siri), makineye sesle komut verme.

3. **Doğal Dil İşleme (NLP - Natural Language Processing):**
   - Bilgisayarların insani dil (metin/konuşma) anlaması.
   - **Örnekler:** Chatbot'lar, dil çevirisi, duygu analiz.

### **Ek Bilgi:**
- **Uygulama Alanları:** Akıllı kentler, sağlık, sanayi 4.0, tüketici deneyimi.
- **Teknolojik Temeller:** Yapay sinir ağları (DL), takviyeli öğrenme (RL), sembolik AI.

## **Huawei'nin Full-Stack AI Stratejisi Adımları Kısaca:**

1. **Chip Enablement (Ascend Serisi):**
   - **Ascend** (NPU tabanlı işlemciler) ve **CANN** (optimizasyon kütüphanesi) ile donanım desteği sağlar.
   - **Ascend-Max, Ascend-Mini, Ascend-Tiny** gibi farklı performans seviyeleri için çözümler sunar.

2. **Framework (MindSpore):**
   - **MindSpore**, device-edge-cloud için uyumlu eğitim/çıkarma (training/inference) çerçevesi sunar.
   - **Automatik paralellik** ve CPU/GPU/Ascend işlemcilerinin desteklenmesi ile esneklik sağlar.

3. **Application Enablement (ModelArts):**
   - **ModelArts**, end-to-end AI hizmetleri (model eğitimi, deploy, optimize) için platform sunar.
   - Ön-integrasyonlu çözümler ve senaryo özgü API'ler sağlar.

### **Özet:**
Huawei, **Ascend işlemcileri** ile donanım, **MindSpore** ile yapısal çerçeve ve **ModelArts** ile uygulama düzeyinde bütünleştirme ile **tüm senaryolar (device-edge-cloud)** için AI çözümleri sunar.

![alt text](notes-images/image-28.png)

## Rule based ve ML
ML (Machine Learning) ve rule-based algoritmalar arasında temel farklar şunlardır:

1. **Öğrenme Yöntemi:**
   - **Rule-based:** Kurallar kullanıcı tarafından elle tanımlanır (örneğin, "eğer yaşı 18'den küçükse izin ver").
   - **ML:** Makineler, eğitim verilerinden otomatik olarak karar kurallarını öğrenir (örneğin, belirli özelliklere göre sınıflandırma).

2. **Veri Tabanlılık:**
   - **Rule-based:** Sabit kurallar kullanır ve veriye bağımlı değildir.
   - **ML:** Veriden öğrenme yapar ve modelin performansı eğitim verilerine bağlıdır.

3. **Kararlılık ve Esneklik:**
   - **Rule-based:** Kurallar değişmez olabilir, ancak karmaşık senaryolarda yetersiz kalabilir.
   - **ML:** Kompleks verileri modellemek için daha esnek olan modeller oluşturur.

4. **Uygulama Alanı:**
   - **Rule-based:** Basit ve belirli kurallar gerektiren problemlere (örneğin, trafik ışıkları) uygundur.
   - **ML:** Büyük veri setlerinde gizli kuralları keşfetmek istenen durumlarda (örneğin, spam tespiti) daha uygun olur.

## ML çözümleri

Machine Learning (ML) temel olarak aşağıdaki türde problemlere çözüm sunar:

1. **Sınıflandırma (Classification):**
   - Veri girişini belirli kategorilere atamak.
   - Örnek: Görüntü sınıflandırma (meme kanseri tespiti).

2. **Regresyon (Regression):**
   - Girdi verileri için sürekli çıktı tahmin etmek.
   - Örnek: Emlak fiyatı tahmini (ev metrekaresi verisi kullanılarak).

3. **Kümeleme (Clustering):**
   - Etiketlenmemiş veri setlerini içsel benzerliklere göre kategorilere ayırmak.
   - Örnek: Kullanıcı profil yönetimi veya görüntü arama.

## ML kategorileri
Machine Learning (ML) sınıfları temel olarak **üç ana kategoriye** ayrılır:

1. **Supervised Learning (Gözlemlenen Öğrenme):**
   - Etiketlenmiş veriler kullanarak model eğitilir.
   - **Sınıflandırma** (örneğin, spam tespiti) ve **regresyon** (örneğin, fiyat tahmini) problemlerinin çözümü için kullanılır.
   - *Örnek:* SVM (Support Vector Machine), Linear Regression.

2. **Unsupervised Learning (Gözlemsiz Öğrenme):**
   - Etiketsiz verilerden modeller öğrenir.
   - **Kümeleme** (örneğin, müşteri segmentasyonu) ve **boyut indirgeme** (örneğin, PCA) gibi problemler için uygundur.
   - *Örnek:* K-Means, DBSCAN.

3. **Reinforcement Learning (Takviyeli Öğrenme):**
   - Eylemlerin sonucuna göre ödüller alarak öğrenme yapar.
   - Oyun oynama robotlar veya öneri sistemlerinde kullanılır.
   - *Örnek:* Q-Learning.

**Ek Not:**
- **Ensemble Yöntemleri** (örneğin, Random Forest, GBDT) veya **Yarı-Gözlemlenen Öğrenme** (örneğin, Semi-Supervised Learning) gibi alt kategoriler de mevcuttur.

### Supervised için:
### **1. Sınıflandırma (Classification) Örnekleri:**
- "*Bir e-posta spam (işlevsiz) mi yoksa normal (işlevsel) mi?*"
- "*Bir hasta meme kanseri riski altında mı?*"
- "*Bir müşteri kredi kartı başvurusu kabul edilecek mi?*"

### **2. Regresyon (Regression) Örnekleri:**
- "*Bu evin fiyatı ne kadar olacaktır?*"
  - **Amaç:** Ev metrekaresi, konum gibi özelliklere göre fiyat tahmini.

- "*Bu arzandaki malın satış miktarı ne olacak?*"
  - **Amaç:** Satış verilerini kullanarak talebi tahmin etmek.
  
---

### Unsupervised için:
### **Clustering (Kümeleme) İçin Örnek Sorular:**

- *"Hangi müşteri grupları benzer alışveriş davranışları sergiliyor?"*
   - **Amaç:** Müşterileri satın aldıkları ürünler, harcadıkları para miktarı ve frekans gibi özelliklere göre segmentlere ayırmak.


### **Feature Selection (Özellik Seçimi) Çeşitleri:**

1. **Filter Methods (Filtre Yöntemleri):**
   - Özelliklerin hedef değişken ile ilişkisini istatistiksel ölçütler kullanarak değerlendirir.
   - *Örnekler:* Chi-Square, ANOVA, Mutual Information.
   - **Avantaj:** Hızlı ve verimlidir.

2. **Wrapper Methods (Sarılayıcı Yöntemleri):**
   - Farklı modellerin performansını kullanarak en iyi özellik kümesini belirler.
   - *Örnekler:* Forward Selection, Backward Elimination.
   - **Avantaj:** Model performansına odaklanır.

3. **Embedded Methods (Gömülü Yöntemler):**
   - Model eğitimi sırasında özelliği seçer.
   - *Örnekler:* **Lasso Regression (L1 regularization)**, Ridge Regression (L2 regularization).
   - **Avantaj:** Model karmaşıklığını azaltır.

**Özet:**
- **Filtreler** hızlı seçer,
- **Sarılayıcılar** model performansına göre seçer,
- **Gömülü yöntemler** model eğitimiyle birlikte seçer.

---

### **Model Validity (Model Doğruluğu) Özeti:**

1. **Genelleştirme Yeteneği (Generalization):**
   - Modelin **yeni verilerde** de iyi performans gösterme özelliğidir.
   - **Genelleştirme hata** (generalization error): Yeni verilerde yapılan hatalar.
   - **Eğitim hatası** (training error): Eğitim verilerinde yapılan hatalar.

2. **Underfitting (Yetersiz Öğrenme):**
   - Model verileri iyi öğrenemez (yüksek eğitim hata).
   - *Örnek:* Çok basit bir model kullanmak.

3. **Overfitting (Aşır Öğrenme):**
   - Model eğitim verilerini mükemmel öğrenir ama yeni verilerde başarısız olur (yüksek genelleştirme hata).
   - *Örnek:* Çok karmaşık bir model kullanmak.

4. **Hedef ve Hipotez Fonksiyonları:**
   - **Target function (f):** Gerçek dünyadaki ideal fonksiyon (bilinmez).
   - **Hypothesis function (g):** Modelin tahmin ettiği fonksiyon (f'nin yaklaşığı).

**Ana Amacı:** **Düşük genelleştirme hata** sağlayan modeller elde etmek.

---

### **Bias ve Variance (Kısaca):**

1. **Bias (Yönelim/Sapma):**
   - Modelin **gerçek fonksiyonu** (target function) taklit etme yeteneğinin yetersizliği.
   - **Çok yüksek bias** (underfitting): Model basit ve hatalı tahminler yapar.
   - *Örnek:* Linear regression kullanıp bir kare fonksiyonu tahmin etmeye çalışmak.

2. **Variance (Varyans):**
   - Modelin **eğitim verilerindeki küçük değişimlere** göre çok hassas olma durumu.
   - **Çok yüksek variance** (overfitting): Model eğitim verilerini kendisi yerine tüm veri kümesini öğrenir.
   - *Örnek:* 1000'nin üzerinde decision tree düğümü kullanmak.

3. **Ideal Model:**
   **Bias ve Variance'ın dengeli olmasına** ihtiyaç vardır.
   - **Düşük bias & düşük variance** → İyi model (örneğin: Random Forest).
   - **Düşük bias & yüksek variance** → Overfitting.
   - **Yüksek bias & düşük variance** → Underfitting.
   - **Yüksek bias & yüksek variance** → Kötü model.

*(Context'teki "Variance and Bias" bölümünden bilgiler kullanılmıştır.)*

**Özet:**
- **Bias** = Modelin hatalı genel kurallar oluşturması.
- **Variance** = Modelin verilerdeki gürültüye çok duyarlı olması.
- **Hedef:** **Dengeyi** bulmak! (Bias-Variance Tradeoff)
  
---

### **Gradient Descent (Görünüm Deseni) Yöntemleri:**

1. **Batch Gradient Descent (BGD - Toplu Görünüm Deseni):**
   - **Tüm eğitim verilerini** kullanarak ağırlıkları günceller.
   - **Daha stabil** ama **yavaş** çalışır (her seferinde tüm veri setini işler).
   - **Uygulama:** Büyük veriler için yetersiz (hesaplama maliyeti yüksek).      

2. **Stochastic Gradient Descent (SGD - Rastgele Görünüm Deseni):**
   - **Her seferinde tek tek veri örneklerini** kullanır.
   - **Hızlı** ancak **gürültülü** (genellikle optimal noktaya titreme ile ulaşır).
   - **Uygulama:** Büyük verilerde tercih edilir (mini-batch SGD ile optimizasyonlar yapılır).

3. **Mini-Batch Gradient Descent (MBGD - Küçük Toplu Görünüm Deseni):**
   - **BGD ve SGD arasında bir dengedir.** Her seferinde **bir grup veri (mini-batch)** kullanır.
   - **Denge:** Hızlı ve daha stabilize çalışır (SGD'den daha az gürültü, BGD'den daha hızlı).
   - **Uygulama:** Genellikle **MBGD tercih edilir** (örneğin, 32-256 örneklik mini-batch'lar).

### **Özet:**
| Yöntem          | Veri Kullanımı       | Hızlılık | Stabilite | Uygulama |
|-----------------|----------------------|----------|-----------|----------|
| **BGD**         | Tüm veriler          | Yavaş    | Yüksek    | Küçük veriler |
| **SGD**         | Tek tek örnekler     | Hızlı    | Düşük     | Büyük veriler |
| **MBGD**        | Mini-batch'lar       | Orta     | Orta       | Genel kullanım |

---

### **Hiperparametreler ve Metodları (Özet):**

#### **1. Hiperparametreler Nedir?**
- **Modelin dışarıdan ayarlanabilen** ayarlarıdır.
- **Parametrelerden farklıdır:** Parametreler modelin eğitim sırasında öğrenilen değerlerdir (örneğin, linear regression'deki katsayılar).
- **Örnekler:**
  - **Lasso/Ridge Regression:** `λ` (landa, ceza terimi).
  - **Neural Network:** Öğrenme hızı (learning rate), batch size, katman sayısı.
  - **SVM:** `C` (ceza parametresi) ve `σ` (çevreleme fonksiyonu).
  - **Random Forest:** Ağaç sayısı.
  - **KNN:** `k` (en yakın komşu sayısı).

#### **2. Hiperparametre Optimizasyon Metodları:**
- **1. Grid Search (İzleme Araması):**
  - **Tüm mümkün kombinasyonları** deneyerek en iyi hiperparametreyi bulur.
  - **Avantaj:** Esnek ve sistematik.
  - **Dezavantaj:** **Çok zaman alıcı** (sayıları fazla olduğunda).
  - **Uygulama:** KNN, SVM gibi basit modellerde kullanılır.

- **2. Random Search (Rastgele Arama):**
  - **Rastgele seçilen hiperparametre kombinasyonları** denenir.
  - **Avantaj:** Grid search'e göre daha hızlı ve genellikle daha iyi sonuçlar verir.

- **3. Bayesian Optimization (Baysiyen Optimizasyon):**
  - **Diğer deneyimlerden öğrenerek** daha iyi adaylar seçer.
  - **Avantaj:** Daha verimli (az sayıda deneme ile iyi sonuçlar verir).

- **4. Gradient-Based Optimization (Gradient Tabanlı Optimizasyon):**
  - **Hiperparametrelerin kayıp fonksiyonuna göre** güncellenmesi.
  - **Uygulama:** Derin öğrenme modellerinde (örneğin, learning rate optimizasyonu).

- **Cross Validation**, modelin performansını doğrulamak için verileri **eğitim seti** ve **doğrulama seti** şeklinde bölerek tekrar tekrar test eden bir yöntemdir. Modeli eğitim setiyle eğitip, doğrulama setiyle test eder.
- **K-Fold CV**, en yaygın kullanılan yöntemdir (örneğin, 5-Fold).    - Veriyi **k adet eşit parçaya** böler (örneğin, k=5).
   - Her seferinde **1 parça doğrulama seti**, **diğer k-1 parça eğitim seti** olur.
   - **k adet farklı model** eğitilir ve ortalama doğrulama başarı oranı hesaplanır.
- **Amacı:** Overfitting riskini azaltarak modelin genel performansını artırmaktır.

---

## Görevler:

**Classification:** Algoritma genel olarak bi f fonksiyonundan sınıflara çıktı veren bir fonksiyondur.  f: R^n -> (1,2,..,k)

**Regression:** Model, veriye göre bir çıktı tahmin etmeye çalışır. Algoritması genel olarak bir çıktı fonksiyonu verir. f: R^n -> R   
Örn. sigorta ücretini tahmin etmeye çalışan bir model. 

**Clustering:** Etiketsiz, büyük bir verisetindeki verileri, içerisindeki benzerliğe göre birçok gruba böler. Aynı kategorideki veriler birbirine daha çok benzer. Örn. image retrieval, user profile management.

Tahmin etme problemleri için %80-%90 olarak classification ve regression kullanılır.

## Çeşitleri

**Supervised learning:** Labeled data. Tangible(elle tutulur, somut) ve intangible(soyut) objeleri sınıfandırmada kullanılır. Obje hakkında bilgi vermeden. 

Product recommendatitons, segment customers based on customer data, diognose a disease etc.

**Unsupervised learning:** Unlabeled data. Makineyi büyük değişken verilere maruz bırakılır. Clustering sıklıkla kullanılır.

**Semi-supervised learning:** Küçük miktarda labeled verinin doğrudan öğrenilmesine yardımcı olmak için büyük miktarda unlabeled veri kullanır. Sınıf videolarından öğrencilerin öğrenme şeklini anlamak vb.

**Reinforcement learning:** Algoritmayı ödül ve ceza yöntemine göre eğitir. Agent, çevresi ile etkileşime girer, doğru ise ödül, yanlış ise ceza verilir.

## Feature Selection
Filter: Filtre metodları modelden bağımsız
Wrapper: Feature subset tanımlamak için bir tahmin modeli kullanır
Embedded: Bu metodlar future selection'u modelin bi yapısı olarak ele alır  

Bias: Beklenen/ortalama tahmin değerinin gerçek değerden ne kadar farklı olduğu

Variance: Tahmin değerinin, her tahminde ortalama değerden ne kadar değiştiği

Dependent variable: tahmin edilecek değer
independent variable: tahmin etmek için kullanılacak değer

# Deep Learning Overview

Derin öğrenme modeli unsupervised feature learning ve feature hierarchy learning'e dayanır.

Feature selection/extraction kısmında daha otomatiktir.

Aktivasyon fonksiyonu:
Sigmoid: Vanishing gradient problem / sigmoid sıfır olduğunda fonksiyon çalışmayı durdurur

# Mainstream Frameworks

-> In TensorFlow 2.x, eager execution is enabled by default. ( )(1.0 points)

# İkinci Kurs

# Neural Networks Quiz

## True or False
The neuron with computing capability at hidden layer is referred to as the computing unit.(1.0 points) - T

Increasing the number of parameters in layers of convolutional networks without increasing their depth will enhance the ability of our model.(1.0 points) - T

Using a deep model expresses a useful preference over the space of functions the model can learn.(1.0 points) -T

Dataset includes features and samples.A feature is used to describe the characteristics of an object.A sample is object or event with many features.(1.0 points) - T

Semi-supervised learning is on the part of the data has labels and others don't have their labels.(1.0 points) - T

If points on the line connected between any two points in the set are also in the set, the set is a convex set.(1.0 points) -T

The backpropagation algorithm can be used by the gradient descent optimization algorithm to adjust neural network weights.(1.0 points) -T

## Single Choice
Follow these operation, Which one is not right?(1.0 points) (A)
- A. BGD is more sensitive to noise than SGD.
- B. Mini-batch gradient descent (MBGD) is used small batch size training dataset to update the weights.
- C. All training data is used for each update to minimize the loss function in BGD.
- D. Only one sample point is considered during each update in SGD.

Which of the following methods can be used to implement backpropagation?(1.0 points) (A)
- A. Chain rule
- B. Computational graph
- C. Cost function
- D. Higher order differential

## Multiple Choices
For AI tasks. We can divide a task into four classes. Which calss is AI task.(1.0 points) (all)
- A. Supervised learning algorithms
- B. Semi-supervisor learning
- C. Reinforcement learning
- D. Unsupervised learning algorithms

Follow these operation, Which one is not right?(1.0 points) (all)
- A. ReLU has a derivative function and allows for backpropagation.
- B. ELU has an extra alpha constant which should be positive number.
- C. Softmax function calculates the probabilities of the event over 'n' different events.
- D. The activation function should be non-linear.

# Image Processing

Sampling: Görüntüdeki piksellerin sayısının azaltılması.
Quantization: Görüntüdeki piksellerin renk sayısının azaltılması. Mesela grayscale'e çevirmek.  
8-bits: 256 renk  
2-bits: 4 renk

![alt text](image.png)

# Image Representation

![alt text](image-1.png)
buradaki matris'e channel denir.

![alt text](image-2.png)

RGB: Red, Green, Blue. Ekranda görüntüleri göstermek için kullanılır. 3 channel içerir. 255 0 0  

HSV: Hue, Saturation, Value  
Burada V: 0-1, S: 0-1, H: 0-360 arasında değişir.

YUV: Luminance (Y) ve chrominance (U, V) bileşenlerinden oluşur. Y ile U,V birbirinden ayrıdır.
Eğer bir görüntü sadece Y bileşenini içeriyorsa, bu görüntü grayscale olarak adlandırılır.

CMYK: Cyan, Magenta, Yellow, Black. CMYK renk uzayı, baskı endüstrisinde yaygın olarak kullanılır. CMY renk uzayı ise RGB'nin tersine dayanır.

![alt text](image-3.png)
Position feature: Görüntüdeki piksellerin konumunu temsil eder.

Connected Region: Görüntüdeki piksellerin birbirine bağlı olduğu bölgeleri temsil eder.

# Image Transformation

Coordinate Transformation: Görüntüdeki piksellerin konumunu değiştirmek için kullanılır. Örneğin, bir görüntüyü döndürmek veya ölçeklendirmek için kullanılabilir. p' = Ap + b şeklinde ifade edilir.

Transpose: Matrisin satırlarını sütunlara, sütunlarını satırlara dönüştürür. Örneğin, A^T.

![alt text](image-4.png)
Mirror: Görüntüyü yatay veya dikey olarak yansıtır. Örneğin, A^M.

![alt text](image-5.png)
Rotate: Görüntüyü belirli bir açıyla döndürür. Örneğin, A^R.

![alt text](image-6.png)
Zooming: Görüntüyü belirli bir ölçekle büyütür veya küçültür. Örneğin, A^Z.

![alt text](image-7.png)
Interpolation: Görüntüdeki piksellerin değerlerini tahmin etmek için kullanılır.
Görüntüdeki (x,y) integer olmalıdır, ama transformasyon sonrası (x,y) float olabilir. Bu durumda interpolation kullanılır.

![alt text](image-8.png)
Grayscale Transformation-Inversion: Görüntüyü grayscale'e dönüştürür. Inversi ise görüntünün renklerini tersine çevirir.

![alt text](image-9.png)
Grayscale Transformation-Contrast Enhancement: Görüntünün kontrastını artırır. Bu, görüntüdeki parlaklık farklarını artırarak daha net bir görüntü elde etmeyi sağlar.

![alt text](image-10.png)
Contrast compression: Görüntünün kontrastını azaltır. Bu, görüntüdeki parlaklık farklarını azaltarak daha yumuşak bir görüntü elde etmeyi sağlar.

![alt text](image-11.png)
Gamma correction: Görüntünün parlaklığını ayarlamak için kullanılır. Gamma değeri, görüntünün parlaklık düzeyini kontrol eder. Gamma değeri 1'den büyükse, görüntü daha parlak olur; 1'den küçükse, görüntü daha karanlık olur.

# Histogram

![alt text](image-12.png)
Histogram of a grayscale image: Grayscale görüntünün histogramı, görüntüdeki piksel değerlerinin dağılımını gösterir. Histogram, görüntüdeki parlaklık düzeylerini analiz etmek için kullanılır. Bütün görüntüdeki piksel değerlerinin sayısını gösterir.

![alt text](image-13.png)
Histogram calculation: Histogram, görüntüdeki piksel değerlerinin dağılımını gösterir. Her piksel değeri için, o değere sahip piksel sayısını hesaplar.

![alt text](image-14.png)
Histogram equalization: Histogram eşitleme, görüntünün kontrastını artırmak için kullanılır. Bu işlem, görüntüdeki piksel değerlerinin dağılımını daha dengeli hale getirir. 

Histogram eşitleme, görüntüdeki düşük kontrastlı bölgeleri aydınlatır ve yüksek kontrastlı bölgeleri karartır. 

Otomatik olarak hesaplar. API çağrısı ile invoke edilir. Generates an image that globally equalized.

![alt text](image-15.png)
Histogram specification: Histogram spesifikasyonu, bir görüntünün histogramını belirli bir hedef histogram ile eşleştirmek için kullanılır. Bu işlem, görüntünün kontrastını artırmak ve belirli bir renk dağılımını elde etmek için kullanılır.

# Filtering

![alt text](image-16.png)
Spatial filtering: Görüntüdeki piksellerin değerlerini komşu piksellerin değerlerine göre değiştirir. Bu, görüntüdeki gürültüyü azaltmak veya kenarları vurgulamak için kullanılır.
N neighbours genellikle bir tek sayı olarak seçilir. Örneğin, 3x3, 5x5 gibi.
central pixel - p

![alt text](image-17.png)
Mean filter: Görüntüdeki piksellerin değerlerini, komşu piksellerin ortalaması ile değiştirir. Bu, görüntüdeki gürültüyü azaltmak için kullanılır. Genellikle blur efektini elde etmek için kullanılır.

Median filter: Görüntüdeki piksellerin değerlerini, komşu piksellerin medyanı ile değiştirir. Bu, görüntüdeki gürültüyü azaltmak için kullanılır. Intensity yi değiştirmez. Özellikle tuz ve biber gürültüsünü azaltmak için etkilidir.

Çok detaylı görüntülerde iyi değildir. Çünkü detayları da kaybeder.

![alt text](image-18.png)
Gaussian filter: Görüntüdeki piksellerin değerlerini, komşu piksellerin Gaussian dağılımına göre değiştirir. Bu, görüntüdeki gürültüyü azaltmak için kullanılır. Gaussian dağılımı, merkezi pikselin etrafındaki piksellere daha fazla ağırlık verir.

![alt text](image-19.png)
Sharpening filter: Görüntüdeki piksellerin değerlerini, komşu piksellerin değerlerine göre değiştirir. Bu, görüntüdeki kenarları vurgulamak için kullanılır. Genellikle blur etkisini azaltmak için kullanılır.
![alt text](image-20.png)
Buradaki operatorler edge detection için de kullanılır.

![alt text](image-21.png)
Affine transformation: Görüntüyü ölçeklendirme, döndürme, yansıtma gibi işlemlerle dönüştürür. Bu, görüntünün geometrik özelliklerini değiştirmek için kullanılır.

![alt text](image-22.png)
Perspective transformation: Görüntüyü perspektif olarak dönüştürür. Bu, görüntünün perspektif özelliklerini değiştirmek için kullanılır. Örneğin, bir görüntüyü farklı bir açıdan görmek için kullanılabilir.

Nonlinear bir transformation'dır. 8 tane parametre ile ifade edilir. 4 tane kaynak nokta ve 4 tane hedef nokta ile ifade edilir.

![alt text](image-23.png)
Color image processing: Farklı kanalları ayrı olarak işler. Sonrasında kanalları birleştirir. Diğer bir yol, her bir pikseli multi dimensional ayrı bir vektör olarak ele alıp, bu vektörleri ayrı ayrı işler.

![alt text](image-24.png)
Brightness enhancement: Görüntünün parlaklığını artırmak için kullanılır. Bu, görüntüdeki piksel değerlerini belirli bir değere ekleyerek veya çıkararak yapılır.

![alt text](image-25.png)
Saturation enhancement: Görüntünün doygunluğunu artırmak için kullanılır. Bu, görüntüdeki renklerin yoğunluğunu artırarak daha canlı renkler elde etmeyi sağlar.

![alt text](image-26.png)
Hue enhancement: Görüntünün rengini değiştirmek için kullanılır. Bu, görüntüdeki renk tonlarını değiştirerek farklı renkler elde etmeyi sağlar.

![alt text](image-27.png)
Data augmentation tipleri: zooming, strecthing, adding noise, flipping, rotation, translation, sheaaring, contrast adjustment, channel transformation ..

# Image Recognition

Precision'u genellikle proportion (oran)'a bakmak istediğimizde kullanırız.
Recall rate i medikal alanda sık kullanırız. Çünkü olabildiğince doğru tahmin yapmak isteriz.

![alt text](image-29.png)
IoU (Intersection over Union): İki nesnenin kesişim alanının, birleşim alanına oranını ölçer. Genellikle nesne tespiti ve segmentasyon problemlerinde kullanılır.

![alt text](image-30.png)
Coonected-region segmentation: Görüntüdeki piksellerin birbirine bağlı olduğu bölgeleri ayırmak için kullanılır. Bu, görüntüdeki nesneleri veya bölgeleri tanımlamak için kullanılır. 

Binary image e çevirir ve boşlukları doldurur. böylece görüntüdeki nesneleri ayırır.

![alt text](image-31.png)

![alt text](image-32.png)
Object detection only needs to detect the object at a certain approximate position, while image segmentation needs to segment the target along the boundary of the target area.

U-net, deeplab

![alt text](image-33.png)
Dice coefficient: İki kümenin benzerliğini ölçmek için kullanılır. Genellikle görüntü segmentasyonu problemlerinde kullanılır. 0 ile 1 arasında bir değer alır. 1, iki kümenin tamamen aynı olduğunu gösterir.

![alt text](image-34.png)
Object tracking: Nesnenin hareketini takip etmek için kullanılır.

![alt text](image-35.png)
Character recognition: Görüntüdeki karakterleri tanımak için kullanılır. Bunları düzenlenebilir hale getirir. Kelime kelime tanır.

Genellikle OCR (Optical Character Recognition) sistemlerinde kullanılır.

Adımları:
- Image processing
- Binarization
- Character segmentation

![alt text](image-36.png)
![alt text](image-37.png)

# Feature Extraction

![alt text](image-38.png)

Downsampling: Görüntüdeki piksellerin sayısını azaltmak için kullanılır. Bu, görüntünün boyutunu küçültmek ve işlem süresini azaltmak için yapılır.

Region of Interest (ROI): Görüntüdeki belirli bir bölgeyi seçmek için kullanılır. Bu, görüntünün belirli bir bölümünü analiz etmek veya işlemek için yapılır.

Feature descriptor: Görüntüdeki belirli özellikleri tanımlamak için kullanılır. Bu, görüntünün belirli bir bölümündeki özellikleri analiz etmek veya işlemek için yapılır.

![alt text](image-40.png)

Thresholding: Görüntüdeki piksellerin değerlerini belirli bir eşik değerine göre değiştirir. Bu, görüntüyü ikili (binary) hale getirmek için kullanılır. Genellikle siyah ve beyaz renkleri ayırmak için kullanılır.

![alt text](image-39.png)

Binarization: Görüntüyü ikili (binary) hale getirmek için kullanılır. Bu, görüntüyü siyah ve beyaz renklerle temsil etmek için yapılır. Genellikle görüntüdeki nesneleri ayırmak için kullanılır.

![alt text](image-41.png)

Bimodal histogram: Görüntüdeki piksel değerlerinin iki farklı tepe noktasına sahip olduğu bir histogramdır. Bu, görüntüdeki nesneleri ayırmak için kullanılır.

If the histogram of an image is flat or has multiple peaks, the threshold cannot be calculated on the histogram.

All possible thresholds need to traversed and the segmentation threshold with the largest intra-class (sınıf içi) is selected as optimal threshold.

# Morphological Operations

![alt text](image-42.png)

![alt text](image-43.png)
Dilation: Görüntüdeki ön plan bölgesini genişletmek için kullanılır. Bu, görüntüdeki nesnelerin boyutunu artırmak veya boşlukları doldurmak için yapılır.

Bir kümenin (A) bir yapısal eleman (B) ile genleştirilmesi (dilation), A’daki ön plan bölgesinin B’nin şekli doğrultusunda genişletilmesi işlemidir.

Buradaki merkez nokta B'dir, B'yi A'nın üzerine kaydırıyoruz. 

![alt text](image-44.png)
Erosion: Görüntüdeki ön plan bölgesini daraltmak için kullanılır. Bu, görüntüdeki nesnelerin boyutunu azaltmak veya gürültüyü azaltmak için yapılır.

Bir kümenin (A) bir yapısal eleman (B) ile erozyonu, A’daki ön plan bölgesinin B’nin şekli doğrultusunda daraltılması işlemidir.

Burada merkez nokta B'dir, B'yi A'nın üzerine kaydırıyoruz. Eğer A, B'yi kapsamıyorsa o bölge daraltılır.

Erosion işlemi, görüntüdeki gürültüyü azaltmak ve nesnelerin kenarlarını netleştirmek için kullanılır.

![alt text](image-45.png)
Opening: Erosion -> Dilation işlemi. Görüntüdeki gürültüyü azaltmak ve nesnelerin kenarlarını netleştirmek için kullanılır.

![alt text](image-46.png)
Closing: Dilation -> Erosion işlemi. Görüntüdeki boşlukları doldurmak ve nesnelerin kenarlarını netleştirmek için kullanılır.

![alt text](image-47.png)
Sliding window: Görüntüdeki pikselleri kaydırarak belirli bir bölgeyi seçmek için kullanılır. Bu, görüntünün belirli bir bölümünü analiz etmek veya işlemek için yapılır.

Çok sık kullanılır. Her seferinde görüntünün tamamını işlemeyiz. 

![alt text](image-48.png)
Template matching: Görüntüdeki belirli bir deseni veya nesneyi bulmak için kullanılır.

When the distance is shorter than the threshold, the template is matched.

# Feature Descriptor

![alt text](image-49.png)

![alt text](image-50.png)
HOG (Histogram of Oriented Gradients): Genellikle nesne tespiti ve görüntü sınıflandırma problemlerinde kullanılır. Görüntüdeki kenarları ve yönleri analiz eder.

Görüntü, farklı hücrelere bölünür. Örneğin, bir hücre 18 sector'e bölünebilir ve her bir sektörün derecesi 20 olabilir. Bu yolla, simetrik sektörleri gruplayarak 9 tane orientation elde edebiliriz.

Örneğin: 80x64 pikselli bir görüntü, 8x8 pikselli bir hücreye bölünebilir. Hücredeki her bir piksel için gradient hesaplanır. Then collect the weights votes of gradient orientation over spatial cells.

![alt text](image-51.png)
Her bir pedestrian (yaya) için özel bir HOG özelliği vardır. Bu yayaların özellikle farklıdır, yani feature descriptor'ları farklıdır. Hedef görüntüdeki yayaları tanımlamak için bu template'ler kullanılabilir.

![alt text](image-52.png)
LBP (Local Binary Patterns): Görüntüdeki piksellerin komşu piksellerle karşılaştırılmasıyla oluşturulan bir özellik tanımlayıcıdır. Genellikle yüz tanıma ve görüntü sınıflandırma problemlerinde kullanılır.

Komşu piksel, merkez piksel değerinden büyükse, 1, küçükse 0 olarak işaretlenir. Bu şekilde, her bir piksel için bir ikili kod oluşturulur.

LBP, görüntüdeki merkez piksel ve komşu piksellerin ilişkisini tanımladığından dolayı görüntüdeki texture (dokusal) özellikleri yakalar.

![alt text](image-53.png)
Haar like features: Bir feature extraction structure'dır. Basit yapıları tanımlar (A, B, C, D). Farklı Haar özellikle farklı alanlarla eşleşir. Daha fazla özellik ile görüntünün karakterini anlayabiliriz. Yüz tanımada sık kullanılır.

# CNN

![alt text](image-54.png)

![alt text](image-55.png)
Buradaki convolusion formülleri template match gibi davranır.

![alt text](image-56.png)
![alt text](image-57.png)
![alt text](image-58.png)
Convolution kernel, bir sliding window'dur. Şekildeki gibi kaydırılır. Her kaydırmada bir konvolüsyon işlemi yapılır.

![alt text](image-59.png)
Buradaki filter w0 ve filter w1, birer convolution kernel'dır. Her bir kernel, görüntüdeki farklı özellikleri yakalar. Örneğin, w0 yatay kenarları, w1 dikey kenarları yakalayabilir.

Input volume matrisleri ise, görüntünün 3 channel'ını temsil eder. 3 channel'lı bir görüntüde, her bir channel için ayrı bir konvolüsyon işlemi yapılır. Bu, görüntünün farklı renk kanallarındaki özellikleri yakalamak için kullanılır.

Sonrasında bias eklenir ve bunun sonucu, feature map'teki yerine yazılır. (Output volume kısmı)

# Convolutional Consepts
![alt text](image-60.png)

Convolution kernel: Extracts features from the input image. Kaç tane kernel olduğu, katmanın performansını etkiler.

Kernel size: W x H x D (Width x Height x Depth) boyutunda bir matristir. Bu boyutlar input chanel a bağlıdır. Genellikle sadece W x H boyutları kullanılır.

Feature map: Convolution işlemi sonrası elde edilen matristir. Her bir feature map, farklı bir özelliği temsil eder. Eğer konvolüsyon  mutliple kernel ile yapılırsa, her bir kernel için ayrı bir feature map elde edilir. 

Önemli: Feature map, sıradaki konvolüsyon/pooling işlemleri için bir input olur.

Feature map size:  W x H x D boyutunda bir matristir. Feature map'in boyutunu belirler. Bu, kernel boyutuna ve stride'a bağlıdır.

Konvolüsyon, görüntünün boyutunu küçültecektir. Bunun önüne geçmek için, eğer stride = 1 ise padding kullanılır. 

Stride: Convolution işlemi sırasında kernel'in kaydırılabilme miktarıdır. Eğer kernel her seferinde 1 piksel kaydırılırsa, stride = 1 olur. 

The stride will affect the effect of feature extraction and the size of the feature map. If the stride is larger, the feature map will be smaller.

Zero padding: Convolution işlemi sırasında görüntünün boyutunu korumak için kullanılır. Görüntünün çevresine sıfırlar koyulur.

![alt text](image-61.png)
Image invariance: Görüntünün boyutu, konumu veya açısı değişse bile, modelin aynı özellikleri tanıyabilmesi anlamına gelir. Bu, konvolüsyonel katmanların temel avantajlarından biridir.

![alt text](image-62.png)
Sıradan bir FCN de bu özellik yokken, CNN de vardır.

![alt text](image-63.png)
Local Receptive Field: Lokalden globale geçer. Her nöron lokal bir bölgeyi işler. Bu, modelin daha az parametre ile daha fazla bilgi yakalamasını sağlar. 

![alt text](image-64.png)
Parameter sharing: Her filtre, hesaplama yaparken aynı ağırlıkları kullanır. Bu filtreler görüntüyü tararken bu ağırlıklar sabittir. Position invariance sağlar.

# CNN Architecture
![alt text](image-65.png)

Activation function: Convolution işlemi sonrası elde edilen feature map'in aktivasyon fonksiyonu ile işlenmesi gerekir. Bu, modelin doğrusal olmayan özellikleri öğrenmesini sağlar. Genellikle ReLU (Rectified Linear Unit) kullanılır.

## Convolutional Layer
![alt text](image-66.png)
Convolutional layer, görüntüdeki özellikleri çıkarmak için kullanılır. Bu katman, konvolüsyon işlemi ile görüntüyü işler ve feature map'leri oluşturur.

![alt text](image-67.png)
![alt text](image-68.png)
![alt text](image-69.png)
![alt text](image-70.png)
![alt text](image-71.png)

Daha derine gittikçe, çıkarılan özellikler daha tamamlanmış hale gelir. 5. katmanda, çıkarılan özellikler neredeyse resmin tamamını kapsar. Farklı görüntüler için aynı özellikler çıkarılabilir.

## Pooling Layer
![alt text](image-72.png)
Pooling, Feature map'in boyutunu küçültmek için kullanılır. Bunu yapmak için öncelikle bazı bölgelere ayırır ve maximum veya average değerini hesaplar. Bu, modelin daha az parametre ile daha fazla bilgi yakalamasını sağlar. Downsampling e benzetebiliriz.

Pooling layer, orijinal görüntüdeki hedef özellikleri elde etmemizi sağlar. Bu, son sınıflandırma işlemi için önemlidir.

### Max Pooling
![alt text](image-73.png)
Max pooling, feature map'in her bölgesindeki maksimum değeri alır. Bu, görüntüdeki en belirgin özellikleri yakalamak için kullanılır.

## Fully Connected Layer
![alt text](image-74.png)
Fully connected layer, feature map'in son katmanıdır. Bu katman, feature map'i düzleştirir (lineer ve uzun bir vektör) ve her bir nöronun tüm nöronlarla bağlantılı olduğu bir yapıya dönüştürür. 

Bu, modelin sınıflandırma işlemini gerçekleştirmesini sağlar. Classifier olarak çalışır. Genellikle final sonucu Softmax aktivasyon fonksiyonu ile verir.

# Datasets, Networks, etc.
![alt text](image-75.png)
![alt text](image-76.png)
Burada görüldüğü gibi, 2014 yılında Image Classification, insan seviyesine ulaştı. Hatta daha altına bile düştü.

![alt text](image-77.png)
ImagenetNet, 2012 yılında ImageNet Large Scale Visual Recognition Challenge (ILSVRC) için oluşturulmuş bir dataset'tir. Bu dataset, 1000 farklı sınıfı içerir ve her sınıf için binlerce görüntü barındırır.

![alt text](image-78.png)
Alexnet, ReLu'nun sigmoid'den daha iyi performans gösterdiğini kanıtladı. 

![alt text](image-79.png)
VGGNet, sadece çok küçük bir kernel kullanarak daha derin bir ağ oluşturdu.

![alt text](image-80.png)
Aradaki en büyük fark, konvolüsyon cell'lerin yapısıdır.

![alt text](image-81.png)
GoogleNet, 3 adet softmax çıkışı içerir. Bu, gradient loss'u önlemek içindir. Ayrıca Global Average Pooling kullanır. Inception yapısı kullanır.

![alt text](image-82.png)
Inception yapısı, farklı boyutlarda konvolüsyon işlemleri yaparak daha fazla özellik çıkarmayı sağlar. 1x1 kernel, ağın non-linearity'sini artırabilir.

![alt text](image-83.png)
ResNet, residual connection kullanarak daha derin ağlar oluşturmayı sağlar. Resnetin en büyük amacı, model derinleştikçe ortaya çıkan degenerate problem'i çözmektir. 

Degenerate problem, ağ, örneğin 10 katmanda en iyi sonucu verecektir, fakat biz ağı 20 katman olarak eğittiğimizde, 10 katmanlı ağdan daha kötü sonuçlar alırız. Bu, ağın daha derinleştikçe öğrenme yeteneğinin azalması anlamına gelir.

![alt text](image-84.png)
Residual connection, bir katmandan sonraki katmana doğrudan bağlantı sağlar. Input ve output'u birleştirir. 

Eğer fonksiyon değeri 0 ise, önemli bir özellik çıkarılamadığı anlaşılır. Ağın optimal fit e eriştiğini gösterir.

![alt text](image-85.png)
Çalışma, SENet bloğu ile ResNeXt bloğunu birleştirerek daha iyi bir performans elde etti. SENet, Squeeze-and-Excitation Network olarak bilinir. GAP kullanır ve Scale operation ile feature map'leri yeniden ölçeklendirir. 

# Quiz
## True or False
Image calculation includes arithmetic operation and coordinate transformation.(1.0 points) - T
```
#### 🔢 Arithmetic Operations
These include pixel-wise operations such as:

- Addition, subtraction, multiplication, and division (e.g. blending images, brightness adjustment)
- Convolution operations (e.g. applying filters or kernels)
- Normalization or scaling of pixel values

#### 📐 Coordinate Transformations
These modify the spatial arrangement of pixels:

- Translation, rotation, scaling, and shearing
- Affine and perspective transformations
- Mapping pixels from one coordinate space to another (e.g. image warping, registration)
```

Traditional image preprocessing methods can be used for data set enhancement.(1.0 points) - T

We can use confusion matrix to measure regression result.(1.0 points) - F
```
A confusion matrix is specifically designed to evaluate the performance of classification models, not regression models. Here's why:

🤔 Why It Doesn't Fit for Regression
- Confusion matrix compares predicted class labels vs true class labels.
- Regression outputs continuous numerical values, not discrete classes.
- There's no straightforward way to define "true positive", "false positive", etc., in the context of continuous values.

✅ What You Use for Regression Instead
You typically use metrics like:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R² Score These assess how close the predicted values are to the actual values.
```

Object detection and object segmentation are the same.(1.0 points) - F
```
🧭 Object Detection
Goal: Identify and locate objects in an image.
Output: Bounding boxes around each detected object with associated class labels.

Example: Drawing rectangles around a dog and a bicycle in a street scene.

🎨 Object Segmentation
Goal: Classify every pixel in an image as belonging to an object or background.

Types:
Semantic segmentation: Labels each pixel by class but doesn’t differentiate between object instances.
Instance segmentation: Labels each pixel and distinguishes between different instances of the same class.

Output: Precise object outlines rather than simple boxes.
```

The sliding window method is commonly used in image precessing.(1.0 points) - T

## Single Choice

When we use gamma correction, the r value is bigger, them image will be ( ).(1.0 points) (A)  
A. Darker   
B. Brighter  
C. No change

```
Gama correction is a nonlinear operation that adjusts the brightness of an image. 
r > 1 -> darker
r < 1 -> brighter
r = 1 -> no change
```

Opening operation means ( ).(1.0 points) (B)  
A. Erosion followed by erosion  
B. Erosion followed by dilation  
C. Dilation followed by dilation  
D. Dilation followed by erosion

```
Opening: Erosion -> Dilation
Closing: Dilation -> Erosion
```

Which of the followings can extract global features？(1.0 points) (B)
A. Convolutional kernel in shadow layer
B. Convolutional kernel in deep layer
C. Pooling layer
D. Fully connected layer

```
Shallow layers (early convolutional layers) extract local features, such as edges, corners, and textures, 
because their receptive field (the area of the input image they "see") is small.

Deep layers (later convolutional layers) have a much larger receptive field due to the stacking of multiple layers. 
This means each neuron in a deep layer can "see" a much larger portion of the input image, sometimes even the whole image.

As a result, deep convolutional kernels can extract global features—such as object shapes,
overall structure, or context—because they aggregate information from the entire image.

Summary:

Shallow layers = local features
Deep layers = global features
Pooling and fully connected layers do not directly extract global features;
pooling reduces spatial size,
and fully connected layers use features already extracted by previous layers.
```

Resnet solve ( ) problem.(1.0 points) (A)
A. Degenerate 
B. Gradient explosion 
C. Gradient loss

## Multiple Choices
Which of the followings are computer vision application scenarios?(1.0 points)  (all)
A. Public security    
B. National defense  
C. Smart transportation  
D. Entertainment

Which of the followings are color space?(1.0 points) (A, B)  
A. YUV  
B. HSV  
C. LBP  
D. SVM  

```
❌ The incorrect options:
C. LBP (Local Binary Patterns):
Not a color space. It's a texture descriptor used in image processing to classify textures.

D. SVM (Support Vector Machine): 
A machine learning algorithm for classification, not related to color representation.
```

Which of the followings are important convolutional concepts？(1.0 points) (all)  
A. kernel size  
B. stride  
C. feature map size  
D. zero padding  

