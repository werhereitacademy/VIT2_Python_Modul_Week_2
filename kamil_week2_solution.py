#SORU1

ogrenciler = {
    "Ahmet Yilmaz" : [86,90,70],
    "Mehmet Demr" : [97,68,85],
    "Ayse Kaya" : [89,87,79],
    "Betul Ankara" : [67,45,66],
    "Ali izmir" : [70,80,78],
    "Mustafa Akca" : [ 98, 87,88],
    "Emine Gunay" : [75,59,99],
    "Fatma Boz" : [69,77,77],
    "Ibrahim Bozdag" : [83,82,81],
    "Buse Gunes" : [46,81,53]
}

for anahtar in ogrenciler:
    deger = ogrenciler[anahtar]
    toplam = 0
    for a in deger:
        toplam+=a
    ortalama = toplam/3
    deger = deger  + [ortalama]
    ogrenciler[anahtar] = deger
print(ogrenciler)

# En yüksek not alan ogrenci ve ortalamasi
max_not_ogr = max(ogrenciler,key=lambda x: ogrenciler[x][-1])
print(f"En Yüksek Not Ortlamasina sahip öğrenci: {max_not_ogr}.")

ort = ogrenciler[max_not_ogr]
print(f"En yuksek ortalama: {ort[-1]}")

# Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin.

ad_soyad_tuple_listesi=[]
for a in ogrenciler.keys():
    ad,soyad = a.split()
    ad_soyad_tuple_listesi.append((ad,soyad))
print(ad_soyad_tuple_listesi)


# Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.
alfabetik= []
for a in ogrenciler:
    alfabetik.append(a)
alfabetik.sort()
print(alfabetik)  #hata vermiyor ama yazdirmadi!!!!!!!!!


# Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın.
ort70_alti = set()
for a in ogrenciler:
    deger = ogrenciler[a]
    if deger[-1]<70:
        ort70_alti.add(a)
print(ort70_alti)


