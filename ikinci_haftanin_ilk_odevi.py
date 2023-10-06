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
