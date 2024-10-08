def fibonacci_sequencia(n):
    sequencia = [0,1]

    while True:
        proximo_valor = sequencia[-1] + sequencia[-2]
        if proximo_valor > n:
            break
        sequencia.append(proximo_valor)

    return sequencia

def pertence_a_fibonacci(n):
    fib_sequencia = fibonacci_sequencia(n)
    if n in fib_sequencia:
        return True
    else:
        return False
    
# Solicitar ao usuário um número
numero = int(input("Informe um número:"))

if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")