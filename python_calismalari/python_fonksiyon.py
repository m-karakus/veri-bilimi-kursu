ali=[10,40,55,81,11]
veli=[101,1,3,7,41]

toplam =0
def toplama(lis):
    """
    Bu fonksiyon listenin değerlerini toplar ve donuş değeri olarak toplanan sayıyı verir.
    """
    toplam = 0
    for i in lis:
        toplam = i + toplam
    print(toplam)
    return toplam

print(toplam)

t = toplama(ali)
print(toplam)
print("Alinin toplam parası:",t)
print("Velini toplam parası:",toplama(veli))