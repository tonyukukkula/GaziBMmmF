# mrb
Vize için çalışırken alınmış notların internetteki Türkçe içeriğe katkıda bulunma amacı ile yazılmıştır, hataları af buyurunuz. Resimler ilgili bağlantıdaki yer alan oynatma listesindeki videolardan alınmıştır: https://www.youtube.com/playlist?list=PLh9ECzBB8tJOS7WQKdeUaAa5fmPLYAouD
> Kaynak olarak Uraz Hoca'mızın işlediği sunular ve mevzubahis oynatma listesi videoları kullanılmıştır.

Vizeye kadar sorumlu olunan başlıklar(küçük büyük farketmez şekilde listelenmiştir):
<details><summary>Birinci dersin başlıkları</summary>
  
- Database Applications Examples
- Purpose of Database Systems
- Data Models
- Relational Model
- View of Data
- Instances and Schemas
- Physical Data Independence
- Data Definition Language (DDL)
- Data Manipulation Language (DML)
- SQL Query Language
- Database Access from Application Program]
- Database Design
- Database Engine
- Storage Manager
- Query Processor
- Query Processing
- Transaction Management
- Database Architecture
- Database Applications
- Two-tier and three-tier architectures
- Database Users
- Database Administrator
- History of Database Systems
</details>

---
# Birinci Hafta
## Veritabanı Uygulamaları
İşletme bilgileri: satış, muhasebe, insan kaynakları
Üretim: ürün yönetimi, depo, siparişler
Banka: kullanıcı bilgileri, para akışları
Evrenkent(Üniversite): kayıt, not
vb.

## Veritabanı Sistemlerinin Amacı
İlk zamanlarda veritabanı sistemleri, dosya sistemleri üstünde kurulu olurdu. Bundan dolayı birkaç sıkıntıtıya mahal vermiştir:
- Verilerdeki aykırılık(inconsistency) ve çokluk(redudancy) sıkıntıları
  - > Çoklu dosya biçimlerinde tutulduğu için aynı veriden birden çok yerde olma ve bazı verilerin değişirken bazıların değişmemesi suretiyle çıkan sıkıntılar
- Veriye erişim zorluğu(difficulty in accessing data)
  - > Her yeni sorgu için yeni bir program yazılması gerekmesi
- Veri tecriti(data isolation)
  - > çoklu dosyalar ve biçimleri yüzünden
- Bütünlük sıkıntıları (Integrity Problems)
  - > Bütünlük kısıtları(integrity constraints), yeni kısıtlar ekleyeme veya var olan kısıtları değiştirme zorluğu
- Güncelleştirmelerin Atomisitesi (Atomicity of updates)
  - > Hatalar, gerçekleştirilen kısmi güncellemelerle veritabanını tutarsız bir durumda bırakabilir.
- Çoklu kullanıcı tarafından eşzamanlı erişim
  - > Eşzamanlı erişim, performans için gereklidir
  - > Kontrolsuz eşzamanlı erişim tutarsızlığa sebebiyet verir.
- Güvenlik sıkıntıtıları 
Veritabanı sistemleri bu zımbırtıların tümüne çözüm getirmeyi hedefler.

## Veri Taslamları (Data Models)
Veri, veri ilişkileri, veri anlamsallığı(semantic), veri kısıtları(constraints); terimleri açıklamak için gerekli olacaktır.
Taslamlar:
- İlişkisel Taslam (Relational Model)
- E-R Veri taslamı (Entity-Relationship data model)
- Nesne-tabanlı veri taslamı
- Yarı-yapılı veri taslamı (XML)
- Eski taslamlar:
  - Ağ taslamı (network model)
  - Aşamalı taslam (Hierarchical model)

## İlişkisel Taslam(Relational Model)
Burayı ilerde açıklasam daha iyi olur gibi

## DDL
Tabloların oluşturulması ve veri sözlükleri(data dictionary) burada yer almaktadır.

## DML
Sorgular, SQL

## Verinin görüntüsü (View of Data)
![resim](https://user-images.githubusercontent.com/44534126/115115304-64376a80-9f9c-11eb-9a9d-91b6f9c66834.png)\
Resimde görüldüğü üzere mantıksal katman fiziksel katmanın üzerinde yer almaktadır. Mantıksal katmanı #1.7'de belirttiğimiz gibi veritabanının tablolarının ilişkilerini ve yapılarını belirtirdi, görüntü katmanı(view level) mantıksal katmanda belirtilen yapıya uygun tabloların yer aldığı katmandır.


## Örnekler ve Şemalar (Instances and Schemas)
Fiziksel veya mantıksal bir şema oluşumu burada mevzubahistir. Fiziksel şema belleğin nasıl kullanılacağını belirtir, mantıksal şema ise veritabanı tablolarının ilişkileri ve yapılarını belirtir.
Örnek(Instance): Veritabanının anlık görüntüleridir.

Fiziksel veri bağımsızlığı(physical data independence): Üst katmanda tanımlanmış olan mantıksal katman sabitken alttaki fiziksel veri ile işlem yapabilirlik problemidir.

## SQL Sorgu Dili
Sorguların işlenim taslamı: <br/>
![resim](https://user-images.githubusercontent.com/44534126/115115450-3999e180-9f9d-11eb-9bf5-70d599ddba23.png)

Query: Sorgu, `select from X;` gibi.\
Parser and Translator: Sorguyu anahtar kelimelerle parçalar ve çevirir\
Relational-algebra expression: İlişkisel cebir ifadeleri\
Optimizer: R-aE'de oluşan ifadeleri iyileştirir.\
Execution Plan: Çalışım takvimini oluşturur.\
Evaluation Engine: Çalıştırma motoru, veriye erişim olur\
Query Output: Sorgunun çıktısı.

## Veritabanı Kullanıcıları (DB Users)
Tüm olayı özetler: <br/> ![resim](https://user-images.githubusercontent.com/44534126/115115727-a2358e00-9f9e-11eb-8fdc-8610d3ddad52.png)

## Veritabanı Mimarisi (Database Architecture)
Tüm olayı özetler: (Bazılarına düzgün karşılık düşünemedim) <br/> ![resim](https://user-images.githubusercontent.com/44534126/115115866-63ec9e80-9f9f-11eb-8bdf-96303683e976.png)
<br/>
Query Processor: Sorguların işlendiği katman, Sorgu İşlemcisi\
Storage Manager: Verinin tutulduğu katman (hafızanın hangi alanında olduğu bilgisi)\
Disk Storage: İndisler, kayıtlar, veri sözlükleri gibi bilgiler tutulur.

**Veritabanı Mimarileri:**
- Merkezi (Centralized)
  - > Merkezi bir sistem vardır
- İstemci-Sunucu (Client-server)
  - > İstemci ve sunucu arasında mesafe vardır
- Paralel
  - > Çok çekirdekli sistemler üzerinde çalışırlar
- Distributed
  - > Tablolar dağınıktır

**Two-tier ve Three-Tier  mimarileri**<br/>
Buradaki ayrım istemci-sunucu arasındaki katmanlarda sunucu kısmında kaç basamak olduğudur.<br/>
![resim](https://user-images.githubusercontent.com/44534126/115116306-88e21100-9fa1-11eb-876e-fe65c3867d2f.png)<br/>
<br/>günümüzde tatavası yapılan mimari three-tier'dır.

---
# İkinci Hafta
