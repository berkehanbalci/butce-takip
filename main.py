harcama_metni = input("Kac harcama gireceksin:")
harcama = int(harcama_metni)
toplam = 0

if harcama > 0:
    for i in range(harcama):   
        tutar_metni = input(f"Lutfen {i+1}. harcama tutarini giriniz:")
        tutar = float(tutar_metni)
        toplam = toplam + tutar
    print(f"Toplam tutar: {toplam}")    
    ortalama = toplam / harcama
    print(f"Ortalama tutar: {ortalama}")
else:
    print("Lutfen gecerli bir harcama giriniz")        



