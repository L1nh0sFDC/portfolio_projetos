# To-Do List simples salvando em arquivo texto

from pathlib import Path

ARQ = Path("tarefas.txt")

def carregar():
    if ARQ.exists():
        return [linha.strip() for linha in ARQ.read_text(encoding="utf-8").splitlines() if linha.strip()]
    return []

def salvar(tarefas):
    ARQ.write_text("\n".join(tarefas), encoding="utf-8")

def listar(tarefas):
    if not tarefas: print("Sem tarefas.")
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. {t}")

print("To-Do List: add <tarefa>, rm <nº>, ls, sair")
tarefas = carregar()

while True:
    cmd = input("> ").strip()
    if cmd == "sair":
        salvar(tarefas); print("Salvo. Até mais!"); break
    elif cmd == "ls":
        listar(tarefas)
    elif cmd.startswith("add "):
        tarefas.append(cmd[4:].strip()); salvar(tarefas); print("Adicionada.")
    elif cmd.startswith("rm "):
        try:
            idx = int(cmd[3:]) - 1
            removida = tarefas.pop(idx)
            salvar(tarefas); print("Removida:", removida)
        except (ValueError, IndexError):
            print("Informe um número válido (ls para ver índices).")
    else:
        print("Comandos: add <tarefa> | rm <nº> | ls | sair")
