
def tek():
    return "girdiginiz sayi bir tek sayidir"

def cift():
    return "girdiginiz sayi bir cift sayidir"
sayi = int(raw_input("lutfen bir sayi giriniz:"))

if sayi % 2 == 0:
    print cift()
else:
    print tek()
