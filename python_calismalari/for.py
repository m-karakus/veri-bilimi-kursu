faturalar=[2800,6300,4300,5124,8800,10000,9257]

toplam_giderler=0

for i in range(len(faturalar)):
    print(i+1,"inci Ay Harcama:", faturalar[i])
    toplam_giderler = toplam_giderler + faturalar[i]

print("Toplam Giderler:",toplam_giderler)
