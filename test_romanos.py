import unittest

from romanos import RomanError, arabigo_a_romano, romano_a_arabigo

class RomanosFuncionesTest(unittest.TestCase):
    def test_arabigo_a_romano_sin_restas(self):
        self.assertEqual(arabigo_a_romano(36), "XXXVI")

    def test_arabigo_a_romano_con_restas(self):
        self.assertEqual(arabigo_a_romano(464), "CDLXIV")

    def test_arabigo_a_romano_solo_admite_enteros(self):
        with self.assertRaises(TypeError):
            arabigo_a_romano("loailo")

class RomanosFuncionesAromanoTest(unittest.TestCase):
    def test_romano_a_arabigo_tres_repeticiones_OK(self):
        self.assertEqual(romano_a_arabigo("III"), 3)

    def test_romano_a_arabigo_cuatro_repeticiones_ERROR(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo("IIII")
    def test_romano_a_arabigo_dos_repeticiones_de_VLD_error(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo("VV")
        with self.assertRaises(RomanError):
            romano_a_arabigo("LL")
        with self.assertRaises(RomanError):
            romano_a_arabigo("DD")
    
    def test_romano_a_arabigo_VLD_no_resta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo("VX")
        with self.assertRaises(RomanError):
            romano_a_arabigo("LC")
        with self.assertRaises(RomanError):
            romano_a_arabigo("DM")
    
    def test_romano_a_arabigo_tras_repeticion_no_se_resta(self):
        with self.assertRaises(RomanError):
            romano_a_arabigo("XXL")


"""
# print(arabigo_a_romano(36)) 
# print(arabigo_a_romano(46))
print(romano_a_arabigo("XXXIII"))
print(romano_a_arabigo("XLVII"))
print(romano_a_arabigo("LXIV"))
print(romano_a_arabigo("MCMXCII"))
print(valores_romanos)
print(valores_arabigos)
"""