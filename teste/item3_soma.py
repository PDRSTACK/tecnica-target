def calcular_soma():
    INDICE = 12
    SOMA = 0
    K = 1

    while K < INDICE:
        K += 1
        SOMA += K

    return SOMA

# Resultado final
print(f"O valor final de SOMA é: {calcular_soma()}")
