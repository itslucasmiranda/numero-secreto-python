import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from numero_secreto import jogar, mensagem_motivadora


class TestMensagens(unittest.TestCase):

    def test_retorna_mensagem_sorteada(self):
        with patch(
            "numero_secreto.random.choice",
            return_value="Você consegue!"
        ) as sorteio:
            resultado = mensagem_motivadora()

        self.assertEqual(resultado, "Você consegue!")
        sorteio.assert_called_once()

    def test_mensagem_apos_palpite_menor(self):
        saida = StringIO()

        with (
            patch("numero_secreto.gerar_numero_secreto", return_value=42),
            patch("numero_secreto.ler_palpite", side_effect=[20, 42]),
            patch(
                "numero_secreto.mensagem_motivadora",
                return_value="Continue tentando!"
            ) as mensagem,
            redirect_stdout(saida),
        ):
            jogar(max_tentativas=2)

        self.assertIn("Tente um número maior!", saida.getvalue())
        self.assertIn("Continue tentando!", saida.getvalue())
        mensagem.assert_called_once()

    def test_mensagem_apos_palpite_maior(self):
        saida = StringIO()

        with (
            patch("numero_secreto.gerar_numero_secreto", return_value=42),
            patch("numero_secreto.ler_palpite", side_effect=[70, 42]),
            patch(
                "numero_secreto.mensagem_motivadora",
                return_value="Não desista!"
            ) as mensagem,
            redirect_stdout(saida),
        ):
            jogar(max_tentativas=2)

        self.assertIn("Tente um número menor!", saida.getvalue())
        self.assertIn("Não desista!", saida.getvalue())
        mensagem.assert_called_once()

    def test_sem_mensagem_apos_acerto(self):
        saida = StringIO()

        with (
            patch("numero_secreto.gerar_numero_secreto", return_value=42),
            patch("numero_secreto.ler_palpite", return_value=42),
            patch("numero_secreto.mensagem_motivadora") as mensagem,
            redirect_stdout(saida),
        ):
            jogar(max_tentativas=1)

        self.assertIn("Parabéns!", saida.getvalue())
        mensagem.assert_not_called()