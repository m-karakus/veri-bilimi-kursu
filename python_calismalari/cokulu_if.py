turkiye=["ankara","istanbul", "tokat"]
almanya=["berlin"]
ingiltere=["londra", "tokat"]

sehir=input("Lütfen Ülkesini bilmek istediğiniz Şehrin Adını Girin: ")
sehir=str(sehir)

if sehir in turkiye:
    print("Türkiye bir şehir")
if sehir in almanya:
    print("Almanya'da bir şehir")
elif sehir in ingiltere:
    print("Ingiltere'de bir şehir")
else:
    print("bu şehir nereye ait bilmiyorum")