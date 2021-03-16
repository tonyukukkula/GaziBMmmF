# <p align="center">  Sayısal Tasarım  </p>

## Sayı Sistemleri
  - Elektronik sistemler analog ve sayısal olmak üzere ikiye ayrılır. 
  - Sayısal kelimesi 'dijital' teriminin karşılığıdır. 
  - Analog sistemlerde elektrik sinyalleri sürekli olarak değişir ve belli sınırlar içinde her değeri alabilirler. Sayısal sistemlerde ise elektriksel sinyaller olduğu gibi iletilmez. Bu sinyallerin yerine bunlara karşı düşen rakamlar iletilir. Sayısal işlemler ikili sayısal işaretler üzerinden işlem yaptığından bu rakamlar 0 ve 1 lerdir.

 <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/1.jpg"> </p>
  
  Elektronikte daha önce analog teknikler kullanılarak yapılan uygulamalar, günümüzde sayısal teknikler kullanılarak yapılmaktadır. Sayısal tekniğin, Analog tekniğe göre tercih edilme nedenleri aşağıdaki gibi özetleyebiliriz.
  
 <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/2.png"> </p>

kaynak : https://diyot.net/analog-ve-sayisal-elektronik-sistemler/


  - Elektronik devreler 4 sayı sisteminden oluşmaktadır. Bunlar;
    1. Decimal (Onlu) Sayı Sistemi
    2. Binary (İkili) Sayı Sistemi
    3. Oktal (Sekizli) Sayı Sistemi
    4. Hexadecimal (Onaltılı) Sayı Sistemi

 ## A. Decimal(Onlu) Sayı Sistemi:
  Decimal(Onlu) Sayı sistemi günlük hayatta kullandığımız 0.1.2.3.4.5.6.7.8.9 rakamlarından oluşur. Decimal(Onlu) Sayı sisteminde her sayı bulunduğu basamağa göre değer alır. Sistemin tabanı 10’dur.<br/>
   Örneğin 128 sayısı;<br/>
 128=1x10² + 2x10¹ + 8x10º<br/>
 128=1x100 + 2x10 + 8x1<br/>
 128=100 + 20 + 8<br/>
  Şeklinde yazılacaktır. Örnekten görüldüğü gibi Decimal(Onlu) bir sayıda her basamak farklı üstel ifadelerle gösterilmiştir. Bu üstel ifade o **basamağın ağırlığı** olarak adlandırılır.
  
 ## B. Binary(İkilik) Sayı Sistemi
   Binary (İkilik) Sayı sisteminin tabanı 2’dir. Ve bu sistemde **sadece “0” ve “1” rakamları** kullanılmaktadır. Binary Sayı sisteminde de Decimal(Onlu) Sayı sisteminde olduğu gibi her sayı bulunduğu basamağın **konum ağırlığı ile çarpılır.**<br/>
   Binary(İkili) sayılar yazılırken en sağdaki basamağa en düşük değerlikli bit **(Least 
 Significant Bit-LSB)**,en soldaki basamağa en yüksek değerlikli bit **(Most Significant Bit-MSB)** adı verilir. 

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni1.png"> </p>

### 1- İkilik Tabandan 10’lu Tabana Çevirme
Binary(ikili) sayıları Decimal(Onlu) sayılara dönüştürürken her bir bit basamak ağırlığı ile çarpılıp bu sonuçların toplanması gerekir.

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni2.png"> </p>

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni3.png"> </p>

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni4.png"> </p>

- Virgüllü sayılarda işlem basamaklarının nasıl olduğunu izlemek için youtube linkine bakabilrisiniz.<br/>
	https://www.youtube.com/watch?v=Lh8ra1E-ZQ4&ab_channel=ElektronikDerslerim

### 2- DECİMAL SAYILARIN BİNARY SAYILARA ÇEVRİLMESİ
Ana sayımızın  bölümü 0 olana kadar 2’ye bölüyoruz. Kalan kısmı bize 2’lik tabanın basamaklarını vermiş oluyor.

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni5.png"> </p>

Aşağıda cevapları verilmiş çevirmeleri deneyerek alıştırma yapabilirsiniz.
<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni6.png"> </p>

<p>   10 tabanındaki ondalıklı sayıları 2 tabanındaki sayı sistemine dönüştürmek için ondalıklı sayıyı 2 ile çarpıyoruz. Çıkan sonucun tam sayı kısmında bulunan 0 veya 1’i en soldan olacak şekilde yazmaya başlıyoruz. Eğer çarpımın sonucu en sonunda 1’e eşit oluyorsa çarpma işlemi biterek sonuca ulaşmış olunur. <p/>

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni7.png"> </p>

Çarpmalar sonucunda sonuç hala 1 çıkmadıysa yapmanız gereken işlem aşağıdaki gibidir.

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni8.png"> </p>

## BİNARY SAYILARDA TOPLAMA
Binary(İkilik) sayı sistemindeki temel toplama kuralları;<br/>
0+0 =  0 Elde 0 Toplam 0<br/>
0+1 =  1 Elde 0 Toplam 1<br/>
1+0 = 1 Elde 0 Toplam 1<br/> 
1+1 = 10 Elde 1 Toplam<br/> 
0 1+1+1  = 11 Elde 1 Toplam 1<br/> 
Binary sayı sisteminde de iki sayı toplandığında eğer sonuç bir haneye sığmıyorsa bir elde(cary) oluşur. Yani aynı sütunda toplanan her iki adet bir için bir üst basamağa “1” elde eklenir. 


<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni9.png"> </p>

Çözümlü Örnek-2

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni10.png"> </p>

|  | Sonuç | Elde |
| :---:   | :-: | :-: | 
| 1+1= 10 |  0 | 1 |
| (1)+ 0 +1 =10 | 0 | 1 |
| (1)+ 1+0=10 | 0 | 1 |
| (1)+ 1+1=(10)+1=11 | 0 | 1 |
| 1+1+1=11 | 11 | 0|

<p align="center">   <img src="hhttps://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni11.png"> </p>

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni12.png"> </p>

## BİNARY SAYILARDA ÇIKARMA

Binary(İkilik) sayı sistemindeki temel çıkarma kuralları;<br/>
0-0=0 Borç 0 Sonuç 0<br/> 
1-1= 0 Borç 0 Sonuç 0<br/> 
1-0 = 1 Borç 0 Sonuç 1<br/> 
0-1 = 1 Borç 1 Sonuç 1<br/> 
Şeklinde belirtilebilir. Binary sayı sisteminde de küçük değerlikli bir basamaktan büyük değerlikli bir basamak çıkarıldığında, bir üstteki basamaktan bir borç (borrov) alınır ve çıkarma işlemi tamamlanır. Borç alınan “1” bir alt basamağa 2 adet “1” olarak geçer.

| | | |
| :---: | :-: | :-: | 
| <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni13.png"> </p> | <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni14.png"> </p> | <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni15.png"> </p> |

## BİNARY SAYILARDA ÇARPMA
 Binary(İkilik) Sayılarla Çarpma işlemi Decimal(Onluk) sayı sisteminin aynısı olup temel çarpma kuralları aşağıdaki gibidir. 
 - 0 x 0 = 0  
 - 0 x 1 = 0 
 - 1 x 0 = 0 
 - 1 x 1 = 1
 Aslında bildiğimiz çarpma işlemi yapıyoruz.
 <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni16.png"> </p>
 
| | |
| :---: | :-: | 
| <p>   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni17.png"> </p> | <p>   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni18.png"> </p> | 

 <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni19.png" width="500"> </p>
 
## BİNARY SAYILARDA BÖLME

 Binary(İkilik) Sayılarda kullanılan temel bölme kuralları aşağıdaki gibidir. Binary(İkilik) Sayılardaki bölme işlemi Decimal (Onluk) Sayı sisteminin aynısıdır. 
 - 0 ÷ 0 = 0 
 - 0 ÷ 1 = 0 
 - 1 ÷ 0 = 0 
 - 1 ÷ 1 = 1
<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni20.png" width="500"> </p>
<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni21.png" width="500"> </p>

Detaylı anlatım için buradan izleyebilirsiniz:
- https://www.youtube.com/watch?v=oPgNeL8VotA&ab_channel=RealElectronicsTR

 ## C. 	Octal(Sekizli) Sayı Sistemi
 Kullanılan bu sayı sistemlerinden Octal (Sekizli) Sayı sisteminin tabanı sekiz olup 0, 1, 2, 3, 4, 5, 6, 7 rakamları bu sayı sisteminde kullanılır.
   1. 8’lik tabandan 2’lik tabana çevirme
     2^n (2 üzeri n) formülüne baktığımızda 8 tabanında yazılan bir sayının 3 bitten oluşması gerekir. N yerine 3 yazdığımızda 8 sayısına ulaşırız çünkü. Örnek olarak:
     
 <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni22.png" width="500"> </p>
 Örneğini verebiliriz.

   2. 2’lik tabandan 8’lik tabana çevirme
Bu kısımda ise elimizdeki 2’lik tabandaki sayıları sağdan başlayarak 3’erli gruplara ayırıyoruz. Eğer en sonda kalan sayımız 3 basamaktan az ise en soluna eksik basamak kadar 0 yazarak basamakları 3’e tamamlıyoruz. Daha sonra her 3’lü grupta çıkan sonuç 8’lik tabandaki sayının bir basamağını oluşturmaktadır. Örnek vermek gerekirse:

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni23.png" width="500"> </p>

## D. Hexadecimal(16’lı) Sayı Sistemi 	
Hexadecimal sayı sistemlerde 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F 
Kullanılır. 9’dan sonrasında harflere geçilmesinin sebebi 10 ile 1-0’ın karışmasını önleyerek karışıklığı ortadan kaldırmaktır. Hexadecimal sayıların 2’lik tabandaki gösterimi aşağıdaki gibidir:

<p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/yeni24.png" width="500"> </p>
Sayıyı kafadan istediğimiz gibi verebiliriz. Örneğin sayımız (1001011111111011)₂ bunu 16 tabanına çevirelim.<br/>
16 = 2⁴<br/>
Yani 4'er gruplara ayıracağız.<br/>
(1001),(0111),(1111),(1011) bu da 97FB<br/>
Çözümlü Örnek-2<br/>
(010101101010111001101010) 2’lik tabandaki sayı. 16’lık tabana dönüştürelim.<br/>
0101 0110 1010 1110 0110 1010<br/>
5     6     A   E     6	  A<br/>
Sonuç:   56AE6A	

## İşaretli İkili Sayılar 
 ## **İşaretsiz ikili sayılar**:  
 Sekiz bitlik bir belleğin herbir gözü bir sayı saklamak amacıyla kullanılırsa 28=256 değişik işaretsiz sayıyı saklama olanağı vardır. 
  - 0000 0000 -> 0 
  - 1111 1111  -> 255    
  - 
 # **İşaretli İkili Sayılar**: 
 İkilik bir sayının işaretini belirtmek için iki yöntem kullanılır: 
 ## 1. İkilik sayıdaki sekiz bitten bir tanesini işaret bitine ayırılır. 
 En Yüksek Anlamlı Bit (YAB) işaret biti olarak kullanılır. 
   - YAB’in 1 olması sayının negatif, 0 olması pozitif olduğu anlamına gelir.
      - 1111 1111 -127 
      - 1000 0001 – 1
      - 0000 0000 0 
      - 0111 1111 127 

       **Pozitif** sayıların kodlanmasında ( işaretsiz sayılarda olduğu gibi) “doğal ağırlıklı ikili kodlama “ kullanılır. Dikkay edilmesi gerekilen nokta sayının 0 ile başlamasıdır. Buna göre 8 bit ile temsil edilebilecek pozitif işaretli sayılar: 0000 0000 ile 0111 1111 arasında (yani 0 ile +127) değişecektir.<br/>
      Ancak negatif sayılarda bu yöntem yeterli olmamaktadır çünkü 
-	01101 sayısı işaretsiz sayılar için 13 ve işaretli sayılar için +13 
-	11101 sayısı işaretsiz sayılar için 29 ve işaretli sayılar için -9 anlamına gelir.

**Negatif** sayılar 1’in tümleyeni ya da 2’nin tümleyeni olarak tutulur ancak 2’nin tümleyeni gösterimi daha yaygındır.<br/>

 ## 2. Tümleme yöntemi: 
    - r-1 tabanında tümleyen<br/>
    - r tabanında tümleyen<br/>
  Buradaki r harfi tümleme işleminin yapıldığı basamağı temsil eder.<br/>
    Örneğin iki tabanı için;<br/>
       • 2’nin tümleyeni r tümleyen<br/>
       • 1’in tümleyeni r-1 tümleyendir.<br/>
 On tabanı için;<br/>
    • 10’un tümleyeni r tümleyen<br/>
    • 9’un tümleyeni r-1 tümleyendir.<br/>
    
### r-1 tabanında Tümleyen
   r tabanlı bir tam sayı sisteminde n basamaklı pozitif tamsayı N ile gösterilirse N sayısının r-1 rümleyeni;
                                   <p align="center">   **(r(n) -1 ) – N** </p> 
-	23 desimal sayısının 9(r-1) tümleyeni => 102-1-23 = 99 - 23 = 76
-	2314 desimal sayısının 9’a tümlenini =>10000-1-2314 =9999-2314=7685

İkili sayılarda kısaca 0 ları 1, 1 leri 0 yaparak elde edilebilir.
-	(101101)2  binary sayısının 1’re(r-1) tümleyeni => 010010
### r tabanında Tümleyen 
  r tabanlı bir tam sayı sisteminde n basamaklı pozitif tamsayı N ile gösterilirse N sayısının r tümleyeni ;
                                  <p align="center">   **Nr=rn-N** </p> 
olarak tanımlanabilir

-	23 sayısının 10 tümleyeni => 102-23 = 100 – 23 = 77<br/>

İkilik bir sayının 2’ye tümleyenini bulmak için önce sayının 1’e tümleyeni alınır ardından 1 eklenir.<br/>
-	110010 binary sayısının 2 (r) tümleyeni : 001101 + 1     : 001110(2)

## İşaretli Sayılarda Toplama 
Yapılan işlem işaretsiz sayılarda yaptığımıla aynıdır ancak yorumlanması farklı yapılır. n bitlik işaretli iki sayının toplanması sonucu (n+1). bit oluşuyorsa bu bit göz ardı edilir(taşma). Burada önemli olan negatif sayıların 2’nin tümleyeni şekilde yazılması ve eğer sonuç negatif çıkıyorsa bu sonuncunun 2’nin tümleyeni olarak elde edildiğini göstermesidir.<br/>
- Örnek
  - 00000001 -> 1
  - 1’in tümleyini    : 11111110
  - 2’nin tümleyeni : 1111110 + 1 : 11111111   
  <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/25.png" width="500"> </p>
  <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/26.png" width="500"> </p>
   -1 ile 3'ün toplanması sırasında en sol bitlerden bir elde gelir. Bu elde ihmal edildiğinde doğru sonuca ulaşılmış olunur.
   <p align="center">   <img src="https://github.com/tonyukukkula/GaziBMmmF/blob/main/s%C4%B1n%C4%B1f2/donem2/Say%C4%B1sal%20Tasar%C4%B1m/Kaynak/27.png" width="500"> </p>
        Kırmızı olan taşan bitler oldukları için dikkate alınmıyor. Eğer sayı 0 ile başlıyorsa pozitiftir ve normal gösterilmiştir ancak eğer 1 ile başlıyorsa negatiftir ve sayı 2’ nin tümleyeni şeklinde gösteriliyordur.
