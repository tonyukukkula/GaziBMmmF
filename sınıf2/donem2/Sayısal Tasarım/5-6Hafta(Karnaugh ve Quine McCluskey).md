**KANONİK VE STANDART FORMLAR DEVAM**

**Maxtermlerin Çarpımı**

Lojik ifadeler, çarpımlar toplamı ya da toplamlar çarpımı formunda ifade
edilebilirvearalarındadönüşümleriyapılabilir.

• **Çarpımlar Toplamı Formu:** Çarpımlar toplamı formu, değişkenlerin
çarpımlarından vebu çarpımların toplamlarındanoluşur. Değişkenlerin ise
ya normal ya da tümleyen formları olur. Çarpım terimleri, değişkenlerin
tamamını içermek zorunda değildir.

![](media/image1.PNG){width="6.275543525809274in"
height="3.3002865266841646in"}

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

***- Üç değişkene sahip bir lojik ifade 8 adet maxterm(23) içerir. ***

***- Bu maxtermler girişlerin sadece belli bir kombinasyonunda 0
değerini alır. Maxtermler Mindis ile ifade edilirler. ***

***-İndis, maxtermin değerini 0 yapan değişken kombinasyonunun decimal
değeridir. Ayrıca maxtermler, mintermlerin değili olarak da
düşünülebilir.***

![](media/image2.PNG){width="6.3in" height="4.308333333333334in"}

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

![](media/image3.PNG){width="6.3in" height="2.9180555555555556in"}

-   ***2 değişkenli karnaugh haritası :*** Bu kutu tipi dijital devrede
    iki tane giriş olduğu zaman kullanılır. Ayrıca karnaugh haritası
    2\^2 =4 adet kutucuğa sahiptir.

> ![](media/image4.png){width="1.906515748031496in"
> height="1.5002088801399824in"}

![](media/image5.PNG){width="6.3in" height="4.1305555555555555in"}

-   ***3 değişkenli karnaugh haritası :*** Bu kutu tipi dijital devrede
    üç tane giriş olduğu zaman kullanılır. Ayrıca karnaugh haritası 2\^3
    =8 adet kutucuğa
    sahiptir.![](media/image6.png){width="2.2919860017497813in"
    height="1.3960279965004374in"}

![](media/image7.PNG){width="6.3in" height="4.417361111111111in"}

![](media/image8.PNG){width="6.3in" height="4.230555555555555in"}

![](media/image9.PNG){width="6.3in" height="4.295138888888889in"}

![](media/image10.PNG){width="6.3in" height="4.089583333333334in"}

-   ***4 değişkenli karnaugh haritası :*** Bu kutu tipi dijital devrede
    dört tane giriş olduğu zaman kullanılır. Ayrıca karnaugh haritası
    2\^4 =16 adet kutucuğa sahiptir.

![](media/image11.png){width="2.489931102362205in"
height="2.4170034995625547in"}

![](media/image12.PNG){width="6.3in" height="3.658333333333333in"}

![](media/image13.PNG){width="6.3in"
height="4.454166666666667in"}![](media/image14.PNG){width="6.3in"
height="4.388194444444444in"}![](media/image15.PNG){width="5.591666666666667in"
height="3.9354932195975505in"}

**HARİTA ÜZERİNDE BİRLEŞTİRME KURALLARI**

![](media/image16.PNG){width="6.3in" height="4.65in"}

![](media/image17.PNG){width="6.3in"
height="4.302083333333333in"}![](media/image18.PNG){width="6.3in"
height="4.757638888888889in"}![](media/image19.PNG){width="6.3in"
height="4.574305555555555in"}

ÖRNEKLER

![](media/image20.PNG){width="3.0836001749781277in"
height="2.6752318460192477in"}![](media/image21.PNG){width="2.5668886701662292in"
height="2.5252187226596674in"}![](media/image22.PNG){width="2.741903980752406in"
height="2.9419214785651793in"}![](media/image23.PNG){width="3.200277777777778in"
height="3.9586767279090114in"}![](media/image24.PNG){width="3.15in"
height="2.7734481627296588in"}![](media/image25.PNG){width="3.0807097550306213in"
height="2.8916666666666666in"}

**Quine McCluskey Yöntemi**

![](media/image26.PNG){width="6.3in" height="5.175925196850394in"}

![](media/image27.PNG){width="6.3in"
height="4.340277777777778in"}![](media/image28.PNG){width="6.3in"
height="3.38125in"}
