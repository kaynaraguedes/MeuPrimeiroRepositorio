# Declaração de variáveis
curso = 25
alunos = curso
curso = "Analista de Dados"
media_nota = 8.5
ativo = True
# Exibindo os valores
print(curso, alunos, ativo)

print("Digite um valor:")
teste = input()
print(type(teste))
dobro = int(teste) * 2
print("Resultado:", dobro)

idade = int(input("Sua idade: "))
print(type(idade))
print("sua idade e: ",idade)
# Agora idade é um número inteiro!

Codigo exercicio_aula.py:

nome_produto = input("Digite o nome do produto: ")

valor_produto = float(input("Digite o valor do produto: "))

produto_com_desconto = valor_produto - valor_produto * 0.10

print("O nome do produto E: ", nome_produto)

print("O valor do produto com 10% de desconto é: ", produto_com_desconto)