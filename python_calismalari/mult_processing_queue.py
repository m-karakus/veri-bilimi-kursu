import time
import multiprocessing


def h_karesi(sayilar,q):
    for sayi in sayilar:
        sonuc = sayi*sayi
        q.put(sonuc)
    return 


if __name__ == "__main__":
    baslangic_zamani = time.time()
    array = [1,2,3,5]

    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=h_karesi,args=(array,q))

    p1.start()
    p1.join()

    bitis_zamani = time.time()
    print("Bitti! Toplam süre:", (bitis_zamani-baslangic_zamani),"sn")

    while q.empty() is False:
        print(q.get())
