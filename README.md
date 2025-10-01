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

    - Instalar o Python e configurar o ambiente corretamente.  
    - Rodar o interpretador interativo (REPL) e testar:  
      ```python
      print("Primeiro teste no REPL!")
      2 + 2
      ```  
    - Criar um arquivo `primeiro.py` com o código:  
      ```python
      print("Olá, Python!")
      ```  
    - Rodar o script no terminal com:  
      ```bash
      python primeiro.py
      ```  
    - Explicar a diferença entre **executar no REPL** e rodar um **script `.py`**.  
  </details>
