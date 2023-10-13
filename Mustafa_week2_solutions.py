###Soru1: Öğrenci Notları İşleme###
ogrenci_dict = {"ahmet demir" :[50,66,45],"mehmet kaya":[80,66,75],
                "ali al":[70,69,95],"yigit duru":[50,46,65],
                "selim can":[50,60,75],"oguz kale":[40,69,63],
                "ihsan yilmaz":[90,64,77],"alperen bahadir":[60,46,36],
                "anil ulu":[55,88,75],"bora helvaci":[90,96,85],}

ortalama = {}
yuksek_ortalama = 0
for key, value in ogrenci_dict.items():
        sum = 0
        count = 0
        for i in value:
            sum += i
            count += 1
        average = sum/count # ortalama buldum
        ogrenci_dict[key] = (ogrenci_dict[key], average)# ogrenci ortalamalarini bu satirla kutuphaneye ekledim.

        print(key,"{:.2f}".format(average),)
print(ogrenci_dict)
    
en_buyuk_anahtar, en_buyuk_deger = max(ogrenci_dict.items(), key=lambda x: x[1]) # soru 1 cevap 2 
print("en yuksek ortalamaya sahip ogrenci = ",en_buyuk_anahtar)


adlar = []
soyadlar = []

# Sözlüğü dönerek adları, soyadları ve notları  listelere ekledim
for ogrenci in ogrenci_dict:
    ad, soyad = ogrenci.split(" ")  # Ad ve soyadı ayırdim
    adlar.append(ad)
    soyadlar.append(soyad)
    

# Elde edilen listeleri görüntüle
print("Adlar:", adlar)
print("Soyadlar:", soyadlar)

adlar.sort()
print("alfabetik siralamaya gore isimler: ",adlar) # isimlerin siralandigi liste

notu_70_alti_ogrenciler = set() # sete donusturmek icin bos kueli set tanimladim

for key, (value1,value2) in ogrenci_dict.items():
     
    if value2 < 70:
        notu_70_alti_ogrenciler.add(key)
print(notu_70_alti_ogrenciler)






###Soru 2 : Film Kütüphanesi Yönetim Sistemi Projesi###

filmler = []
film_numarasi_artir = 1

def film_liste():
    print("\nTüm :")
    if not filmler:
        print("Henüz hiç film eklenmemiş.")
    else:
        for film in filmler:
            print(f"{film['Sira Numarasi']}: {film['Filmin Adi']} ({film['Filmin Yonetmeni']}) ({film['Filmin Yayinyili']})({film['Filmin Turu']})")

def film_ekle():
    global film_numarasi_artir
    film_adi = input("Yeni filmin adini girin: ")
    film_yonetmen = input("FIlmin yonetmeninin adini girin: ")
    film_yayinyili = input("Filmin yayinyilini girin: ")
    film_turu = input("Filmin turunu girin: ")
    film = {
        "Sira Numarasi": film_numarasi_artir,
        "Filmin Adi": film_adi,
        "Filmin Yonetmeni": film_yonetmen,
        "Filmin Yayinyili": film_yayinyili,
        "Filmin Turu": film_turu  
    }
    filmler.append(film)
    film_numarasi_artir+= 1
    print("Yeni film eklendi: ", film_adi)


def film_duzenle():
    film_liste()
    global film_numarasi_artir 
    film_numarasi= int(input("Duzenlenecek filmin numarasini girin: "))
    for film in filmler:
        if film["Sira Numarasi"] == film_numarasi:
            filmler.remove(film)
            for i, film in enumerate(filmler):
                film['Sira Numarasi'] = i + 1    
    film_numarasi_artir -= 1 
    film_ekle()


def film_sil():
    film_liste()
    global film_numarasi_artir   
    film_numarasi= int(input("Silinecek filmin numarasini girin: "))
    for film in filmler:
        if film["Sira Numarasi"] == film_numarasi:
            filmler.remove(film)
            
            for i, film in enumerate(filmler):
                film['Sira Numarasi'] = i + 1
            print(film_numarasi , " numarali  film silindi. ")
    film_numarasi_artir -= 1 
          

while True:
    print("\nFilm Kütüphanesi İşlemleri:")
    print("1. Film Ekle")
    print("2. Film Düzenle")
    print("3. Film Sil ")
    print("4. Film listesini gor ")
    print("5. Cikis")
    print("/////////////////////////////////")
    secim = int(input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): "))
    
    if secim == 1:
        film_ekle()
    elif secim == 2:
        film_duzenle()
    elif secim == 3:
        film_sil()
    elif secim == 4:
        film_liste()
    elif secim == 5:
        print("Uygulamadan cikiliyor")
        break
    else:
        print("Geçersiz seçenek, tekrar deneyin.")


### Soru 3 :Müşteri Yönetim Sistemi ###

musteriler= []
musteri_numarasi_artir = 1

def musteri_liste():
    print("\nTüm Musteriler:")
    if not musteriler:
        print("Henüz hiç musteri eklenmemiş.")
    else:
        for musteri in musteriler:
            print(f"{musteri['Sira Numarasi']}: {musteri['Musteri Adi']} ({musteri['Musteri Soyadi']}) ({musteri['Musteri Mail']})({musteri['Musteri Telefon']})")

def musteri_ekle():
    global musteri_numarasi_artir
    musteri_adi = input("Musterinin adini girin: ")
    musteri_soyad = input("Musterinin soyadini girin: ")
    musteri_mail = input("Mail girin: ")
    musteri_telefon = input("Telefon numarasi girin: ")
    musteri = {
        "Sira Numarasi": musteri_numarasi_artir,
        "Musteri Adi": musteri_adi,
        "Musteri Soyadi": musteri_soyad,
        "Musteri Mail": musteri_mail,
        "Musteri Telefon": musteri_telefon  
    }
    musteriler.append(musteri)
    musteri_numarasi_artir+= 1
    print("Yeni musteri eklendi: ", musteri_adi)


def musteri_guncelle():
    musteri_liste()
    global musteri_numarasi_artir
    musteri_numarasi= int(input("GUncellenecek musterinin numarasini girin: "))
    for musteri in musteriler:
        if musteri["Sira Numarasi"] == musteri_numarasi:
            musteriler.remove(musteri)
            for i, musteri in enumerate(musteriler):
                musteri['Sira Numarasi'] = i + 1    
    musteri_numarasi_artir -= 1 
    musteri_ekle()


def muster_sil():
    musteri_liste()
    global musteri_numarasi_artir  
    musteri_numarasi= int(input("Silinecek musterinin numarasini girin: "))
    for musteri in musteriler:
        if musteri["Sira Numarasi"] == musteri_numarasi:
            musteriler.remove(musteri)
            
            for i, musteri in enumerate(musteriler):
                musteri['Sira Numarasi'] = i + 1
            print(musteri_numarasi , " numarali  film silindi. ")
    musteri_numarasi_artir -= 1 
          

while True:
    print("\nMusteri Yonetim Sistemi:")
    print("1. Yeni Musteri Ekle")
    print("2. Musteri Bilgi Guncelleme")
    print("3. Musteriyi Sil ")
    print("4. Musteri listesini gor ")
    print("5. Cikis")
    print("/////////////////////////////////")
    secim = int(input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): "))
    
    if secim == 1:
        musteri_ekle()
    elif secim == 2:
        musteri_guncelle()
    elif secim == 3:
        muster_sil()
    elif secim == 4:
        musteri_liste()
    elif secim == 5:
        print("Uygulamadan cikiliyor")
        break
    else:
        print("Geçersiz seçenek, tekrar deneyin.")


### Hackerrank list comprehensions ###

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    q = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) 
    if a+b+c != n]
    print(q)



### Hackerrank tuples python###
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))




###Hackerrank nestedlist###
if __name__ == '__main__':
    ogrenciler = {}
    notlar = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in ogrenciler:
            ogrenciler[score].append(name)
        else:
            ogrenciler[score] = [name]
        if score not in notlar:
            notlar.append(score)
    deger = sorted(notlar)[1]
    ogrenciler[deger].sort()
    for i in ogrenciler[deger]:
        print(i)
            
            
            
