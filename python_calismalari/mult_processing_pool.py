from multiprocessing import Pool
import time

def f(n):
    c = 0
    for i in range(1000):
        c = c + (i*i)
    return n*n

if __name__ == "__main__":
    baslangic_zamani = time.time()
    array = range(10000)

    p = Pool(processes=3)

    # sonuc = p.map(f,array)
    # p.close()
    # p.join()

    sonuc = []
    for n in array:
        sonuc.append(f(n))

    # print(sonuc)
    bitis_zamani = time.time()
    print("Bitti! Toplam süre:", (bitis_zamani-baslangic_zamani),"sn")