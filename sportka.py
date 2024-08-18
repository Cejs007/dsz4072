import random


def vsad_sportku(pocet_cisel=6, od=1, do=49):

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


def losuj_sportku(pocet_cisel=6, od=1, do=49):
    '''
    Losování sportky -> vrací list {pocet_cisel} čísel
    {od}, {do} bez opakování.
    '''
    # do + 1 -> because range excludes the right value
    return random.sample(range(od, do + 1), pocet_cisel)
