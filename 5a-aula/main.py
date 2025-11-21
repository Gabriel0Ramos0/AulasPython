# Atividade 1
nomes = []

print("Digite nomes (ou deixe vazio para encerrar):")
while True:
    nome = input("Nome: ")
    if nome == "":
        break
    nomes.append(nome)

# Criando e escrevendo no arquivo
with open("dados.txt", "w", encoding="utf-8") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")

# Lendo e exibindo o conteúdo
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("\nConteúdo do arquivo:")
    print(arquivo.read())
print("#----#------#-----#----#")


# Atividade 2
soma = 0

try:
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            try:
                soma += float(linha.strip())
            except ValueError:
                print(f"Valor inválido ignorado: {linha.strip()}")

    print(f"Soma total: {soma}")

except FileNotFoundError:
    print("Erro: O arquivo 'numeros.txt' não foi encontrado.")
except Exception as e:
    print(f"Erro inesperado: {e}")
print("#----#------#-----#----#")