class Arac:
    def genel_maksat(self):
        print("Genel maksatlı ulaşım aracı")

class Benzin:
    def yakit_turu(self):
        print("benzin")

class Mazot:
    def yakit_turu(self):
        print("Mazot")

class Otomobil(Arac,Mazot):
    def ozel_maksat(self):
        print("şehir içi ulaşım aracı")


    
class Motor(Arac,Benzin):
    def ozel_maksat(self):
        print("zevk için kullanım")

a3 = Otomobil()
a3.ozel_maksat() 
a3.genel_maksat()
a3.yakit_turu()

m = Motor()
m.ozel_maksat()
m.genel_maksat()
