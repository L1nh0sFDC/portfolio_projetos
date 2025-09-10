# Registra gastos simples em CSV e mostra resumo mensal

import csv
from datetime import datetime
from pathlib import Path

ARQ = Path("gastos.csv")

def registrar(data, categoria, descricao, valor):
    novo = [data, categoria, descricao, f"{float(valor):.2f}"]
    existe = ARQ.exists()
    with ARQ.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not existe:
            w.writerow(["data", "categoria", "descricao", "valor"])
        w.writerow(novo)

def resumo(mes_ano):
    # mes_ano no formato YYYY-MM (ex: 2025-09)
    if not ARQ.exists():
        print("Sem registros.")
        return
    total = 0.0
    por_cat = {}
    with ARQ.open(encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["data"].startswith(mes_ano):
                v = float(row["valor"])
                total += v
                por_cat[row["categoria"]] = por_cat.get(row["categoria"], 0.0) + v
    print(f"Resumo {mes_ano}")
    print("Total:", f"R$ {total:.2f}")
    for cat, v in sorted(por_cat.items(), key=lambda x: -x[1]):
        print(f" - {cat}: R$ {v:.2f}")

if __name__ == "__main__":
    print("Comandos:")
    print(" add -> data(YYYY-MM-DD) categoria descricao valor")
    print(" sum -> YYYY-MM")
    while True:
        cmd = input("> ").strip()
        if cmd == "sair": break
        if cmd.startswith("add "):
            try:
                _, data, cat, *rest = cmd.split()
                valor = rest[-1]; descricao = " ".join(rest[:-1])
                datetime.strptime(data, "%Y-%m-%d")  # valida data
                registrar(data, cat, descricao, valor); print("OK.")
            except Exception as e:
                print("Erro ao adicionar:", e)
        elif cmd.startswith("sum "):
            _, mes = cmd.split(maxsplit=1)
            resumo(mes)
        else:
            print("Use: add <data> <categoria> <descricao> <valor> | sum <YYYY-MM> | sair")
