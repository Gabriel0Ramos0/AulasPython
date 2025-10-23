from datetime import date, time, datetime

# Atividade 1

n1 = 21
n2 = 10.5
n3 = True
n4 = "Python"
n5 = None
n6 = bytes("Olá".encode('utf-8'))
n7 = bytearray('Olá', 'utf-8')

print(n1, n2, n3, n4, n5, n6, n7, sep="\n")
print("#----------------------#")
print(type(n1), type(n2), type(n3), type(n4),
      type(n5), type(n6), type(n7), sep="\n")
print("#----#------#-----#----#")

# Atividade 2 - Mutável

lista = [30, 5, 10, 20, 50]
print("Tamanho da lista:", len(lista))
print("Lista em Ordem Crecente:", sorted(lista))
print("lista em Ordem Decrescente:", sorted(lista, reverse=True))
print("#----#------#-----#----#")

# Atividade 3 - Imutável

cores = ("Azul", "Vermelho", "Verde")
print(cores[0])
print(cores.count("Vermelho"))
print(cores.index("Verde"))
print("#----#------#-----#----#")

# Atividade 4

lista2 = set([1, 2, 3, 4, 5, 4, 2])
print(lista2)
print("#----#------#-----#----#")

# Atividade 5

fixa = {
    "nome": "Gabriel",
    "idade": 22,
    "curso": "Sistemas de Informação"
}
print("Nome:", fixa["nome"])
print("Idade:", fixa["idade"])
print("Curso:", fixa["curso"])
print("#----#------#-----#----#")

# Atividade 6

date = datetime.now()

print(datetime.date(date))
print("#----#------#-----#----#")

# Atividade 7

n1 = 10
n2 = 5
soma = n1 + n2

texto1 = "A soma entre"
texto2 = "e"
texto3 = "é igual a"

mensagem = f"{texto1} {n1} {texto2} {n2} {texto3} {soma}."
print(mensagem)
