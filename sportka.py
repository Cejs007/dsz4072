def vsad_sportku(pocet_cisel=6, od=1, do=49):
    '''
    Vsazení sportky uživatelem -> vrací list {pocet_cisel} čísel
    {od}, {do} bez opakování.
    '''
    vybrana_cisla = []
    print(f"Vyber si svých {pocet_cisel} šťastných čísel.")
    while len(vybrana_cisla) < pocet_cisel:

        cislo = input(f"Zadej číslo od {od}-{do} bez opakování:")

        # výstup input přetypovat na číslo
        if cislo.isnumeric():
            cislo = int(cislo)
        else:
            print(f"{cislo} není číslo!")
            continue

        # test interval
        if not do >= cislo >= od:
            print(f"{cislo} není z intervalu {od}-{do}!")
            continue

        if cislo in vybrana_cisla:
            print(f"{cislo} už mám, zadej jiné!")
        else:
            vybrana_cisla.append(cislo)
    return vybrana_cisla
