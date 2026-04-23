# 🌸 CrewAI Haiku Üretici (Haiku Generator)

Bu proje, **CrewAI** çerçevesini kullanarak otonom yapay zeka ajanlarının işbirliği içerisinde yaratıcı Haiku şiirleri üretmesini sağlayan bir Python uygulamasıdır. Uygulama, konu belirleme ve şiir yazma süreçlerini iki farklı uzman ajana bölerek yüksek kaliteli ve tematik sonuçlar elde etmeyi hedefler.

## 🚀 Proje Hakkında

Haiku, geleneksel bir Japon şiir türüdür ve genellikle 5-7-5 hece ölçüsüyle yazılır. Bu projede, bir ajan en uygun ve ilgi çekici konuyu bulurken, diğer ajan bu konuyu sanatsal bir dille Haiku formuna dönüştürür.

## 🤖 Roller ve Ajan Yapısı

Sistem, belirli görevlerde uzmanlaşmış iki ana ajandan oluşmaktadır:

### 1. HaikuTopicFinder (Konu Kaşifi)
* **Görevi:** Haiku yazımı için ilham verici, doğa odaklı veya derinliği olan spesifik bir konu/tema bulmak.
* **Yetkinlik:** Mevsimsel değişimleri, anlık duyguları ve görsel imgeleri analiz ederek yazara en iyi temayı sunar.

### 2. HaikuWriter (Haiku Yazarı)
* **Görevi:** Kendisine iletilen konuyu temel alarak 5-7-5 kuralına uygun (veya modern serbest formda) estetik bir Haiku yazmak.
* **Yetkinlik:** Dil kullanımı, kelime seçimi ve kısa formda derin anlamlar yaratma konusunda uzmanlaşmıştır.

## 📋 Görev Tanımları (Tasks)

Proje akışı aşağıdaki iki temel görev üzerinden ilerler:

1.  **FindHaikuTopic:** `HaikuTopicFinder` ajanı tarafından yürütülür. Güncel veya zamansız bir tema belirler (Örn: "Sonbaharın ilk yağmuru", "Gece vakti boş bir sokak").
2.  **WriteHaiku:** `HaikuWriter` ajanı, belirlenen temayı alır ve bu temayı işleyen son şiiri oluşturur.

## 🛠️ Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. **Depoyu klonlayın:**
   ```bash
   git clone [https://github.com/kullaniciadi/haiku-crewai.git](https://github.com/kullaniciadi/haiku-crewai.git)
   cd haiku-crewai
