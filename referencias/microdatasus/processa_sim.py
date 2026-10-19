"""Dicionário e decodificação do SIM (DATASUS) em Python.

Tradução para Python de `process_sim.R`, do pacote R **microdatasus**
(SALDANHA, R. F.; https://github.com/rfsaldanha/microdatasus/blob/master/R/process_sim.R).
Gerada automaticamente a partir do código R; a lógica e os rótulos são os do original.
Licença MIT do original: Copyright (c) 2021 microdatasus authors (ver LICENSE.md nesta pasta).

Como usar na oficina:
- **Para ler** (TODO 1.1): procure a coluna em `CODIGOS`; cada entrada mostra o que cada código significa.
  Colunas que o microdatasus não recodifica (ex.: os diagnósticos CID-10) não aparecem aqui:
  veja o layout oficial do DATASUS em `referencias/datasus/`.
- **Para rodar** (opcional): `processar(df)` recebe um `pandas.DataFrame` com as colunas como texto
  (como sai de `ler_dbf` no notebook) e devolve uma cópia decodificada, como `process_sim()` no R.

    import sys; sys.path.append("../referencias/microdatasus")
    from processa_sim import CODIGOS, processar
    CODIGOS["CIRCOBITO"]
    processar(amostra_pandas)
"""
import pandas as pd

# Códigos de cada coluna: código no arquivo -> rótulo (None = ignorado/ausente).
# A ordem é a do arquivo R.
CODIGOS = {
    'CODINST': {
        'E': 'Estadual',
        'R': 'Regional',
        'M': 'Municipal',
    },
    'TIPOBITO': {
        '0': None,
        '9': None,
        '1': 'Fetal',
        '2': 'Não Fetal',
    },
    'SEXO': {
        '0': None,
        '9': None,
        '1': 'Masculino',
        '2': 'Feminino',
    },
    'RACACOR': {
        '0': None,
        '1': 'Branca',
        '2': 'Preta',
        '3': 'Amarela',
        '4': 'Parda',
        '5': 'Indígena',
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'ESTCIV': {
        '0': None,
        '1': 'Solteiro',
        '2': 'Casado',
        '3': 'Viúvo',
        '4': 'Separado judicialmente',
        '5': 'União consensual',
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'ESC': {
        '0': None,
        '6': None,
        '7': None,
        '9': None,
        'A': None,
        '1': 'Nenhuma',
        '2': '1 a 3 anos',
        '3': '4 a 7 anos',
        '4': '8 a 11 anos',
        '5': '12 anos ou mais',
        '8': '9 a 11 anos',
    },
    'LOCOCOR': {
        '1': 'Hospital',
        '2': 'Outro estabelecimento de saúde',
        '3': 'Domicílio',
        '4': 'Via pública',
        '5': 'Outros',
        '9': None,
    },
    'IDADEMAE': {
        '0': None,
    },
    'ESCMAE': {
        '0': None,
        '6': None,
        '7': None,
        '9': None,
        'A': None,
        '1': 'Nenhuma',
        '2': '1 a 3 anos',
        '3': '4 a 7 anos',
        '4': '8 a 11 anos',
        '5': '12 anos ou mais',
        '8': '9 a 11 anos',
    },
    'GRAVIDEZ': {
        '1': 'única',
        '2': 'Dupla',
        '3': 'Tríplice e mais',
        '9': None,
    },
    'GESTACAO': {
        '0': None,
        'A': '21 a 27 semanas',
        '1': 'Menos de 22 semanas',
        '2': '22 a 27 semanas',
        '3': '28 a 31 semanas',
        '4': '32 a 36 semanas',
        '5': '37 a 41 semanas',
        '6': '42 semanas e mais',
        '7': '28 semanas e mais',
        '8': '28 a 36 semanas',
        '9': None,
    },
    'PARTO': {
        '0': None,
        '1': 'Vaginal',
        '2': 'Cesáreo',
        '3': None,
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'OBITOPARTO': {
        '0': None,
        '1': 'Antes',
        '2': 'Durante',
        '3': 'Depois',
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'OBITOGRAV': {
        '1': 'Sim',
        '2': 'Não',
        '3': None,
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'OBITOPUERP': {
        '1': 'De 0 a 42 dias',
        '2': 'De 43 dias a 1 ano',
        '3': 'Não',
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'ASSISTMED': {
        '1': 'Sim',
        '2': 'Não',
        '9': None,
    },
    'EXAME': {
        '1': 'Sim',
        '2': 'Não',
        '9': None,
    },
    'CIRURGIA': {
        '1': 'Sim',
        '2': 'Não',
        '9': None,
    },
    'NECROPSIA': {
        '1': 'Sim',
        '2': 'Não',
        '9': None,
    },
    'CIRCOBITO': {
        '0': None,
        '1': 'Acidente',
        '2': 'Suicídio',
        '3': 'Homicídio',
        '4': 'Outro',
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'ACIDTRAB': {
        '1': 'Sim',
        '2': 'Não',
        '9': None,
    },
    'FONTE': {
        '1': 'Boletim de Ocorrência',
        '2': 'Hospital',
        '3': 'Família',
        '4': 'Outro',
        '9': None,
    },
    'TPPOS': {
        'N': 'Não investigado',
        'S': 'Investigado',
    },
    'ATESTANTE': {
        '0': None,
        '1': 'Sim',
        '2': 'Substituto',
        '3': 'IML',
        '4': 'SVO',
        '5': 'Outro',
        '6': None,
        '7': None,
        '8': None,
        '9': None,
    },
    'FONTEINV': {
        '1': 'Comitê de Mortalidade Materna e/ou Infantil',
        '2': 'Visita familiar / Entrevista família',
        '3': 'Estabelecimento de saúde / Prontuário',
        '4': 'Relacionamento com outros bancos de dados',
        '5': 'SVO',
        '6': 'IML',
        '7': 'Outra fonte',
        '8': 'Múltiplas fontes',
        '9': None,
    },
}

# Colunas convertidas para número.
NUMEROS = ['IDADEMAE', 'QTDFILVIVO', 'QTDFILMORT', 'PESO']

# Colunas de data e seu formato no arquivo.
DATAS = {'DTOBITO': '%d%m%Y', 'DTNASC': '%d%m%Y', 'DTATESTADO': '%d%m%Y', 'DTINVESTIG': '%d%m%Y', 'DTCADASTRO': '%d%m%Y', 'DTRECEBIM': '%d%m%Y', 'DTRECORIGA': '%d%m%Y'}

# Colunas cortadas nos primeiros N caracteres (município IBGE com 6 dígitos).
TRUNCAR = {'CODMUNRES': 6, 'CODMUNOCOR': 6}

# Colunas em que um código fora de CODIGOS vira None (nas demais, o código é mantido).
SEM_DEFAULT = []

# Colunas decodificadas por tabelas auxiliares do pacote R (municípios, CBO, naturalidade),
# que não estão aqui; ver `tabelas` em processar().
TABELAS_EXTERNAS = {'NATURAL': 'tabNaturalidade', 'OCUP': 'tabCBO', 'CODMUNRES': 'tabMun', 'OCUPMAE': 'tabCBO'}


def decodificar_idade(idade):
    """IDADE do SIM: 1º dígito = unidade, 2 últimos = valor (bloco `# IDADE` do R).

    0 = minutos, 1 = horas, 2 = dias, 3 = meses, 4 = anos, 5 = 100 + anos. "000" e "999" = ignorado.
    Devolve as colunas IDADEminutos, IDADEhoras, IDADEdias, IDADEmeses, IDADEanos.
    """
    idade = idade.where(~idade.isin(["000", "999"]))
    unidade = idade.str[:1]
    valor = pd.to_numeric(idade.str[1:3], errors="coerce")
    return pd.DataFrame({
        "IDADEminutos": valor.where(unidade == "0"),
        "IDADEhoras": valor.where(unidade == "1"),
        "IDADEdias": valor.where(unidade == "2"),
        "IDADEmeses": valor.where(unidade == "3"),
        "IDADEanos": valor.where(unidade == "4").fillna((valor + 100).where(unidade == "5")),
    })


def processar(df, tabelas=None):
    """Decodifica as colunas conhecidas de `df` (texto) como `process_sim()` do microdatasus.

    `tabelas` (opcional): dict {nome: DataFrame} com as tabelas auxiliares do pacote R
    (tabCBO, tabMun, tabNaturalidade), cuja 1ª coluna é o código e que têm a coluna `nome`.
    Sem elas, essas colunas ficam com o código original.
    """
    tabelas = tabelas or {}
    df = df.copy()
    for col in df.columns:
        s = df[col]
        if col in TRUNCAR:
            s = s.str[:TRUNCAR[col]]
        if col in CODIGOS:
            cod = CODIGOS[col]
            s = s.map(lambda v: cod.get(v, None if col in SEM_DEFAULT else v))
        if col in NUMEROS:
            s = pd.to_numeric(s, errors="coerce")
        if col in DATAS:
            s = pd.to_datetime(s, format=DATAS[col], errors="coerce")
        df[col] = s
    for col, nome_tabela in TABELAS_EXTERNAS.items():
        if col in df.columns and nome_tabela in tabelas:
            t = tabelas[nome_tabela]
            mapa = dict(zip(t.iloc[:, 0].astype(str), t["nome"]))
            df[col] = df[col].astype(str).map(mapa)
    if "IDADE" in df.columns:
        df = df.join(decodificar_idade(df["IDADE"]))
    return df
