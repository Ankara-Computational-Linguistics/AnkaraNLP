### `corpus/README.md`

# Corpus Klasörü

Bu klasör, Ankara NLP projesinin veri işleme ve dil kaynaklarıyla ilgili tüm çalışmalarını barındırır. Türkçe doğal dil işleme araçları geliştirmek için kullanılan veri kümeleri, etiketli örnekler ve veri temizleme/ön işleme betikleri bu dizin altında organize edilmiştir.


## Klasör Yapısı

```bash
corpus/
├── annotated         # Elle veya yarı otomatik olarak etiketlenmiş veriler (POS, NER, morfoloji)
├── cleaned_corpora   # Ham metin verilerinin temizlenmiş, analiz için hazır halleri
└── scripts           # Ham veriyi temizleme, dönüştürme ve bölme işlemleri için Python betikleri
````

---

## Alt Klasör Açıklamaları

### `annotated/`

Bu klasör, üzerinde elle ya da otomatik yöntemlerle yapılmış dilsel etiketlemeleri içerir. Örnek veri türleri:

* **POS (Sözcük Türü) Etiketleri**
* **Morfolojik Etiketlemeler**
* **Varlık Adı Tanıma (NER) Etiketleri**
* **Bağımlılık Ağaçları (ileride eklenebilir)**

Dosya formatı genellikle `.tsv`, `.json`, `.conllu` veya `.txt` şeklindedir.

---

### `cleaned_corpora/`

Türkçeye ait ham metinlerin temel temizleme işlemlerinden geçirilmiş halleri bu dizinde yer alır. Bu dosyalar:

* Özel karakterlerden arındırılmış
* Unicode normalize edilmiş
* Gerekirse cümlelere veya kelimelere bölünmüş
  şekilde sunulur.

Kaynaklar arasında gazete makaleleri, romanlar, kamuya açık veritabanları ve web kazıma sonuçları olabilir.

---

### `scripts/`

Veri işleme sürecinde kullanılan tüm Python betikleri burada bulunur. Betiklerdeki başlıca görevler:

* Metin temizleme (boşluk düzeltme, karakter filtresi vb.)
* Veri formatlama (.txt → .json/.conllu dönüşümü)
* Otomatik etiketleme (örnekleme, önişleme pipeline'ları)
* Segmentasyon ya da corpus bölme işlemleri

Her betik içinde ne yaptığına dair kısa bir açıklama (`docstring`) bulunmalıdır.

---

## Geliştirme Notları

* Bu klasördeki dosyalar sürekli güncellenmektedir.
* Yeni veri eklerken veya betik yazarken `README.md` dosyasını da güncellemeyi unutmayınız.
* Etiketleme işlemlerinde kullanılacak şemaların (`tagset`) ayrı belgelenmesi önerilir.

---

## İletişim

Veri katkısı yapmak veya öneride bulunmak için: [arda@artadosearch.com](mailto:arda@artadosearch.com) veya [ardam1425@gmail.com](mailto:ardam1425@gmail.com)