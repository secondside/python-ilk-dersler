def tek():
    print "girdiginiz sayi bir tek sayidir"

def cift():
    print "girdiginiz sayi bir cift sayidir"

sayi = raw_input("lutfen bir sayi giriniz:")

if int(sayi) % 2 == 0:
    print cift()

else:
    print tek()
