"""Jogo de adivinhação de números executado no terminal."""


def gerar_numero_secreto(inicio=1, fim=100, modo_teste=False, numero_fixo=42):
    """Retorna um número secreto no intervalo configurado.

    O modo de teste utiliza um valor fixo para permitir execuções reproduzíveis.
    """
    raise NotImplementedError("Geração do número secreto pendente")


def ler_palpite(inicio=1, fim=100):
    """Lê e valida um palpite inteiro dentro do intervalo informado."""
    raise NotImplementedError("Validação de palpites pendente")


def mensagem_motivadora():
    """Seleciona uma mensagem de incentivo para a partida."""
    raise NotImplementedError("Mensagens motivadoras pendentes")


def jogar(inicio=1, fim=100, max_tentativas=7, modo_teste=False, numero_fixo=42):
    """Controla o fluxo da partida e o limite de tentativas."""
    print("Descubra o Número Secreto")
    print("Funcionalidade em desenvolvimento.")


if __name__ == "__main__":
    jogar()
