def contar_letra_a(texto):
    # Converte a string para minúsculas para contar 'a' e 'A' de forma unificada
    texto = texto.lower()
    
    # Conta quantas vezes a letra 'a' aparece
    contagem = texto.count('a')
    
    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vezes."
    else:
        return "A letra 'a' não foi encontrada na string."


texto = input("Digite uma string: ")
print(contar_letra_a(texto))