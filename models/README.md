# Modeller (`models/`)

Bu klasör, Ankara NLP projesi kapsamında geliştirilen ve eğitilen tüm doğal dil işleme (NLP) modellerini içerir. Her model, kendi klasöründe yapılandırma dosyaları, ağırlık dosyaları, eğitim günlükleri ve kullanım örnekleri ile birlikte sunulur.

## Klasör Yapısı ve İçerikler

| Klasör / Dosya           | Açıklama                                                                 |
|--------------------------|--------------------------------------------------------------------------|
| `pos/`                   | Sözcük türü etiketleme (Part-of-Speech Tagging) modelleri                |
| `ner/`                   | Varlık adı tanıma (Named Entity Recognition) modelleri                   |
| `morphology/`            | Morfolojik çözümleme modelleri                                          |
| `tokenizer/`             | Özelleştirilmiş tokenizasyon modelleri                                   |
| `language_models/`       | Genel amaçlı dil modelleri (örneğin BERT, LSTM tabanlı modeller)         |
| `README.md`              | Bu dosya, modeller klasörü hakkında genel bilgi sağlar                   |

## Amaç

Bu klasör, model geliştirme sürecini sistematik hale getirmek ve her modelin yeniden kullanılabilirliğini, sürümlenmesini ve belgelenmesini kolaylaştırmak için düzenlenmiştir.

## Her Model Klasörü İçinde Olması Önerilen Dosyalar

- `config.json`: Model yapılandırma ayarları
- `model.pt` veya `model.bin`: Eğitilmiş model ağırlıkları
- `training_log.txt`: Eğitim sürecine dair loglar
- `evaluate.py`: Değerlendirme betiği
- `inference_example.py`: Modelin nasıl kullanılacağını gösteren örnek kod

## Notlar

- Her modelin, hangi veri kümesi ile eğitildiği, hangi metriklerle değerlendirildiği ve varsa karşılaştırmalı sonuçları belgelenmelidir.
- Modeller, ilgili klasör altında kendi README dosyasına sahip olmalıdır.
- Büyük boyutlu ağırlık dosyaları harici bir sunucuda saklanıyor olabilir. Bu durumda, model klasöründe indirme bağlantısı belirtilmelidir.

