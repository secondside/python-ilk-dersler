from sys import argv

script, filename = argv

print "simdi %r isimli dosyayi silecegiz." %filename
print "islemi iptal etmek icin CTRL-C'ye basiniz"
print "isleme devam etmek icin RETURN yaziniz"

raw_input("? ")

print "dosya aciliyor..."
target = open(filename, 'w')

print "dosya silindi. elveda!"
target.truncate()

print "simdi sizden uc satir yazmanizi istiyorum"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "simdi bu satirlari dosyaya yazacagim"

target.write(line1, "\n", line2, "\n", line3)

print "ve artik kapatiyoruz"
target.close()
