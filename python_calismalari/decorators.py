import time

def zamani_olc(func):
    def sarmal(*args,**kwargs):
        baslangic = time.time()
        sonuc = func(*args,**kwargs)
        bitis = time.time()
        print(func.__name__,"fonksiyonu şu kadar sürdü:",(bitis-baslangic)*1000,"milisaniye")
        return sonuc
    return sarmal

@zamani_olc
def h_karesi(sayilar):
    sonuc = []
    for sayi in sayilar:
        sonuc.append(sayi*sayi)
    return sonuc

@zamani_olc
def h_kupu(sayilar):
    sonuc = []
    for sayi in sayilar:
        sonuc.append(sayi*sayi*sayi)
    return sonuc

@zamani_olc
def h_4uncu_kuv(sayilar):
    sonuc = []
    for sayi in sayilar:
        sonuc.append(sayi*sayi*sayi*sayi)
    return sonuc

array = range(1,100000)
cikti_kup = h_4uncu_kuv(array)

