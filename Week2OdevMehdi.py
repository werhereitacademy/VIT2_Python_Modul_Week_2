#Soru 1' in cevabı
ogrenciler={
    'Merve Terek': [50,60,70],
    'Kazim KOyuncu': [65,60,70],
    'Ali Sunal': [30,60,70],
    'Ozcan Deniz': [75,60,70],
    'Hande Yener': [55,60,70],
    'Qua Resma': [80,60,70],
    'Mahmut Tuncel': [85,60,70],
    'Seda Sayan': [20,60,70],
    'Rauf Denktas': [35,60,70],
    'Mahsun Kirmizi': [70,60,70],

}

ort = 0
toplam = 0
for i in ogrenciler.values():
    for j in i:
        toplam += j
        ort = int(toplam/3)
    i.append(ort)
    ort = 0
    toplam = 0

en_buyuk_anahtar, en_buyuk_deger = max(ogrenciler.items(), key=lambda x: x[1])
print("en yuksek ortalamaya sahip ogrenci = ",en_buyuk_anahtar,"Not: ", en_buyuk_deger[-1])
ad_soyad=[]
for i in ogrenciler.keys():
    isimler =tuple(i.split())
    ad_soyad.append(isimler)
print(ad_soyad)

ad_soyad.sort()
print(ad_soyad)

yetmis_down =set()
for i,z in ogrenciler.items():
    if z[3] < 70:
        yetmis_down.add(f"{i},{z[3]}")
print('Notu 70 in altinda olan ogrenciler: ',yetmis_down)

2.Soru
filmler = []
count = 1

def film_ekle():
    global count
    film_adi = input("Yeni filmin adini girin: ")
    yonetmen = input("FIlmin yonetmeninin adini girin: ")
    yayinyili = input("Filmin yayinyilini girin: ")
    turu = input("Filmin turunu girin: ")
    film = {
        "Sira Numarasi": count,
        "Filmin Adi": film_adi,
        "Filmin Yonetmeni": yonetmen,
        "Filmin Yayinyili": yayinyili,
        "Filmin Turu": turu
    }
    filmler.append(film)
    count += 1
    print("Yeni film eklendi: ", film_adi)

def film_sil():
    global count
    film_numarasi= int(input("Silinecek filmin numarasini girin: "))
    for film in filmler:
        if film["Sira Numarasi"] == film_numarasi:
            filmler.remove(film)
def film_liste():
    print("\nTüm :")
    if not filmler:
        print("Listenizde film yok")
    else:
        for film in filmler:
            print(f"{film['Sira Numarasi']}:"
            f" {film['Filmin Adi']} "
            f"({film['Filmin Yonetmeni']})"
            f" ({film['Filmin Yayinyili']})"
            f"({film['Filmin Turu']})")

film_ekle()
film_liste()
film_sil()
film_liste()

SOru 3
musteriler = {}

def yeni_musteri_ekle():
    musteri_id = input("Müşteri ID: ")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    email = input("E-posta: ")
    telefon = input("Telefon: ")

    musteri_bilgileri = {
        "Ad": ad,
        "Soyad": soyad,
        "E-posta": email,
        "Telefon": telefon
    }

    musteriler[musteri_id] = musteri_bilgileri
    print("Yeni müşteri eklendi.")
def musteri_goruntule():
    for i in musteriler.keys():
        x = i
        print(x)

def musteri_sil():
    musteri_id = input("Silmek istediğiniz müşteri ID'sini girin: ")
    if musteri_id in musteriler:
        del musteriler[musteri_id]
        print("Müşteri silindi.")
    else:
        print("Müşteri bulunamadı.")

yeni_musteri_ekle()
yeni_musteri_ekle()
musteri_sil()
musteri_goruntule()
