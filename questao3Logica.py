def proximo_numero(sequencia):
    if sequencia == 'a':
        # Sequência de números ímpares
        ult_numero = 7
        return ult_numero + 2
    elif sequencia == 'b':
        # Sequência geométrica
        ult_numero = 64
        return ult_numero * 2
    elif sequencia == 'c':
        # Sequência dos quadrados dos números naturais
        ult_numero = 6
        return (ult_numero + 1) ** 2
    elif sequencia == 'd':
        # Sequência dos quadrados dos números pares
        ult_numero = 8
        return (ult_numero + 2) ** 2
    elif sequencia == 'e':
        # Sequência de Fibonacci
        penultimo = 5
        ultimo = 8
        return penultimo + ultimo
    elif sequencia == 'f':
        # Sequência mista
        ult_numero = 19
        if ult_numero == 16:
            return 17
        elif ult_numero == 17 or ult_numero == 18:
            return 19
        else:
            return ult_numero + 1

# Teste das sequências
sequencias = ['a', 'b', 'c', 'd', 'e', 'f']
for seq in sequencias:
    print(f"Próximo número da sequência {seq}: {proximo_numero(seq)}")
