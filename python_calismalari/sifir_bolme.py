a = 7
b = 0

try:
    sonuc = a/b
    print(sonuc)
except Exception as e:
    print(e)
    sonuc = 0
    print(sonuc)
finally:
    sonuc = sonuc * 2
    print(sonuc)


print(1+3)