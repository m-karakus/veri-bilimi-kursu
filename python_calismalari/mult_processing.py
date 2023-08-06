import time
import multiprocessing

sonuclar = []
def h_karesi(sayilar):
    for sayi in sayilar:
        time.sleep(0.2)
        sonuc = sayi*sayi
        sonuclar.append(sonuc)
        print("kare:",sayi)
    return 

def h_kupu(sayilar):
    for sayi in sayilar:
        time.sleep(0.2)
        sonuc = sayi*sayi*sayi
        print("küp:",sayi)
    return 


if __name__ == "__main__":
    baslangic_zamani = time.time()
    array = [1,2,3,4,5,6,7]

    p1 = multiprocessing.Process(target=h_karesi,args=(array,))
    p2 = multiprocessing.Process(target=h_kupu,args=(array,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    bitis_zamani = time.time()
    print("Bitti! Toplam süre:", (bitis_zamani-baslangic_zamani),"sn")
    print(sonuclar)


