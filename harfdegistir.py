cumle = raw_input("lutfen cumlenizi giriniz:")
h1 = raw_input("degistirmek istediginiz harfi giriniz:")
h2 = raw_input("simdi yeni harfi giriniz:")

def harfdegistir(c, a1, a2):
    cumle2 = ""
    for i in c:
        if i == a1:
            i = a2
        cumle2 = cumle2 + i
    print cumle2

harfdegistir(cumle, h1, h2)

