import json
def harcamalari_yukle():
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
            kategori = input(f"Lutfen harcamanizin kategorisini giriniz: ")
            yeniharcama = {"aciklama": aciklama, "tutar": tutar, "kategori": kategori}
            harcamalar.append(yeniharcama)
        else:
            print("Lütfen geçerli bir tutar giriniz")
    return harcamalar
def rapor_goster(harcamalar, toplam):
    for eleman in harcamalar:
        print(f"{eleman['aciklama']}: {eleman['tutar']} TL ({eleman.get('kategori','belirsiz')})")
    print(f"Toplam tutar: {toplam}")
    ortalama = toplam / len(harcamalar)
    print(f"Ortalama tutar: {ortalama}")
def kategori_raporu(harcamalar):
    kategori_toplamlari = {}
    for eleman in harcamalar:
        kategori = eleman.get("kategori", "belirsiz")
        tutar = eleman["tutar"]
        if kategori in kategori_toplamlari:
            kategori_toplamlari[kategori] += tutar
        else:
            kategori_toplamlari[kategori] = tutar
    print("=== KATEGORİ RAPORU ===")
    for kategori, kategori_tutari in kategori_toplamlari.items():
        print(f"{kategori}: {kategori_tutari} TL")    
harcamalar = harcamalari_yukle()
harcamalar = harcamalari_topla(harcamalar)          
toplam = 0    
for eleman in harcamalar:
    toplam = toplam + eleman["tutar"]
if len(harcamalar) > 0:
    harcamalari_kaydet(harcamalar)
    rapor_goster(harcamalar, toplam)
    kategori_raporu(harcamalar)
else:
    print("Hiç harcama girilmedi")
