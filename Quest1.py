def fibonacci(n):
    # Inicia a sequência de Fibonacci
    fib_seq = [0, 1]
    
    # Gera a sequência até o número n ou maior
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    # Verifica se o número está na sequência
    if n in fib_seq:
        print(f"{n} pertence à sequência de Fibonacci.")
    else:
        print(f"{n} não pertence à sequência de Fibonacci.")

# Loop para garantir que o usuário forneça um número válido
while True:
    try:
        # Solicita um número ao usuário
        num = int(input("Por favor, informe um número: "))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        # Se a conversão falhar, pede para o usuário tentar novamente
        print("Entrada inválida! Por favor, informe um número inteiro válido.")

# Chama a função e exibe o resultado
fibonacci(num)
