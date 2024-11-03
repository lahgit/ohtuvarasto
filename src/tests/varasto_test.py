import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alku_saldo_negatiivinen(self):
        varasto2 = Varasto(10, -5)
        self.assertAlmostEqual(varasto2.saldo, 0)
        

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

    def test_str(self):
        varasto10 = Varasto(10,5)
        expected_str = "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(varasto10), expected_str)

    def test_negative_creation(self):
        varasto9 = Varasto(10,20)
        self.assertEqual(varasto9.saldo, 10)

    def test_negative_add(self):
        varasto8 = Varasto(10,5)
        varasto8.lisaa_varastoon(-1)
        self.assertEqual(varasto8.saldo, 5)

    def test_overflow_add(self):
        varasto5 = Varasto(10,5)
        varasto5.lisaa_varastoon(20)
        self.assertEqual(varasto5.saldo, 10)

    def test_none_creation(self):
        varasto7 = Varasto(0,0)
        self.assertEqual(varasto7.tilavuus, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_negatiivinen_ottaminen(self):
        varasto5 = Varasto(10,5)
        varasto5.ota_varastosta(-1)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(varasto5.saldo, 5)


    def test_ottaminen(self):
        varasto3 = Varasto(10,5)
        varasto3.ota_varastosta(6)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(varasto3.saldo, 0)
