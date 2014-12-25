from sys import argv

script, first, second, third = argv

def engin(a):
    return int(a)*2

def zari(b):
    return int(b)*3

def sefik(c):
    return c + " yildirim"



print "The script is called:", script
print "Engin'in yasinin iki kati:", engin(first)
print "Zaranin ayak numarasinin 3 kati:", zari(second)
print "Sefik'in tam adi:", sefik(third)

