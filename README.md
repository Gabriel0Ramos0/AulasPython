# 🐍 Jornada Python – Registro de Aulas

Bem-vindo(a) ao repositório da **Jornada Python**!  
Aqui está reunido todo o conteúdo das aulas, anotações, exercícios e projetos desenvolvidos durante o aprendizado da linguagem Python.  

## 📖 Introdução ao Python

O **Python** é uma linguagem de programação de alto nível, versátil e poderosa. Criada por **Guido van Rossum** em 1991, rapidamente ganhou popularidade por sua **simplicidade, clareza e legibilidade**, tornando-se uma das linguagens mais utilizadas do mundo.  

- 🔹 Foco em código limpo e legível  
- 🔹 Comunidade ativa e extensa biblioteca padrão  
- 🔹 Multi-paradigma: suporta **programação estruturada, orientada a objetos e funcional**  
- 🔹 Usado em diversas áreas: **desenvolvimento web, ciência de dados, automação, inteligência artificial, jogos, análise de dados, machine learning** e muito mais  

Python é uma das ferramentas mais importantes para quem quer criar soluções inovadoras, seja em projetos pessoais ou profissionais.  

# 📚 Branch de Aulas – Jornada Python

Cada pasta representa uma aula, contendo materiais, exemplos de código e anotações correspondentes.  

## Estrutura de Pastas

- [**1a-aula-introducao-python**](https://github.com/Gabriel0Ramos0/AulasPython/tree/main/1a-aula) *(instalação e primeiros passos com Python)*  
  <details>
    <summary>preparação de ambiente</summary>

    1. Baixar e instalar o Python:  
       - Site oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
       - Baixe a versão estável mais recente.  

    2. Configurar no Windows:  
       - Durante a instalação, marque a opção **"Add Python to PATH"**.  
       - Caso esqueça, adicione manualmente nas variáveis de ambiente:  
         ```
         C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python3X\
         C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python3X\Scripts\
         ```

    3. Testar instalação:  
       ```bash
       python --version
       ```  
       ou  
       ```bash
       py --version
       ```  
       ✅ Deve retornar algo como `Python 3.12.3`.  

    4. Acessar o interpretador interativo (REPL):  
       ```bash
       python
       ```  
       Vai aparecer:  
       ```
       >>>
       ```  
       Agora já é possível rodar comandos diretamente.  

    5. Executar scripts `.py`:  
       - Crie um arquivo chamado `primeiro.py` com:  
         ```python
         print("Olá, Python!")
         ```  
       - Rode no terminal:  
         ```bash
         python primeiro.py
         ```  

    Documentação:  
    - [Python Docs](https://docs.python.org/3/)  
    - [Python Tutorial – W3Schools](https://www.w3schools.com/python/)  
  </details>

  <details>
    <summary>atividades</summary>

    1. Mostre na tela a frase:  
       ```python
       print("Olá, mundo!")
       ```
    2. Crie uma variável chamada **nome** e armazene seu nome. Mostre com `print(nome)`.  
    3. Some dois números fixos (ex: `7 + 3`) e mostre o resultado.  
    4. Use `input()` para perguntar o nome do usuário e mostre uma saudação.  
    5. Altere o valor de uma variável após imprimir e mostre o novo valor.  
    6. Crie uma variável **curso** com o nome de um curso e mostre:  
       `"Você está aprendendo <curso>"`.  
    7. Crie duas variáveis com notas e calcule a soma.  
    8. Crie três variáveis: **nome, idade e cidade**, e exiba tudo numa frase só.  

  </details>
- [**2a-aula-python-loops-condicionais**](#) *(controle de fluxo, loops, condicionais e coleções)*  
  <details>
    <summary>preparação e conceitos</summary>

    🔁 **Controle de Fluxo em Python**  
    - ✅ Condicionais: if, else, elif  
    - 🔁 Loops: for, while  
    - ⚖️ Escopo e indentação (padrão: 4 espaços)  

    **Operadores Condicionais**  
    ```python
    valor1 = 1
    valor2 = 2
    print(valor1 == valor2)  # Igual
    print(valor1 != valor2)  # Diferente
    print(valor1 > valor2)   # Maior
    print(valor1 < valor2)   # Menor
    print(valor1 >= valor2)  # Maior ou igual
    print(valor1 <= valor2)  # Menor ou igual
    ```

    **Operadores Lógicos**  
    - `and` → E  
    - `or` → OU  
    - `not` → NÃO  
    ```python
    v1 = True
    v2 = False
    print(v1 and v2)  # False
    print(v1 or v2)   # True
    print(not v1)     # False
    ```

    **Estruturas Condicionais**  
    ```python
    idade = 20
    if idade < 18:
        print("Menor de idade")
    elif idade < 60:
        print("Adulto")
    else:
        print("Idoso")
    ```

    **Indentação**  
    - Define blocos de código em Python  
    - Erros comuns: `IndentationError`  
    ```python
    if True:
        print("Dentro do if")
        if True:
            print("Bloco interno")
    print("Fora dos blocos")
    ```

  </details>

  <details>
    <summary>loops e iterações</summary>

    **For**  
    ```python
    for i in range(3):
        print(i)  # 0, 1, 2
    nomes = ["Ana", "Bruno", "Carlos"]
    for nome in nomes:
        print(nome)
    for i, nome in enumerate(nomes):
        print(i, nome)
    ```

    **While**  
    ```python
    i = 0
    while i < 3:
        print(i)
        i += 1
    else:
        print("while é false")
    ```

    **Break e Continue**  
    ```python
    for i in range(5):
        if i == 2:
            continue  # pula o 2
        if i == 4:
            break     # para no 4
        print(i)
    ```

    **Iterando coleções**  
    - **Listas**: ordenada, mutável  
    - **Tuplas**: ordenada, imutável  
    - **Sets**: não ordenado, sem duplicados  
    - **Dicionários**: chave:valor, mutável  
    ```python
    frutas = ['maçã', 'banana', 'laranja']
    frutas.append('uva')
    frutas.sort()
    alunos = {'nome': 'João', 'idade': 20}
    for key, value in alunos.items():
        print(key, value)
    ```

  </details>

  <details>
    <summary>variáveis e tipos de dados</summary>

    **Tipos Nativos**  
    - `None` → Sem valor  
    - `int`, `float`, `complex` → Números  
    - `bool` → True/False  
    - `str` → Texto  
    - `bytes`, `bytearray`, `memoryview` → Dados binários  

    **Exemplos**  
    ```python
    nome = 'Maria'
    idade = 30
    salario = 3500.99
    ativo = True
    mensagem = f'{nome} tem {idade} anos'
    print(mensagem.upper())
    print(len(mensagem))
    ```

    **Coleções**  
    - Listas (`list`): mutável, ordenada  
    - Tuplas (`tuple`): imutável, ordenada  
    - Sets (`set`): não ordenado, sem duplicados  
    - Dicionários (`dict`): chave:valor  
    ```python
    frutas = ['maçã', 'banana']
    frutas.append('laranja')
    alunos = {'nome': 'Carlos', 'idade': 20}
    alunos['curso'] = 'Python'
    ```

    **Data e hora**  
    ```python
    from datetime import date, time, datetime
    d1 = date(2024, 7, 5)
    t1 = time(14, 30, 25)
    dt = datetime(2024, 7, 5, 14, 30, 25)
    print(d1, t1, dt)
    ```

  </details>

   <details>
    <summary>atividades – variáveis e tipos</summary>

    1. 🔢 Crie variáveis dos tipos: `int`, `float`, `bytearray` e use `print()`.  
       Também use `bool`, `str`, `None` e `type()` para cada variável.  

    2. 📦 Crie e uma **lista** com 5 números e exiba:  
       - Tamanho (`len()`)  
       - Ordem crescente (`sort()`)  
       - Ordem decrescente (`sort(reverse=True)`)  

    3. 🎨 Crie uma **tupla** com 3 cores. Acesse os elementos e use `.count()` e `.index()`.

    4. 🔹 Crie um **set** com elementos repetidos e mostre que duplicados são ignorados.  

    5. 🗂 Crie um **dicionário** com `nome`, `idade` e `curso` e acesse os dados.  

    6. 📅 Crie uma **data** usando `datetime.date()` e exiba no console.  

    7. ➕ Some duas variáveis numéricas e concatene duas strings usando **f-string**.  

  </details>

  <details>
    <summary>atividades – loops e condicionais</summary>

    1. 🔢 Informe dois valores numéricos e determine se é **maior, menor ou igual**:  
       - Maior: `'Valor X é maior que valor Y'`  
       - Menor: `'Valor X é menor que valor Y'`  
       - Igual: `'Os valores de X e Y são iguais'`  
       - Use `input()` para informar os valores e `print()` para mostrar o resultado.  

    2. 📝 Informe dois valores de texto e determine se são **iguais ou diferentes**:  
       - Igual: `'Os valores informados são iguais'`  
       - Diferente: `'Valor X é diferente do valor Y'`  

    3. 👨🧓 Escreva um `if/elif/else` que verifica a idade e imprime se é:  
       - Menor  
       - Adulto  
       - Idoso  

    4. 🔁 Faça um loop `for` imprimindo os valores de 1 até 10 em sequência.  

    5. 🔄 Faça um loop `while` imprimindo os valores de 1 até 10 em sequência.  

    6. 🗃️ Dada a lista de dados:  
       ```python
       dados = {'a': 'primeiro', 'b': 'segundo', 'c': 'terceiro', 'd': 'quarto', 'e': 'quinto'}
       ```  
       Imprima: **índice, chave e valor** de cada item.  

    7. 📋 Dada a lista:  
       ```python
       numeros = [9, 25, 5, 6, 5815, 985, 1, 22, 2, 7, 3]
       ```  
       Imprima **somente os valores 1, 2, 5 e 6**, exatamente nessa ordem.  
       Use **loops** e **listas** para filtrar e exibir.  

  </details>
- [**3a-aula-funções-classes-python**](https://github.com/Gabriel0Ramos0/AulasPython/tree/main/3a-aula) *(funções, métodos e classes em Python)*  
  <details>
    <summary>funções e classes</summary>

    ### 🔧 Funções
    - 🏗️ Classes
    - 🗄️ Introdução a objetos
    - 🧰 Métodos
    - 🔧 Funções

    ### ✏️ Definição de Função com `pass`
    ```python
    def minha_funcao():
        pass
    minha_funcao()

    def minha_funcao():
        print('Executa algo')
    ```

    ### 🔁 Função com Retorno e Parâmetros
    ```python
    def minha_funcao_com_retorno():
        return 'Retorno da função'

    print(minha_funcao_com_retorno())

    def saudacao(nome, mensagem):
        return f"{mensagem}, {nome}!"

    print(saudacao("Alice", "Bom dia"))

    def somar(valor1, valor2):
        return valor1 + valor2

    print(somar(5, 10))

    def saudacao(nome, mensagem="Olá"):
        return f"{mensagem}, {nome}!"
    ```

    ### 🎯 Posicional vs Nomeado
    ```python
    print(saudacao("Alice"))
    print(saudacao("Pedro", "Bom dia"))

    def somar(a, b, c):
        return a + b + c

    print(somar(5, 10, 3))
    print(somar(b=10, a=5, c=3))
    ```

    ### 🔢 Parâmetros Variados (`*args`)
    ```python
    def soma_tudo(*args):
        return sum(args)

    print(soma_tudo(1, 2, 3, 4))
    ```

    ### 📦 Parâmetros Nomeados (`**kwargs`)
    ```python
    def imprime_informacoes(**kwargs):
        for chave, valor in kwargs.items():
            print(f"{chave}: {valor}")

    imprime_informacoes(nome="Alice", idade=30)
    ```

    ### 💡 Múltiplos Tipos de Parâmetros
    ```python
    def exemplo(valor, *args, **kwargs):
        print(valor, args, kwargs)

    exemplo('Início', 1, 2, a=3, b=4)
    ```

    ---

    ## 🏗️ Classes e Objetos

    ### 📐 Definição
    Classes são a base da **Programação Orientada a Objetos (OOP)**.  
    Encapsulam dados (*atributos*) e funções (*métodos*).  
    Uma classe define um "molde" para os objetos, especificando propriedades e comportamentos.

    ```python
    class Pessoa:
        pass

    p = Pessoa()
    ```

    ### 🔍 Atributos e 🧰 Métodos
    ```python
    class Usuario:
        nome = None
        ativo = True

    p = Usuario()
    print(p.nome, p.ativo)
    ```

    ### 🔄 `__init__` : Construtor e Atributos
    ```python
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

    p = Pessoa("João", 30)
    print(p.nome, p.idade)
    ```

    ### ✍️ `__str__`, ✅ `__eq__` e 🗑️ `__del__`
    ```python
    class Livro:
        def __init__(self, titulo, autor):
            self.titulo = titulo
            self.autor = autor

        def __str__(self):
            return f"{self.titulo} - {self.autor}"

    print(Livro("Python", "Guido"))
    ```

    ```python
    class Livro:
        def __init__(self, titulo):
            self.titulo = titulo

        def __eq__(self, outro):
            return self.titulo == outro.titulo

    l1 = Livro("Python")
    l2 = Livro("Python")
    print(l1 == l2)
    ```

    ```python
    class MinhaClasse:
        def __del__(self):
            print("Objeto deletado")

    obj = MinhaClasse()
    del obj
    ```

    ### 🧠 Método de Instância
    ```python
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade

        def maior_de_idade(self):
            return self.idade >= 18

    p = Pessoa("Maria", 17)
    print(p.maior_de_idade())
    ```

    ### 🏛️ Método de Classe (`@classmethod`)
    ```python
    class Exemplo:
        contador = 0

        def __init__(self):
            Exemplo.contador += 1

        @classmethod
        def total_instancias(cls):
            return cls.contador

    obj1 = Exemplo()
    obj2 = Exemplo()
    obj3 = Exemplo()

    print(Exemplo.total_instancias())
    ```

    ### 🏦 Caso de Uso – Banco
    ```python
    class Banco:
        contas = []

        def __init__(self, titular, saldo_inicial=0):
            self.titular = titular
            self.saldo = saldo_inicial

        @classmethod
        def adicionar_conta(cls, titular, saldo_inicial=0):
            nova_conta = cls(titular, saldo_inicial)
            cls.contas.append(nova_conta)
            return nova_conta

        @classmethod
        def mostrar_contas(cls):
            for conta in cls.contas:
                print(f"Titular: {conta.titular}, Saldo: {conta.saldo}")

    Banco.adicionar_conta("Alice", 1000)
    Banco.adicionar_conta("Bob", 500)
    Banco.mostrar_contas()
    ```

    ### 🧰 Métodos Estáticos (`@staticmethod`)
    ```python
    class Matematica:
        @staticmethod
        def somar(a, b):
            return a + b

        @staticmethod
        def subtrair(a, b):
            return a - b

    print(Matematica.somar(3, 4))
    print(Matematica.subtrair(10, 5))
    ```
  </details>
  <details>
    <summary>atividades</summary>

    1. ➕ Crie uma função que some dois números.
    2. ➖ Crie uma função que diminua dois números.
    3. ✖ Crie uma função que multiplique dois números. 
    4. ➗ Crie uma função que divida dois números.
    5. 🔢 Crie uma função que some um número indeterminado de números.
    6. ⚙️ Crie uma classe com 4 métodos estáticos, um para cada operação matemática básica (+, -, *, /).
    7. 🧮 Crie uma classe com uma variável global de valor fixo **10** e métodos **dobra_valor()** e **triplica_valor()**, que retornem o dobro e o triplo do valor, respectivamente. 
    8. 🎓 Crie uma classe Aluno com os atributos: **nome**, **cpf**, **idade**, **telefone**, **email=None**, **ativo=True**. 
    - O método __init__ deve controlar os campos obrigatórios e opcionais, e um método deve exibir as informações formatadas como:
    ```
    Aluno: {nome} - {cpf} com idade {idade};
    Contato: {telefone} - {email}; Ativo: {ativo}
    ```

  </details>
- [**4a-aula-orientacao-a-objetos**](https://github.com/Gabriel0Ramos0/AulasPython/tree/main/4a-aula) *(Herança, Classes Abstratas, Polimorfismo e Type Hints)*  

    <details>
    <summary>Heranças e Classes</summary>

    ### 🧬 Conceitos Principais
    - **Herança:** permite que classes filhas herdem atributos e métodos de uma classe pai.  
    - **Classes Abstratas (ABC):** modelos base que não podem ser instanciados diretamente.  
    - **Polimorfismo:** diferentes classes podem implementar o mesmo método de formas distintas.  
    - **Type Hints:** adicionam tipagem opcional para variáveis, parâmetros e retornos, ajudando na leitura e validação do código.

    ### 🧮 Exemplos de Tipagem
    ```python
    valor_inteiro: int = 1
    valor_float: float = 1.78
    valor_str: str = "Texto"

    def soma(a: int, b: int) -> int:
        return a + b

    print(soma(5, 10))
    ```

    ### 🔢 Múltiplos Tipos e Tipos Compostos
    ```python
    from typing import List, Tuple, Callable

    def soma(a: int | float, b: int | float) -> float:
        return float(a + b)

    print(soma(1, 2))
    print(soma(1.55, 2.43))

    def processa_numeros(numeros: List[int]) -> Tuple[int, int]:
        return min(numeros), max(numeros)

    print(processa_numeros([1, 2, 3, 4]))

    def executar(a: int, b: int, op: Callable[[int, int], int]) -> int:
        return op(a, b)

    def multiplicar(x: int, y: int) -> int:
        return x * y

    print(executar(2, 3, multiplicar))
    ```

    ### 🧬 Herança
    ```python
    class Veiculo:
        def __init__(self, descricao):
            self.descricao = descricao

        def __str__(self):
            return self.descricao

    class Carro(Veiculo):
        def __str__(self):
            return f"Carro: {self.descricao}"

    class Moto(Veiculo):
        def __init__(self, descricao):
            super().__init__(f"Moto: {descricao}")

    print(Carro("Gol"))
    print(Moto("Biz 125"))
    ```

    ### 🔒 Classe Abstrata
    ```python
    from abc import ABC, abstractmethod

    class Animal(ABC):
        def __init__(self, nome):
            self.nome = nome

        @abstractmethod
        def fazer_som(self):
            pass

    class Cachorro(Animal):
        def fazer_som(self):
            print(f"{self.nome} está latindo.")

    class Gato(Animal):
        def fazer_som(self):
            print(f"{self.nome} está miando.")
    ```

    ### 🧪 Polimorfismo
    ```python
    from typing import List

    animais: List[Animal] = [Cachorro("Fred"), Gato("Mike")]

    for animal in animais:
        animal.fazer_som()
    ```

    ### 🖋️ Atividade Final
    ```python
    def emitir_som(animal: Animal):
        if not isinstance(animal, Animal):
            print(f"O objeto fornecido '{animal}' não é uma instância de Animal")
            return
        animal.fazer_som()

    emitir_som('Animal fake')

    animais: List[Animal] = [Cachorro("Fred"), Cachorro("Bob"), Gato("Mike")]

    for a in animais:
        emitir_som(a)
    ```
    </details>
    <details>
    <summary>atividades</summary>

    1. ➕ Soma de Inteiros
    Escreva uma função que aceite dois parâmetros do tipo `int` e retorne a **adição** deles.  
    Use *type hints* para especificar os tipos dos parâmetros e do retorno.

    2. ➖ Subtração de Inteiros
    Escreva uma função que aceite dois parâmetros do tipo `int` e retorne a **subtração** deles.  
    Use *type hints* para especificar os tipos dos parâmetros e do retorno.

    3. ✖ Multiplicação de Inteiros
    Escreva uma função que aceite dois parâmetros do tipo `int` e retorne a **multiplicação** deles.  
    Use *type hints* para especificar os tipos dos parâmetros e do retorno.

    4. ➗ Divisão de Inteiros
    Escreva uma função que aceite dois parâmetros do tipo `int` e retorne a **divisão** deles.  
    Use *type hints* para especificar os tipos dos parâmetros e do retorno.

    5. 🧮 Função Operadora
    Crie uma função que aceite **três parâmetros**: dois números inteiros e uma **função** que realiza uma operação sobre esses dois números.  
    Use *type hints* para especificar que o terceiro parâmetro é uma função que aceita dois inteiros e retorna um inteiro.  
    Chame essa função **4 vezes**, passando as funções criadas anteriormente (adição, subtração, multiplicação e divisão).

    6. 🔢 Soma Flexível
    Escreva uma função que receba dois números que podem ser do tipo `int` ou `float` e retorne a **soma** deles como `float`.  
    Use *type hints* para especificar os tipos dos parâmetros e do retorno.

    7. 🎸 Instrumentos Musicais (Classe Abstrata)
    Implemente uma classe abstrata `InstrumentoMusical` com um método abstrato `tocar`.  
    Crie cinco subclasses: `Violao`, `Bateria`, `Guitarra`, `Baixo` e `Piano`.  
    Cada uma deve implementar o método `tocar` de forma diferente.  
    Utilize *type hints* para definir os tipos de atributos e métodos.  
    Crie uma lista com **10 instrumentos musicais diferentes** e execute o método `tocar()` de cada um.

    8. 🚗 Veículos em Movimento (Classe Abstrata)
    Implemente uma classe abstrata `Veiculo` com um método abstrato `mover`.  
    Crie cinco subclasses: `Carro`, `Moto`, `Bicicleta`, `Aviao` e `Barco`, cada uma implementando `mover()` de forma diferente.  
    Utilize *type hints* para definir os tipos de atributos e métodos.  
    Crie uma lista com **10 veículos diferentes** e execute o método `mover()` de cada um.
    
    </details>