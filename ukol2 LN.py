t = 0.1
pes = input("Zadej uživatelské jméno : ")
if pes == "stavebnik":
    kocka = input("Zadej heslo : ")
    if kocka == "stavba":
        sd = float(input("Zadej délku stěny (metry) : "))
        vd = float(input("Zadej výšku stěny (metry) : "))
        vo = float(input("Zadej výšku okna (metry) : "))
        do = float(input("Zadej délku okna (metry) : "))
        so = sd*vd
        print(f"Plocha stěny včetně okna : {so}m^2 ")
        vv = vo*do
        print(f"Plocha okna : {vv}m^2 ")
        vsecko = so-vv
        print(f"Plocha stěny bez okna : {vsecko}m^2 ")
        pocet_tvarnic = vsecko/t
        print(f"Počet tvárnic potřebných k vyzdění plochy stěny : {pocet_tvarnic} ks")
        PP = 500
        PB = 300
        PO = 700
        print("Dostupnost materialu na pobočkách ČR")
        print("*************************************************************************")
        print(("{:<20}|{:<25}|{:<25}|".format("Město","Druh materialu","Počet kusů na pobočce")))
        print("*************************************************************************")
        if pocet_tvarnic<=PP:
            print(("{:<20}|{:<25}|{:<25}|".format("Praha","tvárnice", str(PP))))
        if pocet_tvarnic<=PB:
            print(("{:<20}|{:<25}|{:<25}|".format("Brno","tvárnice", str(PB))))
        if pocet_tvarnic<=PO:
            print(("{:<20}|{:<25}|{:<25}|".format("Ostrava","tvárnice", str(PO))))
        if pocet_tvarnic>PP and pocet_tvarnic>PB and pocet_tvarnic>PO:
            print("Není dostatek tvárnic na žádné pobočce")
    else:
        print("Nesprávné heslo")
else:
    print("Nesprávné uživatelské jméno")        