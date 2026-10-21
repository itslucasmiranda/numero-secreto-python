# Guia Git/GitHub — fluxo utilizado neste repositório

## Primeira vez: clonar o repositório existente

Use o terminal PowerShell do VS Code:

    git clone https://github.com/itslucasmiranda/numero-secreto-python.git
    cd numero-secreto-python
    git status
    git branch -a

O repositório já existe no GitHub, então NÃO execute git init, gh repo create ou crie um segundo origin.
Se já extraiu o ZIP anterior em outra pasta, use este clone como diretório de trabalho para não criar históricos divergentes.

## Após aprovação da PR de estrutura

    git switch main
    git pull --ff-only origin main
    python numero_secreto.py
    python -m unittest discover -s tests -v

## Primeira feature

    git switch -c feat/numero-secreto
    git status
    # edite numero_secreto.py e crie testes/test_geracao.py
    git diff
    git add numero_secreto.py tests/test_geracao.py
    git diff --cached
    git commit -m "feat(game): implementa geracao de numero secreto"
    git push -u origin feat/numero-secreto

No site, abra uma PR com base main, descreva os testes e vincule a Issue.

## Depois do merge

    git switch main
    git pull --ff-only origin main
    git branch -d feat/numero-secreto

## Vocabulário
- git status: mostra suas mudanças locais.
- git add: seleciona alterações para o próximo commit.
- git commit: registra alterações localmente.
- git push: envia commits ao GitHub.
- git pull: traz commits remotos ao seu repositório local.
- branch: linha de desenvolvimento independente.
- PR: proposta de integração que pode ser revisada antes do merge.

## Conventional Commits
- feat: nova funcionalidade.
- fix: correção de bug.
- test: criação ou alteração de testes.
- docs: documentação.
- refactor: organização sem mudar o comportamento.
- chore: tarefas de manutenção e estrutura.
- ci: configuração de automação.

Não utilize mensagens vagas como update ou final. Nunca publique arquivos .env com segredos.

Referências:
- https://docs.github.com/en/get-started/using-git/about-git
- https://www.conventionalcommits.org/pt-br/v1.0.0/
