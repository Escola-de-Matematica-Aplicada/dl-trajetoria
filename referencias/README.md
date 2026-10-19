# Referências da oficina de dados

Artigos e trabalhos citados no notebook `oficina_sim_temporal.ipynb`.

## Nesta pasta

| Arquivo | Onde entra no notebook |
|---|---|
| `datasus/IT_SIHSUS_1603.pdf` — DATASUS, layout da AIH reduzida (FTP `SIHSUS/200801_/Doc/`) | 1.3 — dicionário do SIH (TODO 1.1) |
| `microdatasus/processa_sih.py`, `microdatasus/processa_sim.py` — tradução para Python de `process_sih.R` e `process_sim.R` (SALDANHA, R., pacote microdatasus; licença MIT em `microdatasus/LICENSE.md`) | 1.3 — significado dos códigos (ex.: `CODIGOS["IDENT"]`) |
| `anonimizacao/TCC-Gerardo-Mikael.pdf` — PEREIRA, G. M. C. (TCC EMAp, 2025) | 3.6 — k-anonimato na publicação |
| `grafos/TCC - Yonathan Rabinovici Gherman.pdf` — GHERMAN, Y. R. (TCC EMAp, 2025) | 3.7 — grafo temporal com o ano como entidade |

Os `.md` ao lado de cada PDF são conversões automáticas (markitdown) para busca e leitura rápida; o PDF é a fonte.

## Na web

- DATASUS — FTP público: `ftp://ftp.datasus.gov.br/dissemin/publicos/` (`SIM/CID10/DORES`, `SIM/PRELIM/DORES`, `SIHSUS/200801_/dados`)
- SALDANHA, R. — microdatasus: [`process_sim.R`](https://github.com/rfsaldanha/microdatasus/blob/master/R/process_sim.R), [`process_sih.R`](https://github.com/rfsaldanha/microdatasus/blob/master/R/process_sih.R); livro [*sis*](https://rfsaldanha.github.io/sis/sim.html)
- DATASUS — [CID-10](http://www2.datasus.gov.br/cid10/V2008/cid10.htm)
- TypeSafe — [primitivas do System One](https://docs.typesafe.ai/primitives) (`choice`, `score`, `noul`) — 4.6
- Databricks — [função `ai_decide`](https://docs.databricks.com/aws/en/sql/language-manual/functions/ai_decide) e o [anúncio](https://www.databricks.com/blog/introducing-aidecide-make-fast-decisions-your-governed-data) — 4.7
