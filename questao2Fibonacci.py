def fibonacci_sequencia():
    fib = [0,1]
    while True:
        proximo = fib[-1] + fib[-2]
        fib.append(proximo)
        yield proximo
    
def verifica_pertencimento(numero, sequencia):
    for num in sequencia:
        if num >= numero:
            return f"\n O número {numero} pertence à sequência de Fibonacci."
    return f"\n O número {numero} não pertence à sequência de Fibonacci."
    
numero = int(input("\n Digite um número para verificar se pertence à sequência de Fibonacci: "))
sequencia_fibonacci = fibonacci_sequencia()
mensagem = verifica_pertencimento(numero, sequencia_fibonacci)
print(mensagem)