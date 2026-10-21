# 🎯 Descubra o Número Secreto

> Projeto final do módulo de fundamentos de Python. Repositório de **aprendizado orientado a etapas**, usando Git, GitHub, Issues, branches, Pull Requests, testes e integração contínua.

**Status:** 🚧 Etapa 0 — estrutura inicial preparada; jogo propositalmente incompleto.

## Objetivo

Criar um jogo de terminal que sorteia um número entre limites configuráveis e permite que a pessoa tente adivinhá-lo, recebendo dicas sobre tentar um número maior ou menor. O jogo deve tratar entradas inválidas sem encerrar, contar tentativas válidas, informar vitória ou derrota e exibir mensagens motivadoras.

### Requisitos do desafio original

- [ ] Gerar número secreto com `random` e permitir segredo fixo para testes.
- [ ] Ler um palpite inteiro dentro do intervalo, repetindo a pergunta quando inválido.
- [ ] Controlar um número máximo de tentativas (padrão: 7).
- [ ] Exibir pistas **MAIOR/MENOR** corretas.
- [ ] Encerrar ao acertar; avisar quando acabarem as tentativas.
- [ ] Mostrar mensagens motivadoras.
- [ ] Organizar o código em funções (`gerar_numero_secreto`, `ler_palpite`, `mensagem_motivadora`, `jogar`).

**Extras propostos no PDF, somente após o MVP:** escolha de intervalo, níveis de dificuldade, histórico de palpites e replay sem reiniciar o programa.

## Comece aqui

1. Leia [`docs/ETAPAS.md`](docs/ETAPAS.md) para conhecer as entregas e critérios.
2. Leia [`docs/COMANDOS_GIT.md`](docs/COMANDOS_GIT.md) para configurar Git/GitHub no Windows.
3. Execute `python numero_secreto.py` para conferir o ponto de partida.
4. Execute `python -m unittest discover -s tests -v` para rodar o teste de infraestrutura.
5. Siga [`docs/PASSO_01.md`](docs/PASSO_01.md) e implemente a primeira função.

> O teste inicial verifica **somente** que o módulo e suas funções existem. Não comprova as regras do jogo. Os testes de comportamento serão escritos conforme as entregas evoluírem.

## Estrutura

```text
numero-secreto-python/
├── numero_secreto.py            # Desafio (funções ainda não implementadas)
├── tests/
│   └── test_smoke.py            # Somente teste inicial da estrutura
├── docs/
│   ├── ETAPAS.md                 # Roadmap e critérios de aceite
│   ├── PASSO_01.md              # Primeira tarefa para programar
│   ├── COMANDOS_GIT.md          # Guia prático Git/GitHub
│   ├── FLUXO_OBSIDIAN.md        # Nota Markdown com Mermaid e flashcards
│   └── REQUISITOS.md            # Origem no PDF x práticas adicionais
├── .github/
│   ├── workflows/ci.yml         # Testes automáticos em push e PR
│   ├── ISSUE_TEMPLATE/          # Modelos de tarefa/bug
│   └── pull_request_template.md # Checklist de revisão
├── .gitignore
└── .editorconfig
```

## Tecnologia e comandos

- Python 3.13 (biblioteca padrão; **sem dependências externas**).
- Git e GitHub; GitHub CLI (`gh`) opcional.

```powershell
python numero_secreto.py
python -m unittest discover -s tests -v
```

## Processo de entrega

`Issue → branch → desenvolvimento → testes → commits pequenos → push → PR → review → merge → main`

Não programe todas as funções antes da primeira PR: a intenção deste repositório é **registrar as etapas reais da construção**.

## Origem

Material didático fornecido pelo estudante: `m10_a55.pdf`, projeto **“Descubra o Número Secreto”**. Este repositório adiciona processo de engenharia de software para aprendizado; o documento original não exige GitHub, CI ou Pull Requests.