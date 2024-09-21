from unittest import TestCase
from sportka import _prijmout_cislo, vsad_sportku, losuj_sportku


class Test(TestCase):
    def test_prijmout_cislo(self):
        # simulované vstupy od uživatele (inputy)
        test_inp = ["0", "100", "a", "5", "13"]
        # simulovaná už zvolená čísla
        test_vybrana_cisla = [1, 5]
        # pro každý simulovaný vsput provedu kontrolu a uložím
        zkontrolovano = []
        for inp in test_inp:
            zkontrolovano.append(_prijmout_cislo(inp, test_vybrana_cisla))
        # očekávaný výsledek
        expected = [False, False, False, False, True]
        self.assertEqual(zkontrolovano, expected)

    def test_losuj_sportku(self):
        losovani = losuj_sportku()
        delka = len(losovani)
        # dostanu zpět 6 čísel?
        self.assertEqual(delka, 6)
        delka_unikatni = len(set(losovani))
        # dostanu zpět 6 unikátních čísel?
        self.assertEqual(delka_unikatni, 6)
