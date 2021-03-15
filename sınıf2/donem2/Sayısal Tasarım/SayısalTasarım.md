# <p align="center">  Sayısal Tasarım  </p>

## Sayı Sistemleri
  - Elektronik sistemler analog ve sayısal olmak üzere ikiye ayrılır. 
  - Sayısal kelimesi 'dijital' teriminin karşılığıdır. 
  - Analog sistemlerde elektrik sinyalleri sürekli olarak değişir ve belli sınırlar içinde her değeri alabilirler. Sayısal sistemlerde ise elektriksel sinyaller olduğu gibi iletilmez. Bu sinyallerin yerine bunlara karşı düşen rakamlar iletilir. Sayısal işlemler ikili sayısal işaretler üzerinden işlem yaptığından bu rakamlar 0 ve 1 lerdir.

 <p align="center">   <img src="https://github.com/busranur-sr/Sayisal-Tasarim/blob/main/signals.jpg"> </p>
  
  Elektronikte daha önce analog teknikler kullanılarak yapılan uygulamalar, günümüzde sayısal teknikler kullanılarak yapılmaktadır. Sayısal tekniğin, Analog tekniğe göre tercih edilme nedenleri aşağıdaki gibi özetleyebiliriz.
  
 <p align="center">   <img src="https://github.com/busranur-sr/Sayisal-Tasarim/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202021-03-07%20094943.png"> </p>

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

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni1.png"> </p>

### 1- İkilik Tabandan 10’lu Tabana Çevirme
Binary(ikili) sayıları Decimal(Onlu) sayılara dönüştürürken her bir bit basamak ağırlığı ile çarpılıp bu sonuçların toplanması gerekir.

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni2.png"> </p>

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni3.png"> </p>

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni4.png"> </p>

- Virgüllü sayılarda işlem basamaklarının nasıl olduğunu izlemek için youtube linkine bakabilrisiniz.<br/>
	https://www.youtube.com/watch?v=Lh8ra1E-ZQ4&ab_channel=ElektronikDerslerim

### 2- DECİMAL SAYILARIN BİNARY SAYILARA ÇEVRİLMESİ
Ana sayımızın  bölümü 0 olana kadar 2’ye bölüyoruz. Kalan kısmı bize 2’lik tabanın basamaklarını vermiş oluyor.

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni5.png"> </p>

Aşağıda cevapları verilmiş çevirmeleri deneyerek alıştırma yapabilirsiniz.
<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni6.png?raw=true"> </p>

<p>   10 tabanındaki ondalıklı sayıları 2 tabanındaki sayı sistemine dönüştürmek için ondalıklı sayıyı 2 ile çarpıyoruz. Çıkan sonucun tam sayı kısmında bulunan 0 veya 1’i en soldan olacak şekilde yazmaya başlıyoruz. Eğer çarpımın sonucu en sonunda 1’e eşit oluyorsa çarpma işlemi biterek sonuca ulaşmış olunur. <p/>

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni7.png"> </p>

Çarpmalar sonucunda sonuç hala 1 çıkmadıysa yapmanız gereken işlem aşağıdaki gibidir.

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni8.png"> </p>

## BİNARY SAYILARDA TOPLAMA
Binary(İkilik) sayı sistemindeki temel toplama kuralları;<br/>
0+0 =  0 Elde 0 Toplam 0<br/>
0+1 =  1 Elde 0 Toplam 1<br/>
1+0 = 1 Elde 0 Toplam 1<br/> 
1+1 = 10 Elde 1 Toplam<br/> 
0 1+1+1  = 11 Elde 1 Toplam 1<br/> 
Binary sayı sisteminde de iki sayı toplandığında eğer sonuç bir haneye sığmıyorsa bir elde(cary) oluşur. Yani aynı sütunda toplanan her iki adet bir için bir üst basamağa “1” elde eklenir. 


<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni9.png"> </p>

Çözümlü Örnek-2

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni10.png"> </p>

|  | Sonuç | Elde |
| :---:   | :-: | :-: | 
| 1+1= 10 |  0 | 1 |
| (1)+ 0 +1 =10 | 0 | 1 |
| (1)+ 1+0=10 | 0 | 1 |
| (1)+ 1+1=(10)+1=11 | 0 | 1 |
| 1+1+1=11 | 11 | 0|

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni11.png"> </p>

<p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni12.png"> </p>

## BİNARY SAYILARDA ÇIKARMA

Binary(İkilik) sayı sistemindeki temel çıkarma kuralları;<br/>
0-0=0 Borç 0 Sonuç 0<br/> 
1-1= 0 Borç 0 Sonuç 0<br/> 
1-0 = 1 Borç 0 Sonuç 1<br/> 
0-1 = 1 Borç 1 Sonuç 1<br/> 
Şeklinde belirtilebilir. Binary sayı sisteminde de küçük değerlikli bir basamaktan büyük değerlikli bir basamak çıkarıldığında, bir üstteki basamaktan bir borç (borrov) alınır ve çıkarma işlemi tamamlanır. Borç alınan “1” bir alt basamağa 2 adet “1” olarak geçer.

| | | |
| :---: | :-: | :-: | 
| <p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni13.png"> </p> | <p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni14.png"> </p> | <p align="center">   <img src="https://github.com/busranur-sr/BMT-ST/blob/main/d%C3%B6n%C3%BC%C5%9F%C3%BCm/yeni15.png"> </p> |

