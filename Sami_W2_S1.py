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

'''
Soru1: Öğrenci Notları İşleme
Bir öğrenci notlarını işlemek için bir Python programı yazmanız gerekiyor. Programın aşağıdaki işlevleri yerine getirmesi gerekiyor:

Bir sözlük kullanarak 10 öğrencinin bilgilerini ve notlarını saklayın. Her öğrencinin adı, soyadı ve notları(Vize, Final ve Sozlu notu) olsun.
1-Her öğrencinin not ortalamasını hesaplayın ve sözlüğe ekleyin.
2-En yüksek not ortalamasına sahip öğrenciyi bulun ve ekrana yazdırın.
3-Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin.
4-Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.
5-Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın.
'''
