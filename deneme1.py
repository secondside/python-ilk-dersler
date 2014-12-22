kapi = "kapali"
nerde = "disarda"

soru = raw_input("ne yapmak istiyorsunuz?")
while soru != "exit":
  if soru == "gir":
    if nerde == "disarda":
      if kapi == "acik":
        nerde = "iceride"
        print "hosgeldiniz"
      else:
        print "kapiyi aciniz"
    else:
      print "zaten icerdesin"
  if soru == "cik":
    if nerde == "iceride":
      if kapi == "acik":
        nerde = "disarida"
        print "gule gule"
      else:
        print "kapiyi aciniz"
    else:
      print "zaten disaridasin"

  if soru == "ac":
    if kapi == "kapali":
      kapi = "acik"
      print "kapi acildi"
    else:
      print "kapi zaten acik"
  if soru == "kapat":
    if kapi == "acik":
      kapi = "kapali"
      print "kapi kapandi"
    else:
      print "kapi zaten kapali"

  soru = raw_input("ne yapmak istiyorsunuz?")
