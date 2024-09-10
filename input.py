entrada = input("Digite uma sequência de letras e números: ")

# Variáveis para armazenar as letras concatenadas e a soma dos números
letras_concatenadas = ""
soma_numeros = 0

# Loop para percorrer cada caractere na entrada
for caractere in entrada:
    if caractere.isdigit():  # Verifica se o caractere é um número
        soma_numeros += int(caractere)
        print(f"Soma dos números: {soma_numeros}")

    elif caractere.isalpha():  # Verifica se o caractere é uma letra
        letras_concatenadas += caractere
        print(f"Letras concatenadas: {letras_concatenadas}")

# Exibe os resultados
