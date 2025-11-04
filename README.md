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