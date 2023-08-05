import time
import threading

def h_karesi(sayilar):
    for sayi in sayilar:
        time.sleep(0.2)
        sonuc = sayi*sayi
        print("kare:",sayi)
    return 

def h_kupu(sayilar):
    for sayi in sayilar:
        time.sleep(0.2)
        sonuc = sayi*sayi*sayi
        print("küp:",sayi)
    return 

baslangic_zamani = time.time()
array = [1,2,3,4,5,6,7]

t1 = threading.Thread(target=h_karesi,args=(array,))
t2 = threading.Thread(target=h_kupu,args=(array,))

t1.start()
t2.start()

t1.join()
t2.join()

bitis_zamani = time.time()
print("Bitti! Toplam süre:", (bitis_zamani-baslangic_zamani),"sn")


