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



'''
Proje Açıklaması: Bu proje, kullanıcının kendi film koleksiyonunu yönetmesine yardımcı olacak bir uygulama oluşturmayı amaçlar. Kullanıcılar filmleri ekleyebilir, düzenleyebilir, silebilir ve koleksiyonlarını görüntüleyebilir.
Kullanılan Veri Yapıları: Sözlükler (filmleri ve ilgili bilgileri saklamak için), listeler (film koleksiyonunu görüntülemek için)
Temel İşlevler:
1-Kullanıcıdan film adı, yönetmen, yayın yılı ve tür gibi bilgileri alarak bir film verisi oluşturun ve bunu bir sözlükte saklayın.
2-Kullanıcıya bir filmi düzenleme veya silme seçeneği sunun.(Bunun icin filme ait hangi veriyi degistirmek istiyorlarsa ona uygun bir fonksiyon yazilmasi gerekir.)
3-Kullanıcının koleksiyonunu görüntülemesine izin verin. Tüm filmleri listeleyin veya tür veya yayın yılı gibi kriterlere göre filtreleyin.
4-Film verilerini bir dosyada saklayın ve programı başlattığınızda bu veriyi geri yükleyin.
'''