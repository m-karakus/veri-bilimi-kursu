import time
import multiprocessing

def para_al(balance,kilit):
    for i in range(100):
        #time.sleep(0.01)
        kilit.acquire()
        balance.value = balance.value + 1
        kilit.release()
    return 

def harcama_yap(balance,kilit):
    for i in range(100):
        #time.sleep(0.01)
        kilit.acquire()
        balance.value = balance.value - 1
        kilit.release()
    return 


if __name__ == "__main__":
    for i in range(100):
        baslangic_zamani = time.time()
        balance = multiprocessing.Value("i",200)

        kilit = multiprocessing.Lock()
        p1 = multiprocessing.Process(target=para_al,args=(balance,kilit))
        p2 = multiprocessing.Process(target=harcama_yap,args=(balance,kilit))

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        print(balance.value)
        bitis_zamani = time.time()
        # print("Bitti! Toplam süre:", (bitis_zamani-baslangic_zamani),"sn")


