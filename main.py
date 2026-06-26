harcama_metni = input("Kac harcama gireceksin:")
harcama = int(harcama_metni)
toplam = 0
harcamalar = []

if harcama > 0:
    for i in range(harcama):   
        tutar_metni = input(f"Lutfen {i+1}. harcama tutarini giriniz:")
        aciklama = input(f"Lutfen {i+1}. harcamanizin ne oldugunu giriniz:")
        tutar = float(tutar_metni)
        yeniharcama = {"aciklama": aciklama, "tutar": tutar}
        harcamalar.append(yeniharcama)
        toplam = toplam + tutar
    for eleman in harcamalar:
        print(f"{eleman['aciklama']}: {eleman['tutar']} TL")  
    print(f"Toplam tutar: {toplam}")    
    ortalama = toplam / harcama
    print(f"Ortalama tutar: {ortalama}")
else:
    print("Lutfen gecerli bir harcama giriniz")        



