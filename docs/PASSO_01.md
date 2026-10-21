# Primeira tarefa real — geração do segredo

## Você vai implementar (não copiar uma solução pronta)

No arquivo `numero_secreto.py`, encontre a função `gerar_numero_secreto(...)`. Ela atualmente lança `NotImplementedError`. Nesta etapa, sua missão é **substituir apenas esse comportamento**.

### Entradas

- `inicio` e `fim`: intervalo de escolha (padrões 1 e 100).
- `modo_teste`: `False` para sorteio; `True` para segredo determinístico.
- `numero_fixo`: segredo no modo de teste (padrão 42).

### Critérios de aceite

- [ ] Ao chamar `gerar_numero_secreto(modo_teste=True)` recebo `42`.
- [ ] Ao chamar `gerar_numero_secreto(modo_teste=True, numero_fixo=17)` recebo `17`.
- [ ] Ao chamar `gerar_numero_secreto(1, 10)` recebo um inteiro dentro de `1..10` (inclusive).
- [ ] Ao chamar `gerar_numero_secreto(42, 42)` recebo `42`.
- [ ] O restante do arquivo continua funcionando como starter (não implementar as outras fases agora).

### Pistas — só o necessário

1. `import random` é disponibilizado pela biblioteca padrão.
2. `random.randint(inicio, fim)` inclui ambos os extremos.
3. Um `if modo_teste:` permite um `return` antes do sorteio.
4. `return` devolve o resultado à função que chamou.

### Teste manual inicial (rode no terminal Python)

```python
from numero_secreto import gerar_numero_secreto
assert gerar_numero_secreto(modo_teste=True) == 42
assert gerar_numero_secreto(modo_teste=True, numero_fixo=17) == 17
assert 1 <= gerar_numero_secreto(1, 10) <= 10
assert gerar_numero_secreto(42, 42) == 42
print("Etapa 1: verificacoes manuais passaram")
```

**Depois:** crie `tests/test_geracao.py` usando `unittest` para automatizar as verificações. Consulte o teste inicial `tests/test_smoke.py` como referência de estrutura.

### Fluxo Git para esta tarefa

Abra uma Issue `feat: implementar geração do número secreto` e crie a branch a partir de `main`:

```powershell
git switch main
git pull --ff-only origin main
git switch -c feat/numero-secreto
```

Implemente, execute os testes e depois:

```powershell
git status
git diff
git add numero_secreto.py tests/test_geracao.py
git diff --cached
git commit -m "feat(game): adiciona geracao de numero secreto"
git push -u origin feat/numero-secreto
```

No GitHub, clique em **Compare & pull request**, confira se a base é `main`, preencha o modelo e aguarde os checks antes do merge.

### O que trazer para revisão

Traga o conteúdo da sua função, o resultado dos testes e o link da PR (se já tiver). Vou revisar como se fosse uma code review: comportamento, nomes, clareza e possíveis bugs, sem pular a próxima fase.