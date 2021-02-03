Hürmetler. Hataları bildirmek için destekleme isteği(PR) atabilir veya e-posta yoluyla <a href="mailto:alpkut55@gmail.com">ulaşabilirsiniz</a>.<br/>
Şimdi konumuza gelelim okulumuz(Gazi Üniversitesi Mühendislik Fakültesi) Elektrik-Elektronik Mühendisliği öğrencileri bu derste ARM Assembly görecekleri için bu kaynak onlar adına çok faydalı olmayacağı kanısındayım.
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







# Yararlı Bağlantılar
- Öykünücü Nedir? https://medium.com/@ozkancakirwork/em%C3%BClat%C3%B6r-nedir-nas%C4%B1l-kullan%C4%B1l%C4%B1r-bbf8a0b5d19a
- Emu8086 indir https://emu8086-microprocessor-emulator.en.softonic.com/
- Emu8086 ve Assembly https://roboturka.com/pic-assembly-pic-c/assembly-ve-emu8086/
- Emu8086 ilk adım https://mimoza.marmara.edu.tr/~ubaspinar/mikro2proje/emu8086_foy.pdf

