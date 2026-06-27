import json
def harcamalari_yükle():
    try:
        with open("harcamalar.json", "r", encoding="utf-8") as dosya:
            harcamalar = json.load(dosya)
    except FileNotFoundError:
        harcamalar = []
    return harcamalar
def harcamalari_kaydet(harcamalar):
    with open("harcamalar.json", "w", encoding="utf-8") as dosya:
        json.dump(harcamalar, dosya,  ensure_ascii=False)
def harcamalari_topla(harcamalar):
    while True:
        tutar_metni = input("Lutfen harcama giriniz (çikmak için q): ")
        if tutar_metni == "q":
            break
        tutar = float(tutar_metni)
        if tutar > 0:
            aciklama = input(f"Lutfen harcamanizin ne oldugunu giriniz: ")
            kategori = input(f"Lutfen harcamaninizin kategorisini giriniz: ")
            yeniharcama = {"aciklama": aciklama, "tutar": tutar, "kategori": kategori}
            harcamalar.append(yeniharcama)
        else:
            print("Lütfen geçerli bir tutar giriniz")
    return harcamalar
def rapor_göster(harcamalar, toplam):
    for eleman in harcamalar:
        print(f"{eleman['aciklama']}: {eleman['tutar']} TL ({eleman.get('kategori','belirsiz')})")
    print(f"Toplam tutar: {toplam}")
    ortalama = toplam / len(harcamalar)
    print(f"Ortalama tutar: {ortalama}")
harcamalar = harcamalari_yükle()
harcamalar = harcamalari_topla(harcamalar)          
toplam = 0
for eleman in harcamalar:
    toplam = toplam + eleman["tutar"]
if len(harcamalar) > 0:
    harcamalari_kaydet(harcamalar)
    rapor_göster(harcamalar, toplam)
else:
    print("Hiç harcama girilmedi")
