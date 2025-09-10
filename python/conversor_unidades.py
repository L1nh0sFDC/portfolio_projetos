# Conversor de unidades simples
# Uso: rode e siga o menu no terminal

def c_para_f(c): return (c * 9/5) + 32
def f_para_c(f): return (f - 32) * 5/9
def km_para_mi(km): return km * 0.621371
def mi_para_km(mi): return mi / 0.621371
def kg_para_lb(kg): return kg * 2.20462
def lb_para_kg(lb): return lb / 2.20462

def menu():
    print("\n=== Conversor de Unidades ===")
    print("1) °C → °F")
    print("2) °F → °C")
    print("3) km → milhas")
    print("4) milhas → km")
    print("5) kg → lb")
    print("6) lb → kg")
    print("0) sair")

while True:
    menu()
    op = input("Escolha: ").strip()
    if op == "0":
        print("Até mais!")
        break
    try:
        valor = float(input("Valor: ").strip())
        if op == "1": print(f"{valor} °C = {c_para_f(valor):.2f} °F")
        elif op == "2": print(f"{valor} °F = {f_para_c(valor):.2f} °C")
        elif op == "3": print(f"{valor} km = {km_para_mi(valor):.3f} milhas")
        elif op == "4": print(f"{valor} milhas = {mi_para_km(valor):.3f} km")
        elif op == "5": print(f"{valor} kg = {kg_para_lb(valor):.3f} lb")
        elif op == "6": print(f"{valor} lb = {lb_para_kg(valor):.3f} kg")
        else: print("Opção inválida.")
    except ValueError:
        print("Digite um número válido.")
