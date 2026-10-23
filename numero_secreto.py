"""Jogo de adivinhação de números executado no terminal."""

import random

def gerar_numero_secreto(inicio=1, fim=100, modo_teste=False, numero_fixo=42):
    """Retorna um número secreto no intervalo configurado.

    O modo de teste utiliza um valor fixo para permitir execuções reproduzíveis.
    """
    if modo_teste:
        return numero_fixo
    else:
        return random.randint(inicio, fim)

def ler_palpite(inicio=1, fim=100):
    """Lê e valida um palpite inteiro dentro do intervalo informado."""
    while True:
        try:
            palpite = int(input(f'Digite um palpite entre {inicio} e {fim}: '))
            if inicio <= palpite <= fim:
                return palpite
            else:
                print(f'Palpite fora do intervalo! Tente novamente.')
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")
            
def mensagem_motivadora():
    """Seleciona uma mensagem de incentivo para a partida."""
    raise NotImplementedError("Mensagens motivadoras pendentes")


def jogar(inicio=1, fim=100, max_tentativas=7, modo_teste=False, numero_fixo=42):
    """Controla o fluxo da partida e o limite de tentativas."""
    print("Descubra o Número Secreto")
    
    gerar_numero = gerar_numero_secreto(inicio, fim, modo_teste, numero_fixo)
    tentativas = 0

    while tentativas < max_tentativas:
        palpite = ler_palpite(inicio, fim)
        tentativas += 1

        if palpite < gerar_numero:
            print("Tente um número maior!")
        elif palpite > gerar_numero:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou o número secreto {gerar_numero} em {tentativas} tentativas.")
            return

    print(f"Suas tentativas acabaram! O número secreto era {gerar_numero}.")


if __name__ == "__main__":
    jogar()
