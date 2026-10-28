import unittest
from unittest.mock import patch

from numero_secreto import ler_palpite


class TestValidacaoPalpite(unittest.TestCase):

    def test_palpite_valido(self):
        with patch("builtins.input", return_value="42"):
            resultado = ler_palpite()

        self.assertEqual(resultado, 42)

    def test_entradas_invalidas(self):
        entradas = ["abc", "150", "3.5", "42"]

        with patch("builtins.input", side_effect=entradas) as mock_input:
            resultado = ler_palpite()

        self.assertEqual(resultado, 42)
        self.assertEqual(mock_input.call_count, 4)

    def test_limites_do_intervalo(self):
        for valor in ("1", "100"):
            with self.subTest(valor=valor):
                with patch("builtins.input", return_value=valor):
                    resultado = ler_palpite()

                self.assertEqual(resultado, int(valor))

    def test_intervalo_personalizado(self):
        entradas = ["9", "21", "15"]
        with patch("builtins.input", side_effect=entradas) as entrada:
            resultado = ler_palpite(10, 20)

        self.assertEqual(resultado, 15)
        self.assertEqual(entrada.call_count, 3)