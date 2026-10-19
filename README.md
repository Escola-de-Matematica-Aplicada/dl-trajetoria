# dl-trajetoria — Oficina de dados (Data Lake) · Modelagem Informacional 2026.2

**FGV EMAp · Prof. Júlio César Chaves** · Atividade **individual** · Ambiente: **Databricks Free Edition**

## Desafio

> Descobrir, **desde a data mais antiga até a mais recente**, qual a **doença que mais mata** e qual a **doença que mais causa internação hospitalar**, **ao longo dos anos**, em **cada estado brasileiro**.

Fontes: microdados do **SIM** (mortalidade, 1996 →) e do **SIH/SUS** (internações, 2008 →), do DATASUS, com a **CID-10** como dicionário de doenças.

Você vai percorrer a jornada básica de engenharia de dados:

| # | Etapa | Saída |
|---|---|---|
| 1 | **Find & Understand** | dicionário de dados + decisões de modelagem |
| 2 | **Provision** | arquivos `.dbc` no Volume + tabelas `bronze_*` |
| 3 | **Prep** | `silver_*`, `dim_cid`, `gold_fato_causa`, `gold_lideres` |
| 4 | **Analyze** | doença líder por UF × ano, mapas, leitura temporal, robustez |

O notebook entrega cerca de **70% do caminho pronto**. As células marcadas com **🧩 SUA VEZ** são os outros 30%: é com elas que você trabalha.

## Conteúdo

| Caminho | O que é |
|---|---|
| `notebooks/oficina_sim_temporal.ipynb` | o roteiro-guia: rode e complete no Databricks |
| `scripts/baixar_datasus.py` | Plano B: baixa os arquivos fora do Databricks, se o FTP do DATASUS falhar |

## Como começar no Databricks Free Edition

1. Crie sua conta em <https://www.databricks.com/learn/free-edition>.
2. **Workspace → Create → Git folder** e cole a URL deste repositório. (Se preferir: baixe `notebooks/oficina_sim_temporal.ipynb` e use **Workspace → Import → File**.)
3. Abra `notebooks/oficina_sim_temporal.ipynb` e conecte ao compute **Serverless**.
4. Rode as células de cima para baixo, primeiro com `MODO = "rapido"` (3 UFs, poucos anos, alguns minutos).
5. Quando tudo funcionar, mude para `MODO = "completo"` e rode de novo. Só o que falta é baixado.

> **Cota do Free Edition.** O modo `completo` baixa ~2,5 GB do SIM e ~5 GB do SIH. Rode-o **uma vez**, depois de validar tudo no `rapido`.

## Plano B: o FTP do DATASUS falhou

O serverless do Free Edition acessa o FTP do DATASUS, e o notebook baixa tudo direto de lá. O FTP do DATASUS, porém, às vezes fica lento ou fora do ar. Se a seção 2 do notebook mostrar falhas de download mesmo depois de tentar de novo:

```bash
python3 scripts/baixar_datasus.py --modo rapido        # ou --modo completo
```

Isso cria a pasta `volume/` com a mesma estrutura do Volume do notebook (`dbc/sim`, `dbc/sih`, `dbc/sim_prelim`, `cid`). Envie-a para o Volume:

- pela interface: **Catalog → workspace → oficina_sus → Volumes → bronze_raw → Upload to this volume**, mantendo as subpastas; ou
- pela CLI do Databricks: `databricks fs cp -r volume/ dbfs:/Volumes/workspace/oficina_sus/bronze_raw/`

Depois rode a seção 2 do notebook de novo: os arquivos já presentes não são baixados outra vez.

O script usa só a biblioteca padrão do Python 3.

## Jev (opcional, seção 4.6)

A seção 4.6 usa o Jev (TypeSafe System One) para criar um novo atributo na `dim_cid`. A chave da API **nunca** vai numa célula: guarde-a num *secret scope*. Os comandos abaixo são da **CLI do Databricks** (versão 0.205 ou mais nova) e rodam num **terminal** (Codespaces ou seu computador), não no notebook:

```bash
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh   # instala a CLI
databricks auth login --host https://<seu-workspace>.cloud.databricks.com              # login pelo navegador
databricks secrets create-scope typesafe
databricks secrets put-secret typesafe api_key        # pede a chave (de https://console.typesafe.ai/)
databricks secrets list-secrets typesafe              # confere: deve listar api_key
```

O passo a passo completo, com Windows e macOS, está no início da seção 4.6 do notebook. Sem a chave, a 4.6 é pulada com um aviso.

## Entrega (D2L)

Exporte o notebook executado no modo `completo` (**File → Export → IPython Notebook**) e entregue com o texto de até 1 página descrito na seção 5 do notebook.

## Referências

- DATASUS — FTP público: `ftp://ftp.datasus.gov.br/dissemin/publicos/` (`SIM/CID10/DORES`, `SIM/PRELIM/DORES`, `SIHSUS/200801_/dados`)
- SALDANHA, R. — microdatasus: [`process_sim.R`](https://github.com/rfsaldanha/microdatasus/blob/master/R/process_sim.R), [`process_sih.R`](https://github.com/rfsaldanha/microdatasus/blob/master/R/process_sih.R); livro [*sis*](https://rfsaldanha.github.io/sis/sim.html)
- DATASUS — [CID-10](http://www2.datasus.gov.br/cid10/V2008/cid10.htm)
- Artigos e trabalhos citados (TCCs EMAp) e links do Jev e do `ai_decide`: pasta [`referencias/`](referencias/README.md)
