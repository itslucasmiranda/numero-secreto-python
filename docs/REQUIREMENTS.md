# Especificação de requisitos

## Visão geral

A aplicação executa um jogo de adivinhação de números inteiros no terminal. O sistema escolhe um número secreto e processa palpites até que o valor seja descoberto ou o limite de tentativas seja atingido.

## Requisitos funcionais

| ID | Requisito | Critério de aceitação |
|---|---|---|
| RF-01 | Geração do número secreto | Retornar um inteiro no intervalo inclusivo configurado; permitir valor fixo no modo de teste. |
| RF-02 | Entrada do jogador | Solicitar um número inteiro dentro do intervalo permitido. |
| RF-03 | Validação de entrada | Rejeitar texto e valores fora do intervalo sem encerrar o programa. |
| RF-04 | Contagem de tentativas | Incrementar a contagem apenas após receber um palpite válido e respeitar o limite configurado. |
| RF-05 | Pistas | Informar MAIOR se o palpite for inferior ao segredo e MENOR se for superior. |
| RF-06 | Encerramento | Encerrar com mensagem de vitória quando acertar; informar o segredo caso as tentativas terminem. |
| RF-07 | Mensagens de incentivo | Exibir mensagens motivadoras durante as tentativas incorretas. |

## Restrições técnicas

- Implementação em Python, usando apenas a biblioteca padrão.
- Execução via terminal.
- Organização em funções independentes, para facilitar testes e manutenção.
- Testes automatizados usando `unittest`.

## Evoluções previstas

- Escolha do intervalo pelo jogador.
- Seleção de dificuldade com diferentes limites de tentativas.
- Histórico de palpites.
- Opção de iniciar uma nova partida.

As melhorias previstas não fazem parte do escopo da primeira versão funcional.
