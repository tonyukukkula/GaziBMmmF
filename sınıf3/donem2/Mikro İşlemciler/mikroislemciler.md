Hürmetler. Hataları bildirmek için destekleme isteği(PR) atabilir veya e-posta yoluyla <a href="mailto:alpkut55@gmail.com">ulaşabilirsiniz</a>.<br/>
Şimdi konumuza gelelim okulumuz(Gazi Evrenkenti Mühendislik Bölümcesi) Elektrik-Elektronik Mühendisliği öğrencileri bu derste ARM Assembly görecekleri için bu kaynak onlar adına çok faydalı olmayacağı kanısındayım.
Bu derste öncelikle Assembly ve doğası hakkında konuşmak isterim. Assembly her aletin(işlemcinin) yapısına:
- Komut Seti Yapısına (ISA)
- İşlemci Mimari Yapısına<br/>
bağlıdır. Yukarı seviyeden(high level) bakınca çok ilkel gelebilir ama bilgisayar biliminin transistörün icadından sonraki çağına baktığımızda çok *manyak* bir şey olduğunu anlıyoruz.<br>
Bu gelişimi şöyle özetleyim: bilgisayar bilimi transistörün icadından sonra sayısal tasarım harikaları olduğu kavranmış lâkin ortada bir birlik olmadığını görmüşler. Her bilgisayar kendi başına bir cumhuriyet olduğu dönemlerde insanlık kendisi gibi kavga dövüşsüz birlik olunca daha güçlü olduğunu bildiği gibi bilgisayar biliminin de daha güçlü olabileceğini kavramışlar ve bir ortak zemin kurmak istemişler sonuçta kim yanında hayvan gibi delikli programlama kayıtçısı taşımak ister ki?<br>
<div style="margin-left:auto,margin-right: auto" align="center"><img src="https://i.ytimg.com/vi/wALFrUd6Ttw/hqdefault.jpg" alt="punch card and altair 8800"><br/>soldan akıp giden gri şerit delikli programlama kayıtçısı(punched card)<img/></div><br/>

Sonrasında çeşitli diller geliştirilmiş ki insanlar farklı bilgisayarlar kullansa da ortak bir yazılım tabanında yazılım geliştirilebilsin. Bu arada yazılım demişken epeydir bir zaman tartışma konusu olan "kadın yazılımcılar", "abi erkekler her işte olduğu gibi yazılımda da kadınlardan üstün" tarzı aptalca hikayeler gezmekte lâkin gerçeği biliyor musunuz?<br/>

<div style="margin-left:auto,margin-right: auto" align="center"><img width="300" src="https://media1.tenor.com/images/0d0077a13fff517c97916da3ccb27ec8/tenor.gif?itemid=17051074"/></div></br>

_İlk yazılımcılar arasında erkek yok denecek kadar azdır bunun  asıl nedeni gâvurların 80li yıllara kadar yazılımın değerini kavrayamaması ve asıl işin donanımda olduğunu düşünmesinden dolayı yazılım için "software" yani "cıvık-yumuşak mal" muamelesi yapmaları bu yüzden erkeklere yakıştırılmamasıdır; "hardware" ise "sert-zor mal" anlamına gelip bu iş için daha fazla nitelik gerektirdiğini düşünmeleridir._</br>

Giriş kısmını geride bıraktığımıza göre Assembly nedir kısmına hafiften gelelim.

# Assembly Nedir?
Assembly makina dili üzerinde bulunan ve kendi makina-kod dönüştürücüsü(assembler) yardımıyla yazılan kodu makina diline çeviren bir güzelliktir. C yazdığınızda C derleyicisi kodu Assembly'ye onu da makina koduna çevirir. Bu çevirimde arada olan güzellikleri listelersek listemiz şu şekilde olacaktır.
- derleyici(compiler)
- bağlayıcı(linker) 
- makina-kod dönüştürücüsü(assembler)<br/>
Bu ders kapsamında bu üç elemana gerek duymayacağız ve bir Intel 8086 işlemcisi ![öykünücüsü(emülatörü)](https://medium.com/@ozkancakirwork/em%C3%BClat%C3%B6r-nedir-nas%C4%B1l-kullan%C4%B1l%C4%B1r-bbf8a0b5d19a) ile öğreneceğiz x86 Assembly'i.

# Emu8086
Yazacağımız x86 Assembly kodlarımızı üzerinde öykünetebileceğimiz(emule) bir öykünücüdür. Kullanımı ve genel olarak burayla ilgili açıklamalar için ![bu linke](https://roboturka.com/pic-assembly-pic-c/assembly-ve-emu8086/) bakabilirsiniz.</br>
Ve ![bu bağlantı](https://emu8086-microprocessor-emulator.en.softonic.com/)dan indirilebilir.

# Assembly İlk Adımlar
Komutlar basittir ve programın "help" düğmesinden rahatça erişilebilmektedir.
![image](https://user-images.githubusercontent.com/44534126/113336434-16312e80-932f-11eb-96c6-66de733c2bb8.png)
Burada yukarıdan "8086 Instruction Set" bağıntısına tıklayarak tüm komutların listesine ulaşabilirsiniz.
Yüksek ihtimal tüm komutlara ihtiyacınız olmayacak olursa da buradan okuyabilirsiniz.
Kesinlikle bilinmesi gerekenler:
- ADD
- AND
- CALL
- CMP
- DIV
- INT
- J[bayraklar] : JC, JNB
- JMP
- LEA
- LOOP
- MUL
- MOV
- NOT
- OR
- POP
- PUSH
- SUB
- liste, üzerine düzgünce düşünülürse uzayıp gidebilir lâkin gerek görmedim. Bunların durumsal hallerini, çeşitli bayraklar ile etkileşimde olduğu zamanki hallerini yardım dökümanından kendi başınıza karıştırıp, kod örnekleri inceleyip öğreniminizi verimli hale getirebilirsiniz.

## İyi bu komutları öğrenelim de reg ne memory ne immediate ne sreg ne?
Tüm komutlar olmasa da çoğu komutlar "operand" denilen işleçlerle çalışır ve bunların dökümantasyondan layığıyla öğrenilmesi gerekli yoksa ekrana, _uygun tabirle_, mal gibi baktırır. 

### REG(register/yazmaç) 
Var olanlar: AX, BX, CX, DX, AH, AL, BL, BH, CH, CL, DH, DL, DI, SI, BP, SP.
Burada ikinci karakteri X'li olan yazmaçlar 16 bit yazmaçlardır. 2. karakterdeki L=low(düşük) ve H=High(üst) 8'li bit dizilerini ifade eder; P=Pointer(işaretçi) bir şeyi işaret eden yazmaçlarda görürüz.

![image](https://user-images.githubusercontent.com/44534126/113339744-9e193780-9333-11eb-9d17-dbb3fd69ee22.png)

### Memory(hafıza)
Adı üstünde hafızadaki konumu niteler. Köşeli parantezler içinde  BX, SI, DI, BP yazmaçları ile kullanılabilir, burjuvalar gibi [segment:konum] şeklinde kulllanmaya çalışmayın.  

### Immediate(Hazır değer)
Çeşitli tabanlardaki, _ikilik, sekizlik, onluk, on altılık_, sayıların şap diye işleç olarak kullanılan halidir.
Örnek:
```assembly
mov al, 123 ;buradaki al yazmacına(alanı 256bit=2^8) ondalık tabanda şap diye 123 değerini girdik.
;bir zımbırtı belirlemezsek hazır değerlerimiz ondalık olarak işlem görür
;123h deseydik on altılık tabanda işlem görecekti
;123b diyemezdik çünkü 2lik tabanda yalnızca 0 ve 1 var :D
;123o deseydik sekizlik tabanda işlem görecekti
```
### SREG(segment yazmacı)
Buradaki yazmaçlar segment ifade eder.
![image](https://user-images.githubusercontent.com/44534126/113344836-48945900-933a-11eb-83a7-e5874600bcc6.png)





# Yararlı Bağlantılar
- Öykünücü Nedir? https://medium.com/@ozkancakirwork/em%C3%BClat%C3%B6r-nedir-nas%C4%B1l-kullan%C4%B1l%C4%B1r-bbf8a0b5d19a
- Emu8086 indir https://emu8086-microprocessor-emulator.en.softonic.com/
- Emu8086 ve Assembly https://roboturka.com/pic-assembly-pic-c/assembly-ve-emu8086/
- Emu8086 ilk adım https://mimoza.marmara.edu.tr/~ubaspinar/mikro2proje/emu8086_foy.pdf

