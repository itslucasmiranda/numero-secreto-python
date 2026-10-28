
# Descubra o Número Secreto

Jogo de adivinhação desenvolvido em Python e executado no terminal, utilizando apenas a biblioteca padrão.

O objetivo é descobrir um número secreto dentro de um intervalo, usando as dicas fornecidas a cada tentativa.

## Funcionalidades

- Geração aleatória de um número secreto.
- Modo determinístico para testes.
- Validação de palpites inteiros.
- Rejeição de entradas inválidas sem consumir tentativas.
- Dicas para tentar um número maior ou menor.
- Limite configurável de tentativas.
- Mensagens motivadoras após palpites incorretos.
- Encerramento por vitória ou derrota.

## Requisitos

- Python 3.13 ou superior.

Não são necessárias dependências externas.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/itslucasmiranda/numero-secreto-python.git
```

Entre na pasta:

```bash
cd numero-secreto-python
```

Inicie o jogo:

```bash
python numero_secreto.py
```

Por padrão, o jogo utiliza números entre 1 e 100 e oferece até 7 tentativas.

## Como jogar

1. Execute o programa no terminal.
2. Digite um número inteiro entre 1 e 100.
3. Utilize as dicas para ajustar seus próximos palpites.
4. Continue até descobrir o número secreto ou esgotar as tentativas.

Entradas inválidas não consomem tentativas.

## Testes automatizados

Execute a suíte completa:

```bash
python -m unittest discover -s tests -v
```

O projeto possui 19 testes automatizados, desenvolvidos com `unittest` e `unittest.mock`.

O GitHub Actions executa os testes automaticamente para validar as alterações do repositório.

## Estrutura do projeto

```text
numero-secreto-python/
├── numero_secreto.py
├── tests/
│   ├── test_geracao.py
│   ├── test_validacao.py
│   ├── test_jogo.py
│   ├── test_mensagens.py
│   └── test_smoke.py
├── docs/
│   ├── REQUIREMENTS.md
│   ├── ROADMAP.md
│   └── DEVELOPMENT.md
├── .github/
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
└── README.md
```

## Documentação

- [Requisitos funcionais](docs/REQUIREMENTS.md)
- [Roadmap](docs/ROADMAP.md)
- [Fluxo de desenvolvimento](docs/DEVELOPMENT.md)
- [Diretrizes de contribuição](CONTRIBUTING.md)
- [Histórico de alterações](CHANGELOG.md)

## Evoluções futuras

- Seleção de níveis de dificuldade.
- Configuração do intervalo pelo jogador.
- Histórico de palpites.
- Opção de iniciar uma nova partida.

## Licença

Este projeto ainda não possui uma licença definida.
