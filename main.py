import json
harcamalar = []
try:
    with open("harcamalar.json", "r", encoding="utf-8") as dosya:
        harcamalar = json.load(dosya)
except FileNotFoundError:
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
    else:
        print("Lütfen geçerli bir tutar giriniz") 
toplam = 0
for eleman in harcamalar:
    toplam = toplam + eleman["tutar"]        
if len(harcamalar) > 0:
    with open("harcamalar.json", "w", encoding="utf-8") as dosya:
        json.dump(harcamalar, dosya,  ensure_ascii=False)
    for eleman in harcamalar:
        print(f"{eleman['aciklama']}: {eleman['tutar']} TL")  
    print(f"Toplam tutar: {toplam}")    
    ortalama = toplam / len(harcamalar)
    print(f"Ortalama tutar: {ortalama}")   
else:
    print("Hiç harcama girilmedi")         



