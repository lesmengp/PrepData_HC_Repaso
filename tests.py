import unittest
import os
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    
    def test_DividirDosNumeros_01(self):
      parte_entera, resto = ch.DividirDosNumeros(10, 5)
      lista_test = [parte_entera, resto]
      lista_esperada = [2,0]
      self.assertEqual(lista_test, lista_esperada)

    def test_DividirDosNumeros_02(self):
      parte_entera, resto = ch.DividirDosNumeros(17, 3)
      lista_test = [parte_entera, resto]
      lista_esperada = [5,2]
      self.assertEqual(lista_test, lista_esperada)

    def test_DividirDosNumeros_03(self):
      parte_entera, resto = ch.DividirDosNumeros(13, 3)
      lista_test = [parte_entera, resto]
      lista_esperada = [4,1]
      self.assertEqual(lista_test, lista_esperada)

    def test_ProximoPrimo_01(self):
      valor_test = ch.ProximoPrimo(5)
      valor_esperado = 7
      self.assertEqual(valor_test, valor_esperado)
      
    def test_ProximoPrimo_02(self):
      valor_test = ch.ProximoPrimo(61)
      valor_esperado = 67
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_03(self):
      valor_test = ch.ProximoPrimo(139)
      valor_esperado = 149
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_04(self):
      valor_test = ch.ProximoPrimo(200)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_01(self):
      a = ch.ClaseAnimal('perro','negro')
      valor_test = a.CumplirAnios()
      valor_test = a.CumplirAnios()
      valor_test = a.CumplirAnios()
      valor_esperado = 3
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_02(self):
      a = ch.ClaseAnimal('ballena','azul')
      for i in range(0,10):
        valor_test = a.CumplirAnios()
      valor_esperado = 10
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseAnimal_03(self):
      a = ch.ClaseAnimal('tortuga','verde')
      for i in range(0,100):
        valor_test = a.CumplirAnios()
      valor_esperado = 100
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores


archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Tipo,Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write('Credit,'+str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))