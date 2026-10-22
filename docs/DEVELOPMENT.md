# Desenvolvimento e versionamento

## Preparação do ambiente

```powershell
git clone https://github.com/itslucasmiranda/numero-secreto-python.git
cd numero-secreto-python
python --version
```

O projeto utiliza a biblioteca padrão de Python; não há instalação de dependências externas.

## Fluxo de implementação

Atualizar a branch principal antes de iniciar uma alteração:

```powershell
git switch main
git pull --ff-only origin main
```

Criar uma branch relacionada à Issue:

```powershell
git switch -c feat/numero-secreto
```

Após implementar e validar a alteração:

```powershell
python -m unittest discover -s tests -v
git status
git diff
git add numero_secreto.py tests/test_geracao.py
git diff --cached
git commit -m "feat(game): implementa geracao de numero secreto"
git push -u origin feat/numero-secreto
```

O arquivo `tests/test_geracao.py` será incluído com a implementação da geração do segredo.

Abrir uma Pull Request para `main`, relacionando a Issue correspondente e registrando as verificações realizadas. A integração deve ocorrer após revisão das alterações e aprovação dos checks configurados.

## Após a integração

```powershell
git switch main
git pull --ff-only origin main
git branch -d feat/numero-secreto
```

## Comandos de referência

| Comando | Descrição |
|---|---|
| `git status` | Consulta o estado do diretório de trabalho. |
| `git diff` | Mostra alterações não adicionadas à área de preparação. |
| `git add` | Inclui alterações no próximo commit. |
| `git diff --cached` | Mostra o conteúdo preparado para o commit. |
| `git commit` | Registra uma versão no histórico local. |
| `git push` | Publica commits no repositório remoto. |
| `git fetch` | Atualiza referências remotas sem integrar o conteúdo. |
| `git pull` | Busca e integra mudanças da branch remota. |

## Integração contínua

O workflow em `.github/workflows/ci.yml` valida a sintaxe dos arquivos Python e executa a suíte de testes com `unittest`. Ele não substitui testes funcionais que ainda não tenham sido implementados.
