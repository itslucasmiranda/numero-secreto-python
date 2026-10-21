# Roadmap de entregas

Fluxo: Issue → branch → código + testes → commits → push → Pull Request → revisão → merge.

## Definition of Done
- Alterações limitadas ao escopo da Issue.
- Testes executados localmente e no GitHub Actions.
- PR com descrição, critérios validados e vínculo à Issue.
- Main atualizada apenas após revisão e checks verdes.

## Etapa 0 — Estrutura inicial
- Branch: chore/estrutura-inicial.
- Objetivo: README, esqueleto de código, .gitignore, documentação, teste de estrutura e CI.
- Commit: chore: inicializa estrutura do projeto.
- Critério: imports e smoke test funcionam. O jogo permanece incompleto.

## Etapa 1 — Segredo aleatório / modo de teste
- Branch: feat/numero-secreto.
- Função: gerar_numero_secreto(inicio=1, fim=100, modo_teste=False, numero_fixo=42).
- Aceite: modo teste retorna 42 ou o fixo configurado; modo normal sorteia no intervalo inclusivo.
- Commit: feat(game): implementa geracao de numero secreto.

## Etapa 2 — Validação do palpite
- Branch: feat/validacao-palpite.
- Rejeitar texto, decimais e números fora do intervalo; pedir novamente sem quebrar.
- Commit: feat(input): valida palpites inteiros.

## Etapa 3 — Loop do jogo
- Branch: feat/loop-jogo.
- Usar while, dicas maior/menor, limite configurável de tentativas, vitória e derrota.
- Commit: feat(game): implementa loop de tentativas e dicas.

## Etapa 4 — Feedback motivador
- Branch: feat/mensagens.
- Escolher uma frase de uma lista e mostrá-la após um palpite incorreto.
- Commit: feat(ui): adiciona mensagens motivadoras.

## Etapa 5 — Casos de teste
- Branch: test/casos-jogo.
- Testar entradas inválidas, dicas, limite, vitória, derrota e modo fixo.
- Commit: test(game): cobre fluxos principais da partida.

## Etapa 6 — Entrega MVP
- Branch: docs/entrega-mvp.
- Atualizar README com jogo funcionando e instruções reais de execução.
- Publicar tag v1.0.0 após integração e testes verdes.

## Backlog extra (apenas depois do MVP)
- Escolher intervalo: feat/configurar-intervalo.
- Dificuldade fácil/média/difícil: feat/dificuldades.
- Histórico de palpites: feat/historico.
- Jogar novamente: feat/replay.

Faça uma Issue, uma branch e uma PR por melhoria.
