def f(n):
    return n*n

if __name__ == "__main__":
    array = [1,2,3,4,5]

    sonuc = []
    for n in array:
        sonuc.append(f(n))

    print(sonuc)