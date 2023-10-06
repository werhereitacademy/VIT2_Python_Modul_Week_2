#QUESTION 1 ANSWER

# 10 öğrencinin bilgilerini ve notlarını içeren bir sözlük oluşturun
ogrenciler = {
    "ogrenci_1": {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'vize': 75, 'final': 80, 'sozlu': 90},
    "ogrenci_2": {'ad': 'Mehmet', 'soyad': 'Kaya', 'vize': 85, 'final': 70, 'sozlu': 65},
    "ogrenci_3": {'ad': 'Ayşe', 'soyad': 'Demir', 'vize': 60, 'final': 75, 'sozlu': 80},
    "ogrenci_4": {'ad': 'Fatma', 'soyad': 'Aydın', 'vize': 70, 'final': 65, 'sozlu': 70},
    "ogrenci_5": {'ad': 'Ali', 'soyad': 'Çelik', 'vize': 80, 'final': 90, 'sozlu': 85},
    "ogrenci_6": {'ad': 'Zeynep', 'soyad': 'Yıldız', 'vize': 55, 'final': 60, 'sozlu': 75},
    "ogrenci_7": {'ad': 'Emir', 'soyad': 'Şahin', 'vize': 90, 'final': 85, 'sozlu': 80},
    "ogrenci_8": {'ad': 'Elif', 'soyad': 'Arslan', 'vize': 65, 'final': 70, 'sozlu': 65},
    "ogrenci_9": {'ad': 'Deniz', 'soyad': 'Kurt', 'vize': 75, 'final': 80, 'sozlu': 90},
    "ogrenci_10": {'ad': 'Eren', 'soyad': 'Özdemir', 'vize': 80, 'final': 75, 'sozlu': 70}
}
# Her öğrencinin not ortalamasını hesaplayın ve sözlüğe ekleyin

for bilgi, deger in ogrenciler.items():
    vize_notu = deger['vize']
    final_notu = deger['final']
    sozlu_notu = deger['sozlu']
    not_ortalamasi = int((vize_notu + final_notu + sozlu_notu) / 3)
    deger['not_ortalamasi'] = not_ortalamasi
print(ogrenciler)

# En yüksek not ortalamasına sahip öğrenciyi bulun
en_yuksek_ortalama = 0
en_yuksek_ortalama_ogrenci = None
for ogrenci, deger in ogrenciler.items():
    if deger['not_ortalamasi'] > en_yuksek_ortalama:                #Burada nasil dongu sagladi
        en_yuksek_ortalama = deger['not_ortalamasi']
        en_yuksek_ortalama_ogrenci = ogrenci
print("Ortalamasi en yuksek ogrenci :", en_yuksek_ortalama_ogrenci)

#Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin.
#Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.
adlar_soyadlar = []
for bilgi in ogrenciler.values():
    adlar_soyadlar.append((bilgi['ad'], bilgi['soyad']))
sirali_liste = sorted(adlar_soyadlar)
print(sirali_liste)
#Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın.
notlari_70_den_asagi_olan_ogrenciler = set()
for ogrenci, deger in ogrenciler.items():
    if deger['not_ortalamasi'] < 70:
        notlari_70_den_asagi_olan_ogrenciler.add(ogrenci)
print("Notlari 70 den dusuk ogrenciler :",notlari_70_den_asagi_olan_ogrenciler)


#QUESTION 2 ANSWER
import json          # json dosyasi nerede

# Boş bir film koleksiyonu oluşturun
film_koleksiyonu = []

# Film eklemek için bir fonksiyon tanımlayın
def film_ekle():
    film_adı = input("Film adını girin: ")
    yönetmen = input("Yönetmeni girin: ")
    yayın_yılı = input("Yayın yılını girin: ")
    tür = input("Film türünü girin: ")

    film = {
        'Ad': film_adı,
        'Yönetmen': yönetmen,
        'Yayın Yılı': yayın_yılı,
        'Tür': tür
    }

    film_koleksiyonu.append(film)                                 #Bu ne ise yaradi
    print(f"{film_adı} filmi koleksiyona eklendi.")

# Film düzenlemek için bir fonksiyon tanımlayın
def film_düzenle():
    film_adı = input("Düzenlemek istediğiniz film adını girin: ")
    for film in film_koleksiyonu:
        if film['Ad'] == film_adı:
            film['Yönetmen'] = input("Yeni yönetmeni girin: ")
            film['Yayın Yılı'] = input("Yeni yayın yılını girin: ")
            film['Tür'] = input("Yeni film türünü girin: ")
            print(f"{film_adı} filmi başarıyla düzenlendi.")
            return                                                #Bu nereye geri dondurdu
    print(f"{film_adı} filmi koleksiyonda bulunamadı.")

# Film silmek için bir fonksiyon tanımlayın
def film_sil():
    film_adı = input("Silmek istediğiniz film adını girin: ")
    for film in film_koleksiyonu:
        if film['Ad'] == film_adı:
            film_koleksiyonu.remove(film)
            print(f"{film_adı} filmi koleksiyondan silindi.")
            return                                                #Bu nereye geri dondurdu
    print(f"{film_adı} filmi koleksiyonda bulunamadı.")

# Koleksiyonu görüntülemek için bir fonksiyon tanımlayın
def koleksiyonu_görüntüle():                                      #Burada hangi islem butun koleksiyonu yazdiriyor
    print("\nFilm Koleksiyonu:")
    for film in film_koleksiyonu:
        print(f"Ad: {film['Ad']}")
        print(f"Yönetmen: {film['Yönetmen']}")
        print(f"Yayın Yılı: {film['Yayın Yılı']}")
        print(f"Tür: {film['Tür']}")
        print("\n")

# Filmleri bir JSON dosyasına kaydetmek için bir fonksiyon tanımlayın
def koleksiyonu_kaydet():                                       #Bunu hic anlamadim
    with open('film_koleksiyonu.json', 'w') as dosya:
        json.dump(film_koleksiyonu, dosya)

# Film koleksiyonunu bir JSON dosyasından yüklemek için bir fonksiyon tanımlayın
def koleksiyonu_yükle():                                       #Bunu hic anlamadim
    try:
        with open('film_koleksiyonu.json', 'r') as dosya:
            koleksiyon = json.load(dosya)
            return koleksiyon
    except FileNotFoundError:
        return []

# Başlangıçta koleksiyonu yükle
film_koleksiyonu = koleksiyonu_yükle()                 #Bu niye ekledi

# Ana döngü
while True:
    print("\nFilm Koleksiyonu Uygulaması")
    print("1. Film Ekle")
    print("2. Film Düzenle")
    print("3. Film Sil")
    print("4. Koleksiyonu Görüntüle")
    print("5. Filmleri Dosyaya Kaydet")
    print("6. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        film_ekle()
    elif secim == '2':
        film_düzenle()
    elif secim == '3':
        film_sil()
    elif secim == '4':
        koleksiyonu_görüntüle()
    elif secim == '5':
        koleksiyonu_kaydet()
        print("Film koleksiyonu dosyaya kaydedildi.")
    elif secim == '6':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")



#QUESTION 3 ANSWER

# Boş bir müşteri sözlüğü oluşturun (Müşteri kimliği ile müşteri bilgilerini ilişkilendireceğiz)
musteri_sozlugu = {}

# Müşteri eklemek için bir fonksiyon tanımlayın
def musteri_ekle():
    musteri_id = input("Müşteri Kimliği (ID) girin: ")
    ad = input("Müşteri Adı girin: ")
    soyad = input("Müşteri Soyadı girin: ")
    eposta = input("Müşteri E-Posta girin: ")
    telefon = input("Müşteri Telefon Numarası girin: ")

    musteri_bilgileri = {
        'Ad': ad,
        'Soyad': soyad,
        'E-Posta': eposta,
        'Telefon': telefon
    }

    musteri_sozlugu[musteri_id] = musteri_bilgileri
    print(f"{ad} {soyad} adlı müşteri başarıyla eklenmiştir.")


# Müşteri bilgilerini güncellemek için bir fonksiyon tanımlayın
def musteri_guncelle():
    musteri_id = input("Güncellemek istediğiniz müşterinin Kimliği (ID) girin: ")
    if musteri_id in musteri_sozlugu:
        print(f"Mevcut Müşteri Bilgileri:")
        for bilgi, deger in musteri_sozlugu[musteri_id].items():
            print(f"{bilgi}: {deger}")

        yeni_ad = input("Yeni Müşteri Adı (Değiştirmek istemiyorsanız boş bırakın): ")
        yeni_soyad = input("Yeni Müşteri Soyadı (Değiştirmek istemiyorsanız boş bırakın): ")
        yeni_eposta = input("Yeni Müşteri E-Posta (Değiştirmek istemiyorsanız boş bırakın): ")
        yeni_telefon = input("Yeni Müşteri Telefon (Değiştirmek istemiyorsanız boş bırakın): ")

        if yeni_ad:
            musteri_sozlugu[musteri_id]['Ad'] = yeni_ad
        if yeni_soyad:
            musteri_sozlugu[musteri_id]['Soyad'] = yeni_soyad
        if yeni_eposta:
            musteri_sozlugu[musteri_id]['E-Posta'] = yeni_eposta
        if yeni_telefon:
            musteri_sozlugu[musteri_id]['Telefon'] = yeni_telefon

        print("Müşteri bilgileri başarıyla güncellendi.")
    else:
        print(f"{musteri_id} müşterisi bulunamadı.")


# Müşteri silmek için bir fonksiyon tanımlayın
def musteri_sil():
    musteri_id = input("Silmek istediğiniz müşterinin Kimliği (ID) girin: ")
    if musteri_id in musteri_sozlugu:
        del musteri_sozlugu[musteri_id]
        print(f"{musteri_id} müşterisi başarıyla silindi.")
    else:
        print(f"{musteri_id} müşterisi bulunamadı.")


# Tüm müşterileri listeleme işlemi
def musterileri_listele():
    print("\nTüm Müşteriler:")
    for musteri_id, musteri_bilgileri in musteri_sozlugu.items():
        print(f"Müşteri Kimliği (ID): {musteri_id}")
        for bilgi, deger in musteri_bilgileri.items():
            print(f"{bilgi}: {deger}")
        print("\n")


# Ana döngü
while True:
    print("\nMüşteri Yönetim Sistemi")
    print("1. Müşteri Ekle")
    print("2. Müşteri Güncelle")
    print("3. Müşteri Sil")
    print("4. Tüm Müşterileri Listele")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        musteri_ekle()
    elif secim == '2':
        musteri_guncelle()
    elif secim == '3':
        musteri_sil()
    elif secim == '4':
        musterileri_listele()
    elif secim == '5':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")


#HACKERRANK QUESTION 1 ANSWER
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list=[[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k!=n]

    print(list)
      

#HACKERRANK QUESTION 2 ANSWER
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

# kodun ne amacladigini anlamadim


#HACKERRANK QUESTION 3 ANSWER
if __name__ == '__main__':
    Students = []
    Scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
    Students.append((name, score))                                 #Bu ne ise yaradi
    Scores.add(score)

    second_lowest = sortes(scores)[1]
    print(*sorted([name for name, score in Students if score==second_lowest]),sep='\n')
