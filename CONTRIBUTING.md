# Diretrizes de contribuição

## Fluxo de trabalho

1. Associe a alteração a uma Issue com escopo e critérios de aceitação definidos.
2. Atualize a branch `main` e crie uma branch para a alteração.
3. Mantenha o código, os testes e a documentação pertinentes à mesma entrega.
4. Execute os testes localmente antes de publicar a branch.
5. Abra uma Pull Request apontando para `main`, vinculada à Issue.
6. Confira o diff e os resultados do CI antes de realizar o merge.

## Nomenclatura de branches

- `feat/<descricao>`: funcionalidade.
- `fix/<descricao>`: correção.
- `test/<descricao>`: testes.
- `docs/<descricao>`: documentação.
- `chore/<descricao>`: manutenção.

## Padrão de commits

O repositório utiliza [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/).

Exemplos:

```text
feat(game): implementa geracao de numero secreto
fix(input): corrige validacao de palpites
test(game): cobre limites do intervalo
docs: atualiza instrucoes de execucao
chore: configura ambiente do projeto
```

## Critérios para integração

- Alteração compatível com o escopo da Issue.
- Testes existentes passando, com novos testes quando aplicável.
- Descrição da PR contendo contexto, mudanças e validação.
- Ausência de credenciais, arquivos temporários e dados sensíveis.

Consulte [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) para os comandos de desenvolvimento.
