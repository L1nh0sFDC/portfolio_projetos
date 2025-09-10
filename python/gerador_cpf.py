# Gera CPFs válidos para testes (NÃO são de pessoas reais)

import random

def digito(nums):
    s = sum(v * p for v, p in zip(nums, range(len(nums)+1, 1, -1)))
    r = (s * 10) % 11
    return 0 if r == 10 else r

def gerar(formato=True):
    base = [random.randint(0, 9) for _ in range(9)]
    d1 = digito(base)
    d2 = digito(base + [d1])
    cpf = base + [d1, d2]
    if not formato:
        return "".join(map(str, cpf))
    return f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"

if __name__ == "__main__":
    for _ in range(5):
        print(gerar())
