# Değerlendirme ve Karşılaştırmalar (`evaluation/`)

Bu klasör, Ankara NLP projesinde geliştirilen modellerin değerlendirme sonuçlarını, karşılaştırmalı analizlerini ve hata incelemelerini içerir. Model kalitesini sistematik ve tekrarlanabilir bir şekilde ölçmek için kullanılır.

## Klasör Yapısı ve İçerikler

| Dosya / Klasör        | Açıklama                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `metrics/`            | Model performans metrikleri (accuracy, F1, precision, recall vb.).                                                                                           |
| `comparisons/`        | Farklı model/sürüm sonuçlarının karşılaştırmalı analizleri.                                                                                                  |
| `error_analysis/`     | Hatalı tahminler üzerine analizler, yanlış sınıflandırma örnekleri.                                                                                          |
| `visualizations/`     | Grafiksel raporlar, confusion matrix, etiket dağılımı vs.                                                                                                    |
| `evaluation_scripts/` | Değerlendirme işlemleri için kullanılan Python betikleri.                                                                                                    |
| `benchmarks/`         | Modellerin belirli veri setleri (örn. Universal Dependencies, Türkçe BOUN Treebank) üzerindeki skorları. Karşılaştırmalı benchmark verileri burada saklanır. |

## Amaç

- Geliştirilen modellerin güçlü ve zayıf yönlerini belirlemek
- Farklı yöntemlerin karşılaştırmasını yapmak
- Hataları analiz ederek gelecekteki geliştirmelere yön vermek
- Sonuçları şeffaf ve yeniden üretilebilir şekilde sunmak

## Örnek Değerlendirme Metrikleri

- **Accuracy**
- **Precision / Recall / F1-Score**
- **Per-label breakdown (ör. her POS etiketi için ayrı F1)**
- **Confusion Matrix**
- **AUC / ROC (uygun durumlarda)**

## Kullanım Önerisi

- Her model eğitimi sonrası çıktılar bu klasöre kaydedilmelidir.
- Karşılaştırmalar tarih etiketli dosyalarla versiyonlanmalıdır.
- `evaluation_scripts/` altındaki betikler ile skor hesaplamaları ve hata analizleri otomatikleştirilebilir.

## Not

Bu klasördeki veriler sadece son çıktılarla sınırlı kalmamalı; aynı zamanda model geliştirmenin yönünü belirleyecek analizleri de içermelidir. Görselleştirme araçlarının kullanılması önerilir.

