# Emlak Acentesi Takip Sistemi

##### Aylık Net Asgari Ücret: 2020 yılı için belirlenen aylık net asgari ücret, 2324,70 TL’dir.
##### Emlak Komisyonu: Emlak acentesinin, yapılan her satış için satış bedelinin %4’ü kadar, her kiralama için 1 aylık kira bedeli kadar kazandığı ücreti ifade etmektedir.
##### Emlak Danışmanı: Bir emlak acentesine bağlı olarak çalışan tanıtım ve pazarlama elemanınıifade etmektedir.
##### Maaş: Emlak acentesinin, danışmanlarına ödediği aylık ücreti ifade etmektedir.
##### Prim: Emlak acentesinin, danışmanlarına maaşlarına ek olarak ödediği, 1 ayda kazandırdıkları emlak komisyonu miktarının %10’u tutarındaki ücreti ifade etmektedir.
##### Kota: Emlak danışmanlarının, bağlı oldukları emlak acentesine 1 ayda kazandırmaları beklenen emlak komisyonu tutarını ifade etmektedir.
##### İkramiye: Emlak acentesinin, danışmanlarına kotalarını doldurmaları durumunda maaşlarına ekolarak ödediği, net asgari ücretin yarısı tutarındaki ücreti ifade etmektedir.
##### Aylık Toplam Ücret: Emlak acentesinin, danışmanlarına bir ayda ödediği maaş, prim ve ikramiyetoplamını ifade etmektedir.

## Bir emlak acentesinde kullanılmak üzere, emlak danışmanlarının aylık performanslarını ve ücretlerini hesaplamak, o ay yapılan satış/kiralama işlemleri ve danışmanlar hakkında bazı istatistiksel bilgiler elde etmek için bir program geliştirilmesi istenmektedir. Bunun için, öncelikle acenteye bağlı olarak çalışan emlak danışmanı sayısı , daha sonra her danışman için aşağıdaki veriler programa girilecektir:

- ad soyad
- maaş (TL): reel sayı (aylık net asgari ücret ya da daha büyük)
- kota (TL): reel sayı (maaşının 10 katı ya da daha büyük)
- o ay sattığı ya da kiraladığı her emlak için:
- o emlak tipi: Konut, İş yeri, Arsa (K/k/İ/i/A/a karakterleri)
- o işlem türü: Satış, Kiralama (S/s/K/k karakterleri)
- o satış/kira bedeli (TL): reel sayı (0’dan büyük)
- o ay sattığı/kiraladığı başka emlak olup olmadığı (E/e/H/h karakterleri)

## Her emlak danışmanının verileri girildikten sonra, o danışman için aşağıdaki bilgiler ekrana yazdırılmaktadır:

- adı soyadı
- o ay sattığı emlak adedi, kiraladığı emlak adedi ve oranları (%)
- o ay sattığı emlakların tiplerine göre toplam bedelleri (TL) ve oranları (%)
- o ay kiraladığı konutların ortalama kira bedeli (TL)
- o ay en yüksek bedelle kiraladığı konutun kira bedeli (TL)
- o ay maaşı (TL)
- o ay primi (TL)
- o ay kotası (TL)
- o ay acenteye kazandırdığı toplam komisyon tutarı (TL)
- o ay kotasını doldurup dolduramadığı
- o ay kotasını doldurduysa alacağı ikramiye (TL)
- o ay toplam ücreti (TL)


## Tüm emlak danışmanları için veri girişleri bittikten sonra aşağıdaki istatistiksel bilgiler ekrana yazdırılmaktadır:

- her emlak tipi için o ay satılan ve kiralanan emlak sayıları ile satılma oranları (%)
- her emlak tipi için o ay satılan emlakların satış bedellerinin toplamı (TL) ve ortalaması
(TL)
- o ay en yüksek bedelle satılan emlağın tipi, satış bedeli (TL), satışı yapan danışmanın
adı-soyadı
- o ay en yüksek bedelle kiralanan konutun kira bedeli (TL), kiralayan danışmanın adısoyadı
- o ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların
sayısı ve kiralanan konutlar içindeki oranı (%)
