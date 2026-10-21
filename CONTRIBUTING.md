# Como contribuir (inclusive trabalhando sozinho)

1. Escolha uma Issue com critérios de aceite claros.
2. Atualize `main` e crie uma branch (`feat/`, `fix/`, `test/`, `docs/`).
3. Faça mudanças pequenas e coesas; não resolva outras Issues na mesma PR.
4. Execute `python -m unittest discover -s tests -v` e teste a interface quando aplicável.
5. Use Conventional Commits (`tipo(escopo): descricao`).
6. Faça `git push` para sua branch e abra uma PR apontando para `main`.
7. Revise o diff e cheque a execução do CI antes de fazer merge.

**Nunca commite:** tokens, senhas, chaves privadas, arquivo `.env`, dumps pessoais ou ambientes virtuais.

Ao trabalhar sozinho, o review é uma auto-revisão guiada pelo template; não significa que houve aprovação independente de outra pessoa.