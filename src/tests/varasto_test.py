import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_virheellinen_tilavuus_nollataan(self):
        neg_tilavuus = Varasto(-5)

        self.assertAlmostEqual(neg_tilavuus.tilavuus, -5)

    def test_virheellinen_alkusaldo_nollataan(self):
        neg_alkusaldo = Varasto(5, -5)

        self.assertAlmostEqual(neg_alkusaldo.saldo, 0)

    def test_alkusaldo_ei_ylita_tilavuutta(self):
        iso_alkusaldo = Varasto(5, 10)

        self.assertAlmostEqual(iso_alkusaldo.saldo, 5)

    def test_negatiivinen_lisays_ei_sallittu(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_iso_lisays_tayttaa_tilavuuden(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_negatiivinen_otto_nollataan(self):
        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(self.varasto.ota_varastosta(-5), 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_iso_otto_tyhjentaa_saldon(self):
        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(self.varasto.ota_varastosta(7), 5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_tulostus_toimii(self):
        self.varasto.lisaa_varastoon(7)

        self.assertAlmostEqual(str(self.varasto), "saldo = 7, vielä tilaa 3")
