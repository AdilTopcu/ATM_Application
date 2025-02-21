import json

kullanici_listesi = [
    {'ad': 'Adil', 'cinsiyet': 'erkek', 'hesapNo': '11111', 'bakiye': 13000, 'ekHesapBakiye': 12000,'limit':12000},
    {'ad': 'Mete', 'cinsiyet': 'erkek', 'hesapNo': '22222', 'bakiye': 4000, 'ekHesapBakiye': 2500,'limit':2500},
    {'ad': 'Mustafa', 'cinsiyet': 'erkek', 'hesapNo': '33333', 'bakiye': 63000, 'ekHesapBakiye': 22000,'limit':22000},
    {'ad': 'Melis', 'cinsiyet': 'kız', 'hesapNo': '44444', 'bakiye': 16000, 'ekHesapBakiye': 10000,'limit':10000},
    {'ad': 'Nurcan', 'cinsiyet': 'kız', 'hesapNo': '55555', 'bakiye': 33000, 'ekHesapBakiye': 22000,'limit':22000},
    {'ad': 'Serap', 'cinsiyet': 'kız', 'hesapNo': '66666', 'bakiye': 34000, 'ekHesapBakiye': 32000,'limit':32000}
]

def veriKayitFonk():
    with open('kullanici_verileri.json', 'w') as file:
        json.dump(kullanici_listesi, file, indent=4)

def veriOkumaFonk():
    try:
        with open('kullanici_verileri.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return kullanici_listesi

def cekimYapma(kullanici, miktar):
    global kullanici_listesi
    toplamPara = kullanici['bakiye'] + kullanici['ekHesapBakiye']
    if toplamPara >= miktar:
        if kullanici['bakiye'] >= miktar:
            kullanici['bakiye'] -= miktar
        else:
            ekHesapKullanimi = input('Hesap bakiyeniz yetersiz, ek hesap bakiyesini kullanmak ister misiniz? (E/H):')
            if ekHesapKullanimi == 'E':
                kullanici['ekHesapBakiye'] -= (miktar - kullanici['bakiye'])
                kullanici['bakiye'] = 0
                
            elif ekHesapKullanimi == 'H':
                print("Üzgünüz, yetersiz bakiye.")
    else:
        print("Yetersiz bakiye.Lütfen limit arttırımı için en yakın şubeye başvurunuz.")
    veriKayitFonk()
    return kullanici

def paraYatir(kullanici, miktar):
    borc = kullanici['limit'] - kullanici['ekHesapBakiye']
    if miktar <= borc:
        kullanici['ekHesapBakiye'] += miktar
        kullanici['bakiye'] = 0
    else:
        kullanici['ekHesapBakiye'] = kullanici['limit']
        kullanici['bakiye'] += (miktar - borc)
    veriKayitFonk()
    return kullanici

kullanici_hesap_no = input("Hesap numaranızı giriniz: ")
islem = input("Hangi işlemi yapmak istiyorsunuz. Para çek( PARA ÇEK) Para yatır (PARA YATIR) diyebilirsiniz.").lower()
miktar = int(input("işlem yapmak istediğiniz para miktarı giriniz: "))

kullanici_listesi = veriOkumaFonk()
kullaniciBulundu = False
for kullanici in kullanici_listesi:
    if kullanici['hesapNo'] == kullanici_hesap_no:
        hitap = 'Bey' if kullanici['cinsiyet'] == 'erkek' else 'Hanım'
        if islem == 'para çek':
            kullanici = cekimYapma(kullanici, miktar)
        elif islem == 'para yatır':
            kullanici = paraYatir(kullanici, miktar)
        print(f"Güncel bakiyeniz: Ana hesap: {kullanici['bakiye']} \n                  Ek hesap: {kullanici['ekHesapBakiye']}")
        kullaniciBulundu = True
        break

if not kullaniciBulundu:
    print("Hesap numaranız sistemde bulunamadı. Lütfen geçerli bir hesap numarası giriniz.")

