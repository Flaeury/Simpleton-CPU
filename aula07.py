# import time
# def countdown(minutos):
#     total = minutos * 60
#     for segundos_restantes in range(total, -1, -1):
#         minutos = segundos_restantes // 60
#         segundos = segundos_restantes % 60
#         print(f"{minutos:02d}:{segundos:02d}")
#         time.sleep(0.03)
# countdown(10)


# numeros = []
# for i in range(10):
#     numero = int(input("Digite um número inteiro: "))
#     numeros.append(numero)
# numeros.reverse()
# print("Números em ordem decrescente de entrada:")
# for numero in numeros:
#     print(numero)


# soma_positivos = 0
# quantidade_negativos = 0
# for i in range(20):
#     valor = int(input("Digite um número inteiro: "))
#     if valor > 0:
#         soma_positivos += valor
#     elif valor < 0:
#         quantidade_negativos += 1
# print(f"Soma dos números positivos: {soma_positivos}")
# print(f"Quantidade de valores negativos: {quantidade_negativos}")


# lista = []
# for i in range(5):
#     valor = int(input("Digite um número inteiro e positivo: "))
#     lista.append(valor)
#     lista.sort()
# primeiro_valor = lista[0]
# ultimo_valor = lista[-2]
# print("Primeiro valor da lista:", primeiro_valor)
# print("Último valor da lista:", ultimo_valor)


# print("----------------------------------------")
# print("                CARDÁPIO                ")
# print("----------------------------------------")
# print("Especificação    Código   Preço Unitário")
# print("Cachorro Quente    100         1.20")
# print("Bauru Simples      101         1.30")
# print("Bauru com ovo      102         1.50")
# print("Hambúrguer         103         1.20")
# print("Cheeseburguer      104         1.30")
# print("Refrigerante       105         1.00")
# print("----------------------------------------")
# print("Fechar pedido      000")
# print("----------------------------------------")
# cardapio = []
# pedido_completo = 0
# while True:
#   pedido = input("Digite o código do seu pedido: ")
#   if pedido != '000':
#     match pedido:
#       case '100':
#         pedido_completo += 1.20
#         cardapio.append('Cachorro Quente')
#       case '101':
#         pedido_completo += 1.30
#         cardapio.append('Bauru Simples')
#       case '102':
#         pedido_completo += 1.50
#         cardapio.append('Bauru com ovo')
#       case '103':
#         pedido_completo += 1.20
#         cardapio.append('Hambúrguer')
#       case '104':
#         pedido_completo += 1.30
#         cardapio.append('Cheeseburguer')
#       case '105':
#         pedido_completo += 1.00
#         cardapio.append('Refrigerante')
#   elif (pedido == '000'):
#     print(f"Seus pedidos foram: {cardapio}")
#     print(f"Total a pagar: {pedido_completo}")
#     cardapio = []
#     pedido_completo = 0


# voto_branco = 0
# voto_nulo = 0
# voto_candidatoA = 0
# voto_candidatoB = 0
# voto_candidatoC = 0
# voto_candidatoD = 0
# print("--------------------")
# print("Candidato A       1")
# print("Candidato B       2")
# print("Candidato C       3")
# print("Candidato D       4")
# print("Voto Nulo         5")
# print("Voto em Branco    6")
# print("-------------------")
# print("Terminar Votação: 0")
# print("-------------------")
# while True:
#   votos = input("Qual seu voto?: ")
#   if (votos != '0'):
#     match votos:
#       case '1':
#         voto_candidatoA += 1
#       case '2':
#         voto_candidatoB += 1
#       case '3':
#         voto_candidatoC += 1
#       case '4':
#         voto_candidatoD += 1
#       case '5':
#         voto_nulo += 1
#       case '6':
#         voto_branco += 1
#   elif (votos == '0'):
#     print("-----------------------------")
#     print(f"Votos do Candidato A:  {voto_candidatoA}")
#     print(f"Votos do Candidato B:  {voto_candidatoB}")
#     print(f"Votos do Candidato C:  {voto_candidatoC}")
#     print(f"Votos do Candidato D:  {voto_candidatoD}")
#     print(f"Votos Nulos:           {voto_nulo}")
#     print(f"Votos em Branco:       {voto_branco}")
#     print("-----------------------------")
#     voto_branco = 0
#     voto_nulo = 0
#     voto_candidatoA = 0
#     voto_candidatoB = 0
#     voto_candidatoC = 0
#     voto_candidatoD = 0