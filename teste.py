def mdc(a, b):
    """Calcula o máximo divisor comum (MDC) usando o Algoritmo de Euclides."""
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a, b):
    """Calcula o mínimo múltiplo comum (MMC) usando o MDC."""
    return abs(a * b) // mdc(a, b)

# Testes
print(mmc(10, 2))  # Saída esperada: 10
print(mmc(6, 4))   # Saída esperada: 12
print(mmc(303, 27))  # Saída esperada: 909
