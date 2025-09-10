# Calculadora de 4 operações com tratamento de erros

def calc(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/":
        if b == 0: raise ZeroDivisionError("Divisão por zero")
        return a / b
    raise ValueError("Operação inválida")

print("Calculadora (+ - * /). Digite 'sair' para encerrar.")
while True:
    exp = input("Ex: 10 * 3 → ").strip()
    if exp.lower() == "sair": break
    try:
        a_str, op, b_str = exp.split()
        a, b = float(a_str), float(b_str)
        print("Resultado:", calc(a, b, op))
    except ValueError:
        print("Formato esperado: número operação número (ex: 5 + 2)")
    except ZeroDivisionError as e:
        print("Erro:", e)
