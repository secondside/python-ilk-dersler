from __future__ import division

secenek1 = "(1) toplama"
secenek2 = "(2) cikarma"
secenek3 = "(3) carpma"
secenek4 = "(4) bolme"

print secenek1
print secenek2
print secenek3
print secenek4

while True:
    soru = raw_input("Yapilacak islemin numarasini girin: ")

    if soru == "1":
        sayi1 = input("Toplama icin ilk sayiyi girin: ")
        print sayi1
        sayi2 = input("Toplama icin ikinci sayiyi girin: ")
        print sayi1, "+", sayi2, ":", sayi1 + sayi2

    if soru == "2":
        sayi3 = input("Cikarma icin ilk sayiyi girin: ")
        print sayi3
        sayi4 = input("Cikarma icin ikinci sayiyi girin: ")
        print sayi3, "-", sayi4, ":", sayi3 - sayi4

    if soru == "3":
        sayi5 = input("Carpma icin ilk sayiyi girin: ")
        print sayi5
        sayi6 = input("Carpma icin ikinci sayiyi girin: ")
        print sayi5, "x", sayi6, ":", sayi5 * sayi6

    if soru == "4":
        sayi7 = input("Bolme icin ilk sayiyi girin: ")
        print sayi7
        sayi8 = input("Bolme icin ikinci sayiyi girin: ")
        print sayi7, "/", sayi8, ":", sayi7 / sayi8
