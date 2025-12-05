# Akıllı Alışveriş Tavsiye Ajanı
**Proje:** Akıllı Alışveriş Tavsiye Ajanı (Shopping Advice Agent)  
**Geliştirici:** Büşra Uzunlar

## Proje Özeti
Bu proje, Trendyol gibi e-ticaret sitelerinden ürün verisi toplayıp (scraping), çok kriterli bir skorlama motoru ile kullanıcının belirttiği bütçe/önceliklere göre en uygun ürünleri öneren tek ajanlı bir yapay zeka sistemidir. Ajan, Algı–Karar–Eylem (Perception–Decision–Action) ve BDI (Belief–Desire–Intention) prensiplerini kullanır.

## Özellikler
- Trendyol'dan ürün verisi çekme (başlık, fiyat, puan, yorum sayısı vb.)
- Veri temizleme ve normalize etme
- Çok kriterli skorlama motoru (kullanıcı ağırlıklandırılabilir)
- CLI veya basit bir web arayüzüne entegre edilebilecek modüler yapı
- Selenium ile dinamik sayfa desteği (opsiyonel)

## Uyarılar / Etik
- Bu proje akademik amaçlıdır. Web scraping işlemlerinde hedef sitenin `robots.txt` kurallarına, kullanım koşullarına ve yasal gereksinimlere uyulmalıdır.
- Çok sık istek göndermek yerine istek aralarında bekleme (rate limiting) uygulanmalıdır.

## Gereksinimler (Hızlı)
Python 3.9+ önerilir. Tüm paketler `requirements.txt` dosyasında listelenmiştir.

## Kurulum
1. Depoyu klonla:
   ```bash
   git clone https://github.com/busrauzunlar/shoppingAdviceAgent
   cd shoppingAdviceAgent
