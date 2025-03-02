# Türkçe NLP Araçları

## Yapılacaklar Listesi
### Aşama 1: Temel Ön İşleme
- [ ] Tokenizer
- [ ] Lemmatizer
- [ ] Sentence Splitter
- [ ] Normalization

### Aşama 2: Morfolojik Analiz
- [ ] Morphological Analyzer
- [ ] Morphological Disambiguation

### Aşama 3: Sözdizimsel ve Anlamsal İşleme
- [ ] Sözcük Türü Etiketleyici (POS Tagger)
- [ ] Bağımlılık Çözümleyici (Dependency Parser)
- [ ] Özel Ad Varlık Tanıma (NER)
- [ ] Anlam Belirsizliği Giderme (WSD)
- [ ] Anlamsal Rol Etiketleme (SRL)

## Benzer Projeler
[Buradan](https://github.com/agmmnn/turkish-nlp-resources) Türkçe için yapılmış NLP çalışmalarına ulaşabilirsiniz.Ayrıca [Boğaziçi TULAP](https://tulap.cmpe.boun.edu.tr/home?spc.page=2)'ın ve [BOUN-TABI](https://tulap.cmpe.boun.edu.tr/home?spc.page=2)'nin çalışmalarına bakabilirsiniz

## Mevcut Araçlardan Daha İyi Yapabileceklerimiz ve Notlar
### Zemberek-NLP Morfological Analyzer Eksikleri
- **Circumflex words**: Zemberek morfolojik analiz sırasında "â" gibi harflerde sorun yaşıyor.
- **Özel adlar ve kısaltmalar**: Özel adları ve kısaltmaları tanımalama da sorunları var.
- **Informal Words**: Zemberek "okuycam" gibi daha konuşmaya yakın sözcükleri tespit edebiliyor. Bizde bunu eklemeye çalışabiliriz.
- **Ambigiuty**: Zemberek Averaged Perceptron ile ambiguity sorununu çözüyor.

## Araştırma Kaynakları
