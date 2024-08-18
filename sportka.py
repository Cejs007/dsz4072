import random


def _prijmout_cislo(cislo, vybrana_cisla, od=1, do=49):
    # výstup input přetypovat na číslo
    if cislo.isnumeric():
        cislo = int(cislo)
    else:
        print(f"{cislo} není číslo!")
        return False

    # test interval
    if not do >= cislo >= od:
        print(f"{cislo} není z intervalu {od}-{do}!")
        return False

    if cislo in vybrana_cisla:
        print(f"{cislo} už mám, zadej jiné!")
        return False
    else:
        return True


def vsad_sportku(pocet_cisel=6, od=1, do=49):
    vybrana_cisla = []
    print(f"Vyber si svých {pocet_cisel} šťastných čísel.")
    while len(vybrana_cisla) < pocet_cisel:

        cislo = input(f"Zadej číslo od {od}-{do} bez opakování:")

        zkontrolovano = _prijmout_cislo(cislo, vybrana_cisla, od=od, do=do)
        if zkontrolovano:
            vybrana_cisla.append(cislo)
    return vybrana_cisla


def losuj_sportku(pocet_cisel=6, od=1, do=49):
    '''
    Losování sportky -> vrací list {pocet_cisel} čísel
    {od}, {do} bez opakování.
    '''
    # do + 1 -> because range excludes the right value
    return random.sample(range(od, do + 1), pocet_cisel)
