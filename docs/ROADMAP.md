# Roadmap

O desenvolvimento está organizado em entregas incrementais, associadas a Issues e Pull Requests.

| Fase | Entrega | Issue | Branch prevista |
|---|---|---|---|
| 0 | Estrutura do repositório e CI | PR #1 | `chore/estrutura-inicial` |
| 1 | Geração do número secreto | #2 | `feat/numero-secreto` |
| 2 | Validação de palpites | #3 | `feat/validacao-palpite` |
| 3 | Loop do jogo, dicas e encerramento | #4 | `feat/loop-jogo` |
| 4 | Mensagens motivadoras | #5 | `feat/mensagens` |
| 5 | Cobertura dos fluxos principais | #6 | `test/casos-jogo` |
| 6 | Documentação da primeira versão | #7 | `docs/entrega-mvp` |

## Critérios de conclusão

Uma entrega está apta à integração quando:

- Os critérios de aceitação da Issue foram atendidos.
- Os testes pertinentes foram implementados e passaram.
- A alteração foi documentada quando necessário.
- A Pull Request foi revisada e seus checks foram concluídos com sucesso.

## Versão inicial

A versão `v1.0.0` está prevista para o momento em que o jogo puder ser executado do início ao fim, com os requisitos funcionais principais implementados e validados.

## Backlog

Após a versão inicial:

- Configuração do intervalo.
- Níveis de dificuldade.
- Histórico de palpites.
- Reinício de partida sem fechar o programa.

As evoluções serão priorizadas em Issues independentes.
