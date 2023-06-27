import statistics
init = 0

# digitados = -1
# while init == 0:
#     valor = int(input("Digite um número inteiro: "))
#     digitados += 1
#     if (valor < 0):
#         print(f"O algoritmo termina quando se digita um número negativo.")
#         print(f"Você digitou {digitados} números positivos")
#         break

# numero = 0
# valor = 0
# while init == 0:
#     ler = int(input("Digite somente números inteiros e positivos: "))
#     numero += 1
#     valor += ler
#     media = valor / numero
#     print(f"A média desses valores é {media}")


# total_menores = 0
# total_maiores = 0
# while init == 0:
#     idade = int(input("Digite a idade de várias pessoas: "))
#     if idade < 18:
#         total_menores += 1

#     elif idade > 60:
#         total_maiores += 1

#     print(f"Número de pessoas menores de 18 anos: {total_menores}")
#     print(f"Número de pessoas menores de 18 anos: {total_maiores}")


# a = 35000
# b = 48000
# tempo = 0
# while a < b:
#     a += a * 0.03
#     b += b * 0.02
#     tempo += 1
#     if (a > b):
#         print("----------------------------------------------------------------------------------")
#         print(
#             f"Serão necessários {tempo} anos para a população da cidade A ser maior que a de B")
#         print("----------------------------------------------------------------------------------")


# while init == 0:
#     userB = int(
#         input("Digite um valor para B (B deve ser maior ou igual a 2): "))
#     userN = int(input("Digite um valor para N (N deve ser maior que 1): "))
#     if (userB >= 2):
#         if (userN > 1):
#             math = userB ** userN
#             print(f"B elevado a N = {math}")
#         else:
#             print("Não segue os critérios estabelecidos.")

#     else:
#         print("Não segue os critérios estabelecidos.")


# value = 1
# H = 0
# while init == 0:
#     n = int(input("Dê um valor para N: "))
#     for x in range(1, n+1):
#         H += value / x
#     print(H)

# N = int(input("Pense em um valor para N: "))
# final = 1
# fatorial = 1
# while final <= N:
#     fatorial *= final
#     final += 1
# print(f" O fatorial desse número é: {fatorial}")

# def calcular_mmc(num1, num2):
#     maior = max(num1, num2)
#     while True:
#         if maior % num1 == 0 and maior % num2 == 0:
#             mmc = maior
#             break
#         maior += 1
#     return mmc
# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# resultado_mmc = calcular_mmc(numero1, numero2)
# print("O mínimo múltiplo comum (MMC) entre {numero1} e {numero2} é: {resultado_mmc}")


# def calcular_mdc(num1, num2):
#     menor = min(num1, num2)
#     mdc = 1
#     for i in range(1, menor + 1):
#         if num1 % i == 0 and num2 % i == 0:
#             mdc = i
#     return mdc
# numero1 = int(input("Digite o primeiro número: "))
# numero2 = int(input("Digite o segundo número: "))
# resultado_mdc = calcular_mdc(numero1, numero2)
# print(f"O máximo divisor comum (MDC) entre {numero1} e {numero2} é: {resultado_mdc}")


# num_quadros = 64
# grãos = 1
# total_graos = 1
# for i in range(2, num_quadros + 1):
#     grãos *= 2
#     total_graos += grãos
# resultado = total_graos
# print(f"O monge espera receber um total de {resultado} grãos de trigo.")

# lista_notas = []
# media_notas = 0
# variavel = 0
# for i in range(1, 51):
#     notas = int(input("Digite a nota {i}: "))
#     media_notas += notas
#     variavel += 1
#     media = media_notas / variavel
#     lista_notas.append(notas)
#     lista_notas.sort(key=int)
#     acima_media = 0
#     abaixo_media = 0
#     for nota in lista_notas:
#         if nota > media * 1.1:  # 10% acima da média
#             acima_media += 1
#         elif nota < media * 0.9:  # 10% abaixo da média
#             abaixo_media += 1
# print(f"Notas acima da média: {acima_media}")
# print(f"Notas abaixo da média: {abaixo_media}")


# alturas = []
# for i in range(1, 51):
#     altura = float(input(f"Digite a altura {i}: "))
#     alturas.append(altura)
# media = sum(alturas) / len(alturas)
# desvio_padrao = statistics.stdev(alturas)
# moda = statistics.mode(alturas)
# mediana = statistics.median(alturas)
# print("Resultados:")
# print(f"Média das alturas: {media}")
# print(f"Desvio padrão das alturas: {desvio_padrao}")
# print(f"Moda das alturas: {moda}")
# print(f"Mediana das alturas: {mediana}")

# vetor_original = []

# for i in range(1, 13):
#     numero = int(input(f"Digite o número {i}: "))
#     vetor_original.append(numero)

# vetor_impar = []

# for i in range(len(vetor_original)):
#     if (i + 1) % 2 != 0:
#         vetor_impar.append(vetor_original[i])

# print("Vetor original:", vetor_original)
# print("Vetor com elementos das posições ímpares:", vetor_impar)

# def calcular_coeficiente_binomial(n, k):
#     if k == 0 or k == n:
#         return 1
#     else:
#         return calcular_coeficiente_binomial(n - 1, k - 1) + calcular_coeficiente_binomial(n - 1, k)


# def exibir_triangulo_pascal(n):
#     for linha in range(n):
#         for coluna in range(linha + 1):
#             coeficiente = calcular_coeficiente_binomial(linha, coluna)
#             print(coeficiente, end=" ")
#         print()


# n = int(input("Digite o número de linhas do Triângulo de Pascal: "))
# exibir_triangulo_pascal(n)
