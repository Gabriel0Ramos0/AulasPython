# Atividade 1
def somar(a, b):
    return f'A soma entre {a} e {b} é igual a {a + b}.'

print(somar(10, 15))
print("#----#------#-----#----#")


# Atividade 2
def diminuir(a, b):
    return f'A subtração entre {a} e {b} é igual a {a - b}.'

print(diminuir(10, 15))
print("#----#------#-----#----#")


# Atividade 3
def multiplicar(a, b):
    return f'A multiplicação entre {a} e {b} é igual a {a * b}.'

print(multiplicar(10, 15))
print("#----#------#-----#----#")


# Atividade 4
def dividir(a, b):
    return f'A divisão entre {a} e {b} é igual a {a / b}.'

print(dividir(10, 15))
print("#----#------#-----#----#")


# Atividade 5
def somaInde(*args):
    return f'A soma dos valores {args} é igual a {sum(args)}.'

print(somaInde(5, 10, 15, 20, 25))
print("#----#------#-----#----#")


# Atividade 6
class Operacoes:

    @staticmethod
    def somar(a, b):
        return f'A soma entre {a} e {b} é igual a {a + b}.'

    @staticmethod
    def diminuir(a, b):
        return f'A subtração entre {a} e {b} é igual a {a - b}.'

    @staticmethod
    def multiplicar(a, b):
        return f'A multiplicação entre {a} e {b} é igual a {a * b}.'

    @staticmethod
    def dividir(a, b):
        return f'A divisão entre {a} e {b} é igual a {a / b}.'

print(Operacoes.somar(10, 5))
print(Operacoes.diminuir(10, 5))
print(Operacoes.multiplicar(10, 5))
print(Operacoes.dividir(10, 5))
print("#----#------#-----#----#")


# Atividade 7
n3 = 10

class OperacaoGlobal:
    def __init__(self, numero):
        self.numero = numero

    def dobra_valor(self):
        return f'O dobro de {self.numero} é igual a {self.numero * 2}.'
    
    def triplica_valor(self):
        return f'O triplo de {self.numero} é igual a {self.numero * 3}.'

obj = OperacaoGlobal(n3)
print(obj.dobra_valor() + "\n" +
      obj.triplica_valor())
print("#----#------#-----#----#")


# Atividade 8
class Aluno:
    def __init__(self, nome, cpf, idade, telefone, email=None, ativo=True):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.ativo = ativo

    def mostrar_informacoes(self):
        return (f"Aluno: {self.nome} - {self.cpf} com idade {self.idade};\n"
                f"Contato: {self.telefone} - {self.email}; Ativo: {self.ativo}")

aluno1 = Aluno("Gabriel Ramos", "123.456.789-00", 22, "(11) 99999-9999")
aluno2 = Aluno("Ana Souza", "987.654.321-00", 25, "(11) 98888-8888", "ana@email.com", False)

print(aluno1.mostrar_informacoes() + "\n")
print(aluno2.mostrar_informacoes())
print("#----#------#-----#----#")