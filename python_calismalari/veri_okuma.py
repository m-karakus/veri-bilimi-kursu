file = "test.txt"


# w yeni dosya oluşturur - eski dosya varsa üzerine yazar
# r dosyadaki verileri okur - yazma yapmaz
# a dosyayı genişletir, yeni verileri ekler


satirlar=["1.satır","2.satır","3.satır","4.satır"]
with open(file,"wr") as f:
    print(f.read())