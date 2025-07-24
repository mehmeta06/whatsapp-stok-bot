def stok_arama(sorgu):
    ornek_stok = [
        {"isim": "22 Ayar Altın Bilezik A", "tur": "bilezik", "malzeme": "22 ayar", "fiyat": 8500},
        {"isim": "22 Ayar Altın Yüzük B", "tur": "yüzük", "malzeme": "22 ayar", "fiyat": 4200},
        {"isim": "Gümüş Kolye C", "tur": "kolye", "malzeme": "gümüş", "fiyat": 600}
    ]

    sonuc = []
    for urun in ornek_stok:
        if sorgu["urun_turu"] in urun["tur"].lower():
            if sorgu["malzeme"] in urun["malzeme"]:
                if not sorgu.get("maksimum_fiyat") or urun["fiyat"] <= sorgu["maksimum_fiyat"]:
                    sonuc.append(urun)
    return sonuc
