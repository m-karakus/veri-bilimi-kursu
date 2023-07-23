import json
from pprint import pprint

veri={}
veri["ayşe"] = {
    "ad":"ayşe",
    "soyad":"ateş",
    "yaş":42,
    "email":"ayse12@gmail.com"
    }

veri["fatma"]= {
    "ad": "fatma",
    "soyad":"şahin",
    "yaş":27,
    "email":"fatma444@gmail.com",
    "adres":"istanbul/bağcılar"
}

d = json.dumps(veri)
with open("veri.json","w") as f:
    f.write(d)



with open("veri.json","r") as f:
    t = f.read()


pprint(json.loads(t))