from typing import Callable
from abc import ABC, abstractmethod

# Atividade 1
def soma(a: int, b: int) -> int:
    return a + b

print(soma(10, 15))
print("#----#------#-----#----#")


# Atividade 2
def subtracao(a: int, b: int) -> int:
    return a - b

print(subtracao(15, 10))
print("#----#------#-----#----#")


# Atividade 3
def multiplicacao(a: int, b: int) -> int:
    return a * b

print(multiplicacao(2, 10))
print("#----#------#-----#----#")


# Atividade 4
def divisao(a: int, b: int) -> int:
    return a / b

print(divisao(20, 2))
print("#----#------#-----#----#")


# Atividade 5
def misto(a: int, b: int, funcao: Callable[[int, int], int]) -> int:
    return funcao(a, b)

print(misto(10, 10, soma))
print(misto(10, 10, subtracao))
print(misto(10, 10, multiplicacao))
print(misto(10, 10, divisao))
print("#----#------#-----#----#")


# Atividade 6
def operacao(a: int | float, b: int | float) -> float:
    return a + b

print(operacao(5.2, 5.5))
print("#----#------#-----#----#")


# Atividade 7
class InstrumentoMusical(ABC):
    def __init__(self, nome: str):
        self.nome: str = nome

    @abstractmethod
    def tocar(self):
        pass


class Violao(InstrumentoMusical):
    def tocar(self):
        print(f"{self.nome}: dedilhando as cordas")


class Guitarra(InstrumentoMusical):
    def tocar(self):
        print(f"{self.nome}: solo elétrico rasgando o ar")


class Baixo(InstrumentoMusical):
    def tocar(self):
        print(f"{self.nome}: groove pesado ecoando no ambiente")


class Piano(InstrumentoMusical):
    def tocar(self):
        print(f"{self.nome}: acordes suaves ao toque das teclas")


class Bateria(InstrumentoMusical):
    def tocar(self):
        print(f"{self.nome}: batidas poderosas no bumbo e caixa")


instrumentos: list[InstrumentoMusical] = [
    Violao("Violão Clássico"),
    Guitarra("Guitarra Fender"),
    Baixo("Baixo Jazz"),
    Piano("Piano Yamaha"),
    Bateria("Bateria Pearl"),
    Violao("Violão Folk"),
    Guitarra("Guitarra Gibson"),
    Baixo("Baixo Precision"),
    Piano("Piano Steinway"),
    Bateria("Bateria Eletrônica")
]

print("Tocando os instrumentos musicais:\n")
for instrumento in instrumentos:
    instrumento.tocar()
print("#----#------#-----#----#")


# Atividade 8
class Veiculo(ABC):
    def __init__(self, modelo: str):
        self.modelo: str = modelo

    @abstractmethod
    def mover(self):
        pass


class Carro(Veiculo):
    def mover(self):
        print(f"{self.modelo}: acelera pelas estradas")


class Moto(Veiculo):
    def mover(self):
        print(f"{self.modelo}: corta o vento em duas rodas")


class Bicicleta(Veiculo):
    def mover(self):
        print(f"{self.modelo}: pedala pela ciclovia")


class Aviao(Veiculo):
    def mover(self):
        print(f"{self.modelo}: decola pelos céus")


class Barco(Veiculo):
    def mover(self):
        print(f"{self.modelo}: navega tranquilo sobre as ondas")


veiculos: list[Veiculo] = [
    Carro("Tesla Model 3"),
    Moto("Yamaha MT-07"),
    Bicicleta("Caloi 10"),
    Aviao("Boeing 747"),
    Barco("Lancha Veloz"),
    Carro("Fiat Uno"),
    Moto("Harley Davidson"),
    Bicicleta("Bike Elétrica"),
    Aviao("Caça F-22"),
    Barco("Submarino Azul")
]

print("\nMovendo os veículos:\n")
for veiculo in veiculos:
    veiculo.mover()
print("#----#------#-----#----#")