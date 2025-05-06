# POS Etiketleme Şeması (Part-of-Speech Tagset)

Bu belge, Türkçe metinler için kullanılacak olan sözcük türü etiketlerini tanımlar. Etiketler Universal POS Tagset (UD v2) temel alınarak sadeleştirilmiş ve Türkçeye özel bazı açıklamalarla zenginleştirilmiştir.

---

## Etiket Listesi

| Etiket  | Açıklama                        | Örnekler              |
|---------|----------------------------------|------------------------|
| `NOUN`  | İsim                             | kitap, masa, çocuk     |
| `PROPN` | Özel isim                        | Ankara, Ahmet, Türkiye |
| `PRON`  | Zamir                            | ben, sen, o, biz       |
| `VERB`  | Fiil                             | gitmek, koşuyor        |
| `AUX`   | Yardımcı fiil                    | olmak, edilmek         |
| `ADJ`   | Sıfat                            | güzel, kırmızı         |
| `ADV`   | Zarf                             | hızlıca, az, çok       |
| `ADP`   | İlgeç / edat                     | için, ile, gibi        |
| `CCONJ` | Eşdizimli bağlaç                 | ve, ya da, ama         |
| `SCONJ` | Bağlaç (yan cümle bağlayan)      | çünkü, diye, ki        |
| `DET`   | Belirleyici                      | bir, bu, şu, o         |
| `NUM`   | Sayı                             | bir, iki, 2023         |
| `PART`  | Edat / ek-fiil parçası           | -miş, -di, -se         |
| `INTJ`  | Ünlem                            | ah, eyvah, selam       |
| `PUNCT` | Noktalama işareti                | ., !, ?                |
| `SYM`   | Sembol                           | +, %, ₺                |
| `X`     | Belirsiz / tanımsız öğe          | @morning, unknown_tag  |

---

## Açıklamalar

- `AUX` sadece yardımcı fiiller için kullanılmalıdır: *olmak, edilmek, kılınmak...*
- `PROPN` yalnızca özel isimler için ayrılmıştır. İlk harfi büyük ama özel olmayan kelimeler (örn. başlıklar) `NOUN` olabilir.
- `PART` özellikle Türkçede **ek-fiil** ve **kip/şart** gibi dil bilgisel ekleri kapsar.
- `X` etiketi sadece çok belirsiz ya da bozuk verilerde kullanılmalıdır.
- `PUNCT` etiketi tüm noktalama işaretlerini kapsar ama `SYM` sembollerle (örn. ₺, %, ±) sınırlıdır.

---

## Kaynaklar

- Universal Dependencies v2: https://universaldependencies.org/u/pos/
- Türkçe UD Kılavuzu: [https://universaldependencies.org/tr/](https://universaldependencies.org/tr/)

---

## Etiketleme Örneği

```tsv
Ankara   PROPN
büyük    ADJ
bir      DET
şehirdir NOUN
.        PUNCT
```

## Not

Bu belge zamanla geliştirilecektir. Yeni etiket ihtiyaçları ya da hata düzeltmeleri için katkılarınızı bekliyoruz.