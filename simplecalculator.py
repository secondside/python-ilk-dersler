while True:
    secenek1 = "(1) toplama"
    secenek2 = "(2) cikarma"
    secenek3 = "(3) carpma"
    secenek4 = "(4) bolme"

    print secenek1
    print secenek2
    print secenek3
    print secenek4

    soru = raw_input("Lutfen yapmak istediginiz islemi secin: ")

    if soru == "1":
        sayi1 = input("Lutfen ilk sayiyi girin: ")
        sayi2 = input("Lutfen ikinci sayiyi girin: ")
        print sayi1, "+", sayi2,":", sayi1 + sayi2

    if soru == "2":
        sayi3 = input("Lutfen ilk sayiyi girin: ")
        sayi4 = input("Lutfen ikinci sayiyi girin: ")
        print sayi3, "-", sayi4,":", sayi3 - sayi4

    if soru == "3":
        sayi5 = input("Lutfen ilk sayiyi girin: ")
        sayi6 = input("Lutfen ikinci sayiyi girin: ")
        print sayi5, "x", sayi6,":", sayi5 * sayi6

    if soru == "4":
        sayi7 = input("Lutfen ilk sayiyi girin: ")
        sayi8 = input("Lutfen ikinci sayiyi girin: ")
        print sayi7, "/", sayi8,":", sayi7 / sayi8
