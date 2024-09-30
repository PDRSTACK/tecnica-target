def is_fibonacci(num):
    # Função para calcular a sequência de Fibonacci até ultrapassar o número informado
    fibonacci_sequencia = [0, 1]
    
    while fibonacci_sequencia[-1] < num:
        next_value = fibonacci_sequencia[-1] + fibonacci_sequencia[-2]
        fibonacci_sequencia.append(next_value)
    
    # Verifica se o número está na sequência
    if num in fibonacci_sequencia:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."


num = int(input("Informe um número: "))
print(is_fibonacci(num))
