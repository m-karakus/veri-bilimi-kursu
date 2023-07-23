import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sayi1", help="sayi1 değeri")
    parser.add_argument("--sayi2", help="sayi2")
    parser.add_argument("--operator", help="operator", choices=["toplama","çıkarma","çarpma"])
    args = parser.parse_args()

    sayi1 = int(args.sayi1)
    sayi2 = int(args.sayi2)
    opetator = str(args.operator)

    sonuc = None
    if opetator == "toplama":
        sonuc = sayi1 + sayi2
    elif opetator == "çıkarma":
        sonuc = sayi1 - sayi2
    elif opetator == "çarpma":
        sonuc = sayi1 * sayi2
    
    else:
        print("Işlem tanımlı değildir.")
    
    print("Sonuç:", sonuc)
