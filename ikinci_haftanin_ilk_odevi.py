ogrenciler = [
    {"ad": "Ahmet", "soyad": "Yilmaz", "vize": 85, "final": 90, "sozlu": 75},
    {"ad": "Ayse", "soyad": "Kara", "vize": 70, "final": 80, "sozlu": 65},
    {"ad": "Mehmet", "soyad": "Demir", "vize": 75, "final": 95, "sozlu": 85},
    {"ad": "Fatma", "soyad": "Cetin", "vize": 60, "final": 70, "sozlu": 50},
    {"ad": "Ali", "soyad": "Yildirim", "vize": 90, "final": 85, "sozlu": 80},
    {"ad": "Zeynep", "soyad": "Kaya", "vize": 80, "final": 65, "sozlu": 60},
    {"ad": "Emre", "soyad": "Ergin", "vize": 70, "final": 80, "sozlu": 70},
    {"ad": "Aysenur", "soyad": "Turan", "vize": 95, "final": 90, "sozlu": 85},
    {"ad": "Hakan", "soyad": "Koc", "vize": 60, "final": 60, "sozlu": 75},
    {"ad": "Elif", "soyad": "Ozdemir", "vize": 15, "final": 20, "sozlu": 70}
]

# 2. Not ortalamalarını hesaplayın ve sözlüğe ekleyin
for ogrenci in ogrenciler:
    vize_notu = ogrenci["vize"]
    final_notu = ogrenci["final"]
    sozlu_notu = ogrenci["sozlu"]
    not_ortalamasi = (vize_notu + final_notu + sozlu_notu) // 3  # tam sonuç için /
    ogrenci["not_ortalamasi"] = not_ortalamasi

# 2. En yüksek not ortalamasına sahip öğrenciyi bulun ve ekrana yazdırın
en_yuksek_not_ortalamasi = max(ogrenciler, key=lambda x: x["not_ortalamasi"])
print("En yüksek not ortalamasına sahip öğrenci:", en_yuksek_not_ortalamasi["ad"], en_yuksek_not_ortalamasi["soyad"],
      en_yuksek_not_ortalamasi["not_ortalamasi"])

#lambda x: x["not_ortalamasi"]: Bu ifade, bir lambda (anonim) fonksiyonunu temsil eder. Lambda fonksiyonları,
# küçük işlevleri tek satırda ifade etmek için kullanılır. x lambda ifadesinin girdisini temsil eder ve
# x["not_ortalamasi"] ifadesi, x sözlüğünün içindeki "not_ortalamasi" anahtarının değerini döndürür.
#Örnek olarak, max fonksiyonunu ele alalım. max fonksiyonu, bir dizi öğe içindeki en büyük öğeyi bulmak için kullanılır.
# Ancak, hangi kritere göre en büyük öğeyi belirleyeceğinizi belirtmeniz gerekebilir.
# İşte bu noktada key parametresi devreye girer. key parametresi, her öğe üzerinde çalışan bir fonksiyon olarak
# düşünülür ve bu fonksiyonun sonuçlarına göre sıralama yapılır.

# 3. Adları soyadından ayırarak ayrı bir tuple içinde saklayın ve listeye ekleyin
adlar_soyadlar = []
for ogrenci in ogrenciler:
    ad = ogrenci["ad"]
    soyad = ogrenci["soyad"]
    adlar_soyadlar.append((ad, soyad))

# 4. Adları alfabetik sıraya göre sıralayın ve ekrana yazdırın
adlar_soyadlar.sort()
print("Adlar alfabetik sıraya göre sıralanmış hali:")
for ad, soyad in adlar_soyadlar:
    print(ad, soyad)

# 5. Not ortalaması 70'in altında olan öğrencileri gösterin
zayif_ogrenciler = []
for ogrenci in ogrenciler:
    if ogrenci["not_ortalamasi"] < 70:
        ad = ogrenci["ad"]
        soyad = ogrenci["soyad"]
        not_ortalamasi = ogrenci["not_ortalamasi"]
        zayif_ogrenciler.append((ad, soyad, not_ortalamasi))

print("Not ortalaması 70'in altında olan öğrenciler:")
for ad, soyad, not_ortalamasi in zayif_ogrenciler:
    print(f"{ad} {soyad}, Not Ortalaması: {not_ortalamasi}")






#2. Odev


import json

film_koleksiyonu = []

def film_ekle():
    ad = input("Filmin adını giriniz: ")
    yonetmen = input("Yönetmen adını giriniz: ")
    yil = input("Yılı giriniz: ")
    tur = input("Türü giriniz: ")
    film = {
        "Ad": ad,
        "Yonetmen": yonetmen,
        "Yil": yil,  # Yılı ekledim
        "Tur": tur
    }
    film_koleksiyonu.append(film)
    print(f"{ad} filmi koleksiyona eklendi")

def film_duzenle(film_adi):
    for film in film_koleksiyonu:
        if film["Ad"] == film_adi:
            yeni_ad = input("Yeni film adını giriniz: ")
            yeni_yonetmen = input("Yeni yönetmeni giriniz: ")
            yeni_yil = input("Yeni yılı giriniz: ")
            yeni_tur = input("Yeni türü giriniz: ")

            film["Ad"] = yeni_ad
            film["Yonetmen"] = yeni_yonetmen
            film["Yil"] = yeni_yil
            film["Tur"] = yeni_tur
            print(f"{film_adi} düzenlenmiştir")

def film_sil(film_adi):
    for film in film_koleksiyonu:
        if film["Ad"] == film_adi:
            film_koleksiyonu.remove(film)
            print(f"{film_adi} silinmiştir")

def koleksiyonu_goruntule():
    for film in film_koleksiyonu:
        print(f"Ad: {film['Ad']}, Yönetmen: {film['Yonetmen']}, Yıl: {film['Yil']}, Tür: {film['Tur']}")

def veriyi_dosyaya_kaydet():
    with open("film_koleksiyonu.json", "w") as dosya:
        json.dump(film_koleksiyonu, dosya)

def veriyi_dosyadan_yukle():
    try:
        with open("film_koleksiyonu.json", "r") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return []

# Program başladığında önce veriyi yükle
film_koleksiyonu = veriyi_dosyadan_yukle()

while True:
    print("\nFilm koleksiyonu yönetimi")
    print("1. Film ekle")
    print("2. Film düzenle")  # Seçenek numarasını düzelttim
    print("3. Film sil")  # Seçenek numarasını düzelttim
    print("4. Koleksiyonu görüntüle")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemin numarasını girin: ")

    if secim == "1":
        film_ekle()
        veriyi_dosyaya_kaydet()
    elif secim == "2":
        film_adi = input("Düzenlemek istediğiniz film adını girin: ")
        film_duzenle(film_adi)
        veriyi_dosyaya_kaydet()
    elif secim == "3":
        film_adi = input("Silmek istediğiniz film adını girin: ")
        film_sil(film_adi)
        veriyi_dosyaya_kaydet()
    elif secim == "4":
        koleksiyonu_goruntule()
    elif secim == "5":
        print("Çıkış yapılıyor")
        veriyi_dosyaya_kaydet()
        break
    else:
        print("Geçersiz bir seçim yaptınız")



#3.Odev

def yeni_musteri_ekle():
    musteri_id = input("Müşteri Kimliği (ID) girin: ")
    ad = input("Adinizi girin: ")
    soyad = input("Soyadinizi girin: ")
    email = input("E-posta adresinizi girin: ")
    telefon = input("Telefon numaranizi girin: ")

    musteri = {
        'Ad': ad,
        'Soyad': soyad,
        'E-posta': email,
        'Telefon': telefon
    }

    musteriler[musteri_id] = musteri
    print(f"{ad} {soyad} müşterisi eklenmiştir.")

# Müşteri bilgilerini güncellemek
def musteri_guncelle():
    musteri_id = input("Güncellemek istediğiniz müşterinin kimliğini (ID) girin: ")

    if musteri_id in musteriler:
        print(f"{musteri_id} müşterisinin mevcut bilgileri:")
        mevcut_musteri = musteriler[musteri_id]
        for anahtar, deger in mevcut_musteri.items():
            print(f"{anahtar}: {deger}")

        ad = input("Yeni adi girin (değiştirmek istemiyorsaniz boş birakin): ")
        soyad = input("Yeni soyadi girin (değiştirmek istemiyorsaniz boş birakin): ")
        email = input("Yeni e-postayi girin (değiştirmek istemiyorsaniz boş birakin): ")
        telefon = input("Yeni telefon numarasini girin (değiştirmek istemiyorsaniz boş birakin): ")

        if ad:
            mevcut_musteri['Ad'] = ad
        if soyad:
            mevcut_musteri['Soyad'] = soyad
        if email:
            mevcut_musteri['E-posta'] = email
        if telefon:
            mevcut_musteri['Telefon'] = telefon

        musteriler[musteri_id] = mevcut_musteri
        print(f"{musteri_id} müşteri bilgileri güncellendi.")
    else:
        print(f"{musteri_id} müşterisi bulunamadi.")

# Müşteri silmek
def musteri_sil():
    musteri_id = input("Silmek istediğiniz müşterinin kimliğini (ID) girin: ")

    if musteri_id in musteriler:
        silinen_musteri = musteriler.pop(musteri_id)
        print(f"{silinen_musteri['Ad']} {silinen_musteri['Soyad']} müşterisi silinmiştir.")
    else:
        print(f"{musteri_id} müşterisi bulunamadi.")

# Tüm müşterileri listeleme
def musterileri_listele():
    if len(musteriler) == 0:
        print("Henüz müşteri kaydi yok.")
    else:
        print("\nTüm Müşteriler:")
        for musteri_id, musteri in musteriler.items():
            print(f"Müşteri Kimliği (ID): {musteri_id}")
            for anahtar, deger in musteri.items():
                print(f"{anahtar}: {deger}")
            print("-" * 30)

# Ana program döngüsü
while True:
    print("\nMüşteri Yönetim Sistemi")
    print("1. Yeni Müşteri Ekle")
    print("2. Müşteri Bilgilerini Güncelle")
    print("3. Müşteri Sil")
    print("4. Tüm Müşterileri Listele")
    print("5. Çikiş")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        yeni_musteri_ekle()
    elif secim == '2':
        musteri_guncelle()
    elif secim == '3':
        musteri_sil()
    elif secim == '4':
        musterileri_listele()
    elif secim == '5':
        print("Programdan çikiliyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")
