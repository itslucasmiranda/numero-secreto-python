"""Testes da estrutura. Não testam ainda as regras do jogo."""

import unittest
import numero_secreto


class TestEstruturaDoProjeto(unittest.TestCase):
    def test_funcoes_publicas(self):
        for nome in ("gerar_numero_secreto", "ler_palpite", "mensagem_motivadora", "jogar"):
            with self.subTest(funcao=nome):
                self.assertTrue(callable(getattr(numero_secreto, nome)))


if __name__ == "__main__":
    unittest.main()
