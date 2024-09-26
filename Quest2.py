def contar_letra_a(texto):
    # Converte o texto para minúsculas e conta as ocorrências da letra 'a'
    qtd_letra_a = texto.lower().count('a')
    
    # Verifica se a letra 'a' foi encontrada e exibe a quantidade
    if qtd_letra_a > 0:
        print(f"A letra 'a' aparece {qtd_letra_a} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

# Solicita a entrada de uma string ao usuário
texto_usuario = input("Informe um texto: ")

# Chama a função e exibe o resultado
contar_letra_a(texto_usuario)
