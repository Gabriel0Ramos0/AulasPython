# Atividade 3

from typing import Optional

def soma(a: int, b: int) -> int:
    return a + b

# Simulação correta
resultado1 = soma(10, 5)

# Simulação de erro
resultado2 = soma(10, "5")

print(resultado1)
print(resultado2)