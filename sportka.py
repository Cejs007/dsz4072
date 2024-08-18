import random
from datetime import datetime


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
            vybrana_cisla.append(int(cislo))
    return vybrana_cisla


def losuj_sportku(pocet_cisel=6, od=1, do=49):
    """
    Losování sportky -> vrací list {pocet_cisel} čísel
    {od}, {do} bez opakování.
    """
    # do + 1 -> because range excludes the right value
    return random.sample(range(od, do + 1), pocet_cisel)


def dokud_nevyhraju(stastna_cisla,
                    cena_radku=20,
                    max_radky_losovani=10,
                    pocet_losovani_tydne=3,
                    vypis_n_losovani=1000000):
    """
    Losuje sportku tak dlouho, dokud šťastná čísla nevyhrají
    jackpot.
    Vrací počet losování, počet let do výhry a cenu podání.
    Losuje se 3xtýdně, kdy je možné vsadit 10 sloupců naráz.
    """
    stastna = sorted(stastna_cisla)
    i = 0
    start = datetime.now()
    while True:
        losovano = sorted(losuj_sportku())
        if stastna == losovano:
            break
        i += 1
        if i % vypis_n_losovani == 0:
            print(i)
    vypocet_trvani = datetime.now() - start
    # 52 týdnů v roce
    let_do_vyhry = i / max_radky_losovani / pocet_losovani_tydne / 52
    cena_sazenek = i * cena_radku
    return vypocet_trvani.seconds, let_do_vyhry, cena_sazenek
