import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from numero_secreto import jogar


class TestJogo(unittest.TestCase):

    def test_vitoria_com_dicas(self):
        saida = StringIO()

        with (
            patch("numero_secreto.gerar_numero_secreto", return_value=42),
            patch("numero_secreto.ler_palpite", side_effect=[20, 70, 42]) as ler,
            redirect_stdout(saida),
        ):
            jogar(max_tentativas=3)

        texto = saida.getvalue()

        self.assertIn("Tente um número maior!", texto)
        self.assertIn("Tente um número menor!", texto)
        self.assertIn("Parabéns!", texto)
        self.assertEqual(ler.call_count, 3)
        self.assertNotIn("Suas tentativas acabaram!", texto)

    def test_derrota_apos_limite(self):
        saida = StringIO()

        with (
            patch("numero_secreto.gerar_numero_secreto", return_value=42),
            patch("numero_secreto.ler_palpite", side_effect=[10, 20, 30]) as ler,
            redirect_stdout(saida),
        ):
            jogar(max_tentativas=3)

        texto = saida.getvalue()

        self.assertIn("Suas tentativas acabaram!", texto)
        self.assertIn("O número secreto era 42", texto)
        self.assertEqual(ler.call_count, 3)
        self.assertNotIn("Parabéns!", texto)

    def test_vitoria_primeira_tentativa(self):
        saida = StringIO()

        with (
            patch("numero_secreto.gerar_numero_secreto", return_value=42),
            patch("numero_secreto.ler_palpite", return_value=42) as ler,
            redirect_stdout(saida),
        ):
            jogar(max_tentativas=7)

        self.assertIn("Parabéns!", saida.getvalue())
        self.assertEqual(ler.call_count, 1)

    def test_entrada_invalida_nao_gasta_tentativa(self):
        saida = StringIO()

        with (
            patch("numero_secreto.gerar_numero_secreto", return_value=42),
            patch("builtins.input", side_effect=["abc", "150", "42"]) as entrada,
            redirect_stdout(saida),
        ):
            jogar(max_tentativas=1)

        self.assertEqual(entrada.call_count, 3)
        self.assertIn("Parabéns!", saida.getvalue())
        self.assertNotIn("Suas tentativas acabaram!", saida.getvalue())