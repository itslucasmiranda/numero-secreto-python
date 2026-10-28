import unittest
from unittest.mock import patch
from numero_secreto import gerar_numero_secreto


class TestGeracaoNumeroSecreto(unittest.TestCase):

    def test_modo_teste_padrao(self):
        resultado = gerar_numero_secreto(modo_teste=True)
        self.assertEqual(resultado, 42)

    def test_modo_teste_personalizado(self):
        resultado = gerar_numero_secreto(
            modo_teste=True,
            numero_fixo=17
        )
        self.assertEqual(resultado, 17)

    def test_numero_dentro_intervalo(self):
        resultado = gerar_numero_secreto(1, 10)
        self.assertIsInstance(resultado, int)
        self.assertGreaterEqual(resultado, 1)
        self.assertLessEqual(resultado, 10)

    def test_intervalo_unico(self):
        resultado = gerar_numero_secreto(42, 42)
        self.assertEqual(resultado, 42)

    def test_sorteio_intervalo_personalizado(self):
        with patch("numero_secreto.random.randint", return_value=15) as sorteio:
            resultado = gerar_numero_secreto(10, 20)

        self.assertEqual(resultado, 15)
        self.assertTrue(sorteio.called)
        sorteio.assert_called_once_with(10, 20)