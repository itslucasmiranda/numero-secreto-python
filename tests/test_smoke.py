"""Verificações iniciais da interface pública do módulo."""

import unittest

import numero_secreto


class TestEstruturaDoProjeto(unittest.TestCase):
    def test_funcoes_publicas(self):
        nomes = (
            "gerar_numero_secreto",
            "ler_palpite",
            "mensagem_motivadora",
            "jogar",
        )
        for nome in nomes:
            with self.subTest(funcao=nome):
                self.assertTrue(callable(getattr(numero_secreto, nome)))


if __name__ == "__main__":
    unittest.main()
