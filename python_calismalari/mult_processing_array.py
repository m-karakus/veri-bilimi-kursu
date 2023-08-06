import time
import multiprocessing


def h_karesi(sayilar,sonuclar,d):
    d.value = 1.5
    for idx, sayi in enumerate(sayilar):
        sonuclar[idx] = sayi*sayi
    return 


if __name__ == "__main__":
    baslangic_zamani = time.time()
    array = [1,2,3]


    sonuclar = multiprocessing.Array('i',3)
    d = multiprocessing.Value("d",0.0)
    p1 = multiprocessing.Process(target=h_karesi,args=(array,sonuclar,d))

    p1.start()
    p1.join()

    bitis_zamani = time.time()
    print("Bitti! Toplam süre:", (bitis_zamani-baslangic_zamani),"sn")
    print(sonuclar[:])
    print(d.value)


