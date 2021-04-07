**KANONİK VE STANDART FORMLAR DEVAM**

**Maxtermlerin Çarpımı**

Lojik ifadeler, çarpımlar toplamı ya da toplamlar çarpımı formunda ifade
edilebilirvearalarındadönüşümleriyapılabilir.

• **Çarpımlar Toplamı Formu:** Çarpımlar toplamı formu, değişkenlerin
çarpımlarından vebu çarpımların toplamlarındanoluşur. Değişkenlerin ise
ya normal ya da tümleyen formları olur. Çarpım terimleri, değişkenlerin
tamamını içermek zorunda değildir.

<img src="media/image1.PNG" style="width:6.27554in;height:3.30029in" />

ABC+A’B+BC’D’ veya A’+AB+BC’ ifadeleri çarpımlar toplamı formundadır.
Oysa birden fazla değişkenin tümleyenini içeren terimler varsa çarpımlar
toplamı formundadır diyemeyiz; Standart toplamlar çarpımı şeklinde ifade
edilmiş bir lojik ifadedeki her terim maxterm ismiyle anılır.

**Örnek**:F(A,B,C)=A.B’+A.C lojik ifadesini standart çarpımlar toplamı
biçiminde elde etmek istersek,

ifadedeki birinci terimi (C+C’) ile ikinci terimide(B+B’) ile
genişletmemiz gerekir.(Eksik değişkenleri tamamlamaya çalışıyoruz. Aynı
zamanda işlemin sonucunu değiştirmediği için genişletme yapmış
oluyoruz.).

AB’+AC = AB’(C+C’)+A(B+B’)C = AB’C+AB’C’+ABC+AB’C

= AB’C+AB’C’+ABC

***- Üç değişkene sahip bir lojik ifade 8 adet maxterm(23) içerir.***

***- Bu maxtermler girişlerin sadece belli bir kombinasyonunda 0
değerini alır. Maxtermler Mindis ile ifade edilirler.***

***-İndis, maxtermin değerini 0 yapan değişken kombinasyonunun decimal
değeridir. Ayrıca maxtermler, mintermlerin değili olarak da
düşünülebilir.***

<img src="media/image2.PNG" style="width:6.3in;height:4.30833in" />

**Örnek**: F(A,B,C)=AB’C+A’BC+AB’C’+ABC+A’B’C standart çarpımlar toplamı
biçiminde verilmiş lojik ifadeyi standart toplamlar çarpımı formuna
dönüştürelim.

Çarpım terimlerini 1 yapan kombinasyonlar; 101,011,100,111,001dir.

F(A,B,C)= (A+B+C).(A+B’+C).(A’+B’+C) Ayrıca F(A,B,C) fonksiyonu
mintermler cinsinden Σ(1,3,4,5,7)şeklinde de ifade edilebilir. Bu
mintermler dışındaki kombinasyonlar, maxtermleri oluşturur.

F(A,B,C)= Σ(1,3,4,5,7) = Π(0,2,6) yazılabilir.

**KAPI SEVİYESİNDE SADELEŞTİRME**

**Harita Yöntemi**

<img src="media/image3.PNG" style="width:6.3in;height:2.91806in" />

-   ***2 değişkenli karnaugh haritası :*** Bu kutu tipi dijital devrede
    iki tane giriş olduğu zaman kullanılır. Ayrıca karnaugh haritası 2^2
    =4 adet kutucuğa sahiptir.

> <img src="media/image4.png" style="width:1.90652in;height:1.50021in" />

<img src="media/image5.PNG" style="width:6.3in;height:4.13056in" />

-   ***3 değişkenli karnaugh haritası :*** Bu kutu tipi dijital devrede
    üç tane giriş olduğu zaman kullanılır. Ayrıca karnaugh haritası 2^3
    =8 adet kutucuğa
    sahiptir.<img src="media/image6.png" style="width:2.29199in;height:1.39603in" />

<img src="media/image7.PNG" style="width:6.3in;height:4.41736in" />

<img src="media/image8.PNG" style="width:6.3in;height:4.23056in" />

<img src="media/image9.PNG" style="width:6.3in;height:4.29514in" />

<img src="media/image10.PNG" style="width:6.3in;height:4.08958in" />

-   ***4 değişkenli karnaugh haritası :*** Bu kutu tipi dijital devrede
    dört tane giriş olduğu zaman kullanılır. Ayrıca karnaugh haritası
    2^4 =16 adet kutucuğa sahiptir.

<img src="media/image11.png" style="width:2.48993in;height:2.417in" />

<img src="media/image12.PNG" style="width:6.3in;height:3.65833in" />

<img src="media/image13.PNG" style="width:6.3in;height:4.45417in" /><img src="media/image14.PNG" style="width:6.3in;height:4.38819in" /><img src="media/image15.PNG" style="width:5.59167in;height:3.93549in" />

**HARİTA ÜZERİNDE BİRLEŞTİRME KURALLARI**

<img src="media/image16.PNG" style="width:6.3in;height:4.65in" />

<img src="media/image17.PNG" style="width:6.3in;height:4.30208in" /><img src="media/image18.PNG" style="width:6.3in;height:4.75764in" /><img src="media/image19.PNG" style="width:6.3in;height:4.57431in" />

ÖRNEKLER

<img src="media/image20.PNG" style="width:3.0836in;height:2.67523in" /><img src="media/image21.PNG" style="width:2.56689in;height:2.52522in" /><img src="media/image22.PNG" style="width:2.7419in;height:2.94192in" /><img src="media/image23.PNG" style="width:3.20028in;height:3.95868in" /><img src="media/image24.PNG" style="width:3.15in;height:2.77345in" /><img src="media/image25.PNG" style="width:3.08071in;height:2.89167in" />

**Quine McCluskey Yöntemi**

<img src="media/image26.PNG" style="width:6.3in;height:5.17593in" />

<img src="media/image27.PNG" style="width:6.3in;height:4.34028in" /><img src="media/image28.PNG" style="width:6.3in;height:3.38125in" />
