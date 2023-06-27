# valor_investido = float(input("Qual o valor investido?: "))
# rendimento_mensal = float(input("Qual o rendimento mensal (em %)?: ")) / 100
# montante_desejado = 15000
# tempo_meses = 0

# while valor_investido < montante_desejado:
#     valor_investido += valor_investido * rendimento_mensal
#     tempo_meses += 1
#     tempo_anos = tempo_meses / 12

# print(
#     f"Serão necessários aproximadamente {tempo_anos:.0f} anos para o valor investido chegar a R$ 15.000.")


# n = int(input("Digite o tamanho da matriz (n): "))
# matriz = []
# print("Digite os elementos da matriz:")
# for i in range(n):
#     linha = []
#     for j in range(n):
#         elemento = int(input(f"Elemento [{i}][{j}]: "))
#         linha.append(elemento)
#     matriz.append(linha)
# print("Matriz: ")
# for i in range(n):
#     for j in range(n):
#         print(matriz[i][j], end=" ")
#     print()
# identidade = True
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             if matriz[i][j] != 1:
#                 identidade = False
#                 break
#         else:
#             if matriz[i][j] != 0:
#                 identidade = False
#                 break
# if identidade:
#     print("A matriz é uma matriz identidade.")
# else:
#     print("A matriz não é uma matriz identidade.")


# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
# N = int(input("Digite a quantidade de livros: "))
# livros = []
# for i in range(N):
#     print(f"\nLivro {i+1}:")
#     titulo = input("Título do livro: ")
#     autor = input("Autor do livro: ")
#     ano = int(input("Ano de lançamento do livro: "))
#     livro = Livro(titulo, autor, ano)
#     livros.append(livro)
# ano_fornecido = int(input("\nDigite o ano de busca: "))
# print("\nLivros publicados antes do ano fornecido:")
# for livro in livros:
#     if livro.ano < ano_fornecido:
#         print("-----")
#         print(f"Título: {livro.titulo}")
#         print(f"Autor: {livro.autor}")
#         print(f"Ano de lançamento: {livro.ano}")
#         print("-----")

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


N = int(input("Digite a quantidade de alunos: "))

alunos = []
maior_nota = -1
aluno_maior_nota = None
soma_notas = 0

for i in range(N):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    aluno = Aluno(nome, nota)
    alunos.append(aluno)

    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = aluno.nome
    soma_notas += nota

media_notas = soma_notas / N

print("Aluno com a maior nota:")
print("Nome:", aluno_maior_nota)
print("Nota:", maior_nota)
print("")
print("Média das notas:", media_notas)

print("\nAlunos com nota acima da média:")
for aluno in alunos:
    if aluno.nota > media_notas:
        print("Nome:", aluno.nome)
        print("Nota:", aluno.nota)
        print("-------------------")
