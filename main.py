toplam = 0
harcamalar = []

while True:   
    tutar_metni = input("Lutfen harcama giriniz (çikmak için q): ")
    if tutar_metni == "q":
        break
    aciklama = input(f"Lutfen harcamanizin ne oldugunu giriniz: ")
    tutar = float(tutar_metni)
    yeniharcama = {"aciklama": aciklama, "tutar": tutar}
    harcamalar.append(yeniharcama)
    toplam = toplam + tutar
if len(harcamalar) > 0:
    for eleman in harcamalar:
        print(f"{eleman['aciklama']}: {eleman['tutar']} TL")  
    print(f"Toplam tutar: {toplam}")    
    ortalama = toplam / len(harcamalar)
    print(f"Ortalama tutar: {ortalama}")   
else:
    print("Hiç harcama girilmedi")         



