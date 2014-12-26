alinanNot1 = int(input("1. Notunuzu giriniz:"))
alinanNot2 = int(input("2. Notunuzu giriniz:"))

if alinanNot1 < 0 or alinanNot2 < 0 or alinanNot1 > 100 or alinanNot2 > 100:
    print ("Gecersiz bir not degeri girdiniz!")
else:

    ortalama = (int(alinanNot1) + int(alinanNot2)) / 2
    if ortalama <= 100:
        karneNotu = 5
    if ortalama < 85:
        karneNotu = 4
    if ortalama < 70:
        karneNotu = 3
    if ortalama < 55:
        karneNotu = 2
    if ortalama < 45:
        karneNotu = 1

print "Ortalamaniz:", ortalama
print "Karne Notunuz:", karneNotu
