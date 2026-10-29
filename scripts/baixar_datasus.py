"""Plano B da oficina: baixa os arquivos do DATASUS fora do Databricks.

Use quando o notebook não conseguir baixar nem do FTP do DATASUS nem do espelho da turma.
Rode no seu computador ou no Codespaces e envie a pasta gerada para o Volume:

    python3 scripts/baixar_datasus.py --modo rapido                  # do FTP do DATASUS
    python3 scripts/baixar_datasus.py --modo rapido --fonte github   # do espelho da turma (HTTPS)
    databricks fs cp -r volume/ dbfs:/Volumes/workspace/oficina_sus/bronze_raw/

(ou, pela interface: Catalog → workspace → oficina_sus → Volumes → bronze_raw → Upload,
 respeitando as subpastas dbc/sim, dbc/sih, dbc/sim_prelim e cid).

As listas de UFs, anos e meses são as mesmas da célula CONFIG do notebook.
"""
import argparse, os, shutil, tarfile, urllib.request
from concurrent.futures import ThreadPoolExecutor

FTP = "ftp://ftp.datasus.gov.br/dissemin/publicos"
# Espelho da turma: os mesmos .dbc brutos, em pacotes {sistema}_{UF}.tar (release dados-2026.2)
ESPELHO = "https://github.com/Escola-de-Matematica-Aplicada/dl-trajetoria/releases/download/dados-2026.2"
TODAS_UFS = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA",
             "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
MODOS = {
    "rapido":   dict(ufs=["AC", "AP", "RR"], sim=[1996, 2008, 2019, 2020, 2021, 2024], prelim=[],
                     sih=[2008, 2019, 2020, 2021, 2025], meses=[1, 7]),
    "completo": dict(ufs=TODAS_UFS, sim=list(range(1996, 2025)), prelim=[2025],
                     sih=list(range(2008, 2026)), meses=[1, 4, 7, 10]),
}


def tarefas(m):
    for uf in m["ufs"]:
        for ano in m["sim"]:
            yield f"{FTP}/SIM/CID10/DORES/DO{uf}{ano}.dbc", f"dbc/sim/DO{uf}{ano}.dbc"
        for ano in m["prelim"]:
            yield f"{FTP}/SIM/PRELIM/DORES/DO{uf}{ano}.dbc", f"dbc/sim_prelim/DO{uf}{ano}.dbc"
        for ano in m["sih"]:
            for mes in m["meses"]:
                nome = f"RD{uf}{ano % 100:02d}{mes:02d}.dbc"
                yield f"{FTP}/SIHSUS/200801_/dados/{nome}", f"dbc/sih/{nome}"
    yield "http://www2.datasus.gov.br/cid10/V2008/downloads/CID10CSV.zip", "cid/CID10CSV.zip"


def baixar(url, destino):
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        return "já existe"
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    try:
        with urllib.request.urlopen(url, timeout=300) as r, open(destino + ".part", "wb") as f:
            shutil.copyfileobj(r, f, 1 << 20)
        os.replace(destino + ".part", destino)
        return "baixado"
    except Exception as e:
        if os.path.exists(destino + ".part"):
            os.remove(destino + ".part")
        return f"FALHOU ({e})"


def do_espelho(pacote, faltam, saida):
    "Extrai de `pacote` (ex.: sih_AC.tar) só os caminhos em `faltam` (ex.: dbc/sih/RDAC0801.dbc)."
    feitos = []
    try:
        with urllib.request.urlopen(f"{ESPELHO}/{pacote}", timeout=300) as r, \
             tarfile.open(fileobj=r, mode="r|") as tar:
            for m in tar:
                if m.name in faltam:
                    destino = os.path.join(saida, m.name)
                    os.makedirs(os.path.dirname(destino), exist_ok=True)
                    with tar.extractfile(m) as src, open(destino + ".part", "wb") as f:
                        shutil.copyfileobj(src, f, 1 << 20)
                    os.replace(destino + ".part", destino)
                    feitos.append(m.name)
    except Exception as e:
        print(f"  ✗ espelho {pacote}: {e}")
    return feitos


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--modo", choices=MODOS, default="rapido")
    ap.add_argument("--saida", default="volume", help="pasta local que espelha o Volume bronze_raw")
    ap.add_argument("--fonte", choices=["ftp", "github"], default="ftp",
                    help="ftp: DATASUS · github: espelho da turma (mesmos arquivos, por HTTPS)")
    a = ap.parse_args()
    lista = list(tarefas(MODOS[a.modo]))
    if a.fonte == "github":
        lista = [(f"{ESPELHO}/CID10CSV.zip", d) if d.startswith("cid/") else (u, d) for u, d in lista]
        pacotes = {}
        for _, d in lista:
            if d.startswith("dbc/") and not os.path.exists(os.path.join(a.saida, d)):
                sistema, nome = d.split("/")[1:]
                pacotes.setdefault(f"{sistema}_{nome[2:4]}.tar", set()).add(d)
        with ThreadPoolExecutor(4) as ex:
            list(ex.map(lambda p: do_espelho(p, pacotes[p], a.saida), sorted(pacotes)))
    with ThreadPoolExecutor(4) as ex:
        res = list(ex.map(lambda t: (t[1], baixar(t[0], os.path.join(a.saida, t[1]))), lista))
    falhas = [r for r in res if r[1].startswith("FALHOU")]
    print(f"{len(res) - len(falhas)}/{len(res)} arquivos em {a.saida}/")
    for nome, st in falhas:
        print("  ✗", nome, st)
