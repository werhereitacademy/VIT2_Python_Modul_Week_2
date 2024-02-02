'''Soru1: Öğrenci Notları İşleme
Bir öğrenci notlarını işlemek için bir Python programı yazmanız gerekiyor. Programın aşağıdaki işlevleri yerine getirmesi gerekiyor:

Bir sözlük kullanarak 10 öğrencinin bilgilerini ve notlarını saklayın. Her öğrencinin adı, soyadı ve notları(Vize, Final ve Sozlu notu) olsun
'''


ogrenciler = {
    'Aysima Coskun':  [90, 85, 75],
    'Suheyb Coskun':  [35, 60, 50],
    'Guluzar Coskun': [68, 88, 78],
    'Derya Seker': [65, 87,86],
    'Gamze Yilmaz': [78, 88, 78],
    'Ahmet Furkan': [88, 66, 56],
    'Elif SEN': [78, 58, 88],
    'Ender Yilmaz': [77, 88, 67],
    'Dilan Demir': [99, 88, 77],
    'Duygu Seker': [69, 88, 78]
}

#1-Her öğrencinin not ortalamasını hesaplayın ve sözlüğe ekleyin.

def ortalama_hesaplama(notlar):
    return sum(notlar) /len(notlar)

isimler = ogrenciler.keys()

for isim in isimler:
    #hem notlari hem ortalamayi daha sonra kullanacagim icin ikisinide degiskenlere atadim.
    
    ogrenci_notlari = ogrenciler[isim]
    ortalama = int(ortalama_hesaplama(ogrenci_notlari))
    ogrenciler[isim] = {'ortalama': ortalama, 'notlar': ogrenci_notlari}
print(ogrenciler)

#2-En yüksek not ortalamasına sahip öğrenciyi bulun ve ekrana yazdırın.

en_yuksek_not_ortalamasi = 0
en_yuksek_not_ortalamasi_ogrencisi = ""

for isim in ogrenciler:
    ortalama = ogrenciler[isim]['ortalama']
    if ortalama > en_yuksek_not_ortalamasi:
        en_yuksek_not_ortalamasi = ortalama
        en_yuksek_not_ortalamasi_ogrencisi = isim
print("En yuksek not ortalamasina sahip ogrenci: {}".format (en_yuksek_not_ortalamasi_ogrencisi))



#3-Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin.


list_of_tuple_names = []
for isim in ogrenciler:
    isim_listesi = tuple(isim.split())
    list_of_tuple_names.append(isim_listesi)
print(list_of_tuple_names)
    

#4-Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.

print(sorted(isimler))
    
#5-Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın.

set_of_students = set([])
for isim in ogrenciler:
    if ogrenciler[isim]['ortalama'] < 70 :
        set_of_students.add(isim)
    
print(set_of_students)