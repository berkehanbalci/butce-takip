toplam = 0
harcamalar = []

while True:   
    tutar_metni = input("Lutfen harcama giriniz (çikmak için q): ")
    if tutar_metni == "q":
        break    
    tutar = float(tutar_metni)
    if tutar > 0:
        aciklama = input(f"Lutfen harcamanizin ne oldugunu giriniz: ")
        yeniharcama = {"aciklama": aciklama, "tutar": tutar}
        harcamalar.append(yeniharcama)
        toplam = toplam + tutar
    else:
        print("Lütfen geçerli bir tutar giriniz")    
if len(harcamalar) > 0:
    for eleman in harcamalar:
        print(f"{eleman['aciklama']}: {eleman['tutar']} TL")  
    print(f"Toplam tutar: {toplam}")    
    ortalama = toplam / len(harcamalar)
    print(f"Ortalama tutar: {ortalama}")   
else:
    print("Hiç harcama girilmedi")         



