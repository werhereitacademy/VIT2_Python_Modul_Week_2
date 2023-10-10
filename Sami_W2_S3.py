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

    

'''
Soru 3 :Müşteri Yönetim Sistemi
Proje Açıklaması: Bu proje, müşterilerinizi yönetmek ve temel işlemleri gerçekleştirmek için kullanabileceğiniz bir müşteri yönetim sistemi oluşturmanızı içerir.
Bu sistem, müşteri bilgilerini saklama, yeni müşteri ekleyebilme, müşteri bilgilerini güncelleyebilme, müşteri silme ve müşteri listesini görüntüleme gibi temel işlevlere sahip olacaktır.
 İşte projenin temel adımları:

1-Müşteri bilgilerini saklamak için bir sözlük yapısı kullanın. Her müşteri için bir benzersiz müşteri kimliği (ID) atayın ve müşteri bilgilerini bu kimlikle ilişkilendirin.
 Her müşteri için ad, soyad, e-posta, telefon gibi bilgileri içeren bir sözlük kullanabilirsiniz.

2-Kullanıcıya aşağıdaki işlemleri seçebileceği bir menü sunun:

Yeni müşteri eklemek
Müşteri bilgilerini güncellemek
Müşteri silmek
Tüm müşterileri listelemek
Çıkış yapmak
3-Kullanıcının seçimine göre ilgili işlemi gerçekleştirin. Örneğin, yeni müşteri eklerken kullanıcıdan gerekli bilgileri alın ve sözlüğe yeni bir müşteri ekleyin.

4-Müşteri bilgilerini güncellerken, müşteri kimliğini kullanarak mevcut bilgileri görüntüleyin ve güncellenmiş bilgileri kaydedin.

5-Müşteri silme işleminde kullanıcıdan müşteri kimliğini alın ve bu müşteriyi sözlükten silin.

6-Tüm müşterileri listeleme işleminde, mevcut müşterilerin listesini görüntüleyin.

7-Kullanıcı çıkış yapana kadar işlemleri tekrarlayın.
'''