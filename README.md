# Descubra o Número Secreto

Jogo de adivinhação executado no terminal, desenvolvido em Python com a biblioteca padrão.

**Status:** em desenvolvimento. A estrutura do projeto está disponível; as funcionalidades do jogo serão integradas de forma incremental.

## Funcionalidades previstas

- Geração de número secreto aleatório dentro de um intervalo definido.
- Modo determinístico para testes com um número fixo.
- Leitura e validação de palpites inteiros.
- Dicas indicando se o número secreto é maior ou menor que o palpite.
- Limite configurável de tentativas, com encerramento por vitória ou derrota.
- Mensagens de incentivo durante a partida.

As evoluções planejadas incluem escolha do intervalo, níveis de dificuldade, histórico de palpites e nova partida sem reiniciar o programa.

## Requisitos

- Python 3.13 ou superior.
- Git, para controle de versão.

Não são necessárias dependências externas.

## Execução

```bash
python numero_secreto.py
```

A versão atual inicializa o programa, mas ainda não contém a lógica completa da partida.

## Testes

```bash
python -m unittest discover -s tests -v
```

Os testes disponíveis nesta etapa verificam o carregamento do módulo e a definição das funções. Os testes funcionais serão adicionados conforme as funcionalidades forem implementadas.

## Estrutura do repositório

```text
numero-secreto-python/
├── numero_secreto.py
├── tests/
│   └── test_smoke.py
├── docs/
│   ├── REQUIREMENTS.md
│   ├── ROADMAP.md
│   └── DEVELOPMENT.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── workflows/ci.yml
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

## Documentação

- [Requisitos funcionais e critérios de aceitação](docs/REQUIREMENTS.md)
- [Planejamento das entregas](docs/ROADMAP.md)
- [Fluxo de desenvolvimento e versionamento](docs/DEVELOPMENT.md)
- [Diretrizes de contribuição](CONTRIBUTING.md)

## Qualidade

O repositório utiliza `unittest` para os testes automatizados e GitHub Actions para verificar alterações propostas em Pull Requests.
