# Atividade 1

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

if (x > y):
    print(f"Valor {x} é maior que valor {y}.")
elif (x < y):
    print(f"Valor {x} é menor que valor {y}.")
else:
    print(f"Os valores de {x} e {y} são iguais")
print("#----#------#-----#----#")

# Atividade 2

texto1 = input("Digite a primeira palavra: ")
texto2 = input("Digite a segunda palavra: ")

if (texto1 == texto2):
    print("Os valores informados são iguais")
else:
    print(f"Valor ({texto1}) é diferente do valor ({texto2}).")
print("#----#------#-----#----#")

# Atividade 3

idade = int(input("Digite sua idade: "))

if (idade < 18):
    print("Você é menor de idade.")
elif (idade >= 18 and idade < 65):
    print("Você é adulto.")
else:
    print("Você é idoso.")
print("#----#------#-----#----#")

# Atividade 4

for i in range(1, 11):
    print(f"Número: {i}")
print("#----#------#-----#----#")

# Atividade 5
n1 = 0
while n1 < 10:
    n1 += 1
    print(f"Número: {n1}")
print("#----#------#-----#----#")

# Atividade 6

dados = {'a': 'primeiro', 'b': 'segundo', 'c': 'terceiro', 'd': 'quarto', 'e': 'quinto'}

for indice, (chave, valor) in enumerate(dados.items()):
    print(f"Índice: {indice} - Chave: {chave} - Valor: {valor}")
print("#----#------#-----#----#")

# Atividade 7

numeros = [9, 25, 5, 6, 5815, 985, 1, 22, 2, 7, 3]
valores = [1, 2, 5, 6]

lista = [num for num in numeros if num in valores]

resultadoFinal = sorted(lista)
print(f"Números encontrados: {resultadoFinal}")