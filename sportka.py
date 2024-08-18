def vsad_sportku():
    vybrana_cisla = []
    while len(vybrana_cisla) < 6:
        cislo = input("Zadej číslo od 1-49 bez opakování:")
        # výstup input přetypovat na číslo
        if cislo.isnumeric():
            cislo = int(cislo)
        else:
            print("Prosím příště zadej číslo!")
            continue

        # test interval
        if not 49 >= cislo >= 1:
            print("Špatný interval")
            continue

        if cislo in vybrana_cisla:
            print(f"{cislo} už mám, zadej jiné!")
        else:
            vybrana_cisla.append(cislo)
    return vybrana_cisla

