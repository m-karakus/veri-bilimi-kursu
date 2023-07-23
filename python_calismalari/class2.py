class Insan:
    def __init__(self,i,m):
        self.isim = i
        self.meslek = m
    
    def yaptigi_is(self):
        if self.meslek == 'oyuncu':
            print(self.isim,"filim yapar, dizilerde oynar.")

        elif self.meslek == 'tenis oyuncusu':
            print(self.isim,"tenis oynar.")

    def konus(self):
        print(self.isim,"sana merhaba diyor.")


tom = Insan("tom cruise","oyuncu")
tom.yaptigi_is()
tom.konus()

maria = Insan("maria","tenis oyuncusu")
maria.yaptigi_is()
maria.konus()