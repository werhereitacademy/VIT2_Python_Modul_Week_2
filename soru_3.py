#Müşteri Yönetim Sistemi

#Proje Açıklaması: Bu proje, müşterilerinizi yönetmek ve temel işlemleri gerçekleştirmek için kullanabileceğiniz bir müşteri yönetim sistemi oluşturmanızı içerir. Bu sistem, müşteri bilgilerini saklama, yeni müşteri ekleyebilme, müşteri bilgilerini güncelleyebilme, müşteri silme ve müşteri listesini görüntüleme gibi temel işlevlere sahip olacaktır. İşte projenin temel adımları:'''


#1-Müşteri bilgilerini saklamak için bir sözlük yapısı kullanın. Her müşteri için bir benzersiz müşteri kimliği (ID) atayın ve müşteri bilgilerini bu kimlikle ilişkilendirin. Her müşteri için ad, soyad, e-posta, telefon gibi bilgileri içeren bir sözlük kullanabilirsiniz.

# 2-Kullanıcıya aşağıdaki işlemleri seçebileceği bir menü sunun:

# Yeni müşteri eklemek
# Müşteri bilgilerini güncellemek
# Müşteri silmek
# Tüm müşterileri listelemek
# Çıkış yapmak

# 3-Kullanıcının seçimine göre ilgili işlemi gerçekleştirin. Örneğin, yeni müşteri eklerken kullanıcıdan gerekli bilgileri alın ve sözlüğe yeni bir müşteri ekleyin.

# 4-Müşteri bilgilerini güncellerken, müşteri kimliğini kullanarak mevcut bilgileri görüntüleyin ve güncellenmiş bilgileri kaydedin.

# 5-Müşteri silme işleminde kullanıcıdan müşteri kimliğini alın ve bu müşteriyi sözlükten silin.

# 6-Tüm müşterileri listeleme işleminde, mevcut müşterilerin listesini görüntüleyin.

# 7-Kullanıcı çıkış yapana kadar işlemleri tekrarlayın.

# Müşteri bilgilerini saklamak için bir sözlük oluşturun (müşteri kimliği anahtar olarak kullanılır)



musteri_bilgileri = {}
musteri_id = 1

while True:
    print("\n1. Yeni musteri ekleyin\n2. Musteri bilgilerini guncelleyin\n3. Musteriyi silin\n4. Tum musterileri listeleyin\n5. Cikis yapin")
    
    secim = input("Lutfen bir islem secin (1-5): ")
    if secim == "1":
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        e_posta = input("E-posta: ")
        telefon = input("Telefon: ")
        
        musteri_bilgileri[musteri_id] = {
            'ad': ad,
            'soyad': soyad,
            'email': e_posta,
            'telefon': telefon
        }
        musteri_id += 1
        print(musteri_bilgileri)
        
    elif secim == "2":
        print(musteri_bilgileri)
        guncellenen_musteri_id = int(input("Guncellenecek musteri kimligi: "))
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        e_posta = input("E-posta: ")
        telefon = input("Telefon: ")
        
        musteri_bilgileri[guncellenen_musteri_id] = {
            'ad': ad,
            'soyad': soyad,
            'email': e_posta,
            'telefon': telefon
        }
    
        print ("Musteri bilgileri guncellendi!")
        print (musteri_bilgileri)
        
    elif secim =="3":
        print(musteri_bilgileri)
        silinecek_musteri_id = int(input("Silinecek musteri kimligi: "))
        del musteri_bilgileri[silinecek_musteri_id]
        print("isleminiz basariyla gerceklesti.")
        print(musteri_bilgileri)
        
    elif secim == "4":
        print(musteri_bilgileri)
        
    elif secim == "5":
        print("Cikis yapiliyor . . .")
        print("HOSCAKALIN")
        break
        
    else:
        print("Gecersiz bir secim! Lutfen 1-5 arasinda secim yapiniz.")
        
    
        
    