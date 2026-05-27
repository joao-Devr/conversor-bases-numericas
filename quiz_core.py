import random
from conversor import *
from formatador import resposta_terminal

def gera_numero(tamanho: int, permitidos, depois_virgula: bool) -> str:
    
    numero_pergunta: str = ''

    for i in range(0, tamanho):
        numero_pergunta = random.choice(permitidos) + numero_pergunta 
    
    indice_remover: int = 0
    inicio = 1
    fim = len(numero_pergunta)

    if depois_virgula == True:
        indice_remover = -1
        inicio = 0
        fim = -1

    while numero_pergunta[indice_remover] == '0':
        numero_pergunta = numero_pergunta[inicio:fim]
        if numero_pergunta == '':
            numero_pergunta = gera_numero(tamanho, permitidos, depois_virgula)

    
    return numero_pergunta

def quiz_questao(dificuldade: int, base_anterior: int):
    
    tamanho: int = 3
    
    # Não precisa de elif, porque ele vai aumentando conforme a dificuldade aumenta.
    if dificuldade == 2:
        tamanho = tamanho + 1

    if dificuldade >= 3:
        tamanho = tamanho + 4

    if dificuldade == 5:
        tamanho = tamanho + 4

    # Não precisa de elif, porque ele vai diminuindo conforme a dificuldade aumenta
    tentativas: int = 2

    if dificuldade == 4:
        tentativas = tentativas - 1
    if dificuldade == 5:
        tentativas = tentativas - 1

    bases = [2, 8, 10, 16]
    if base_anterior != 0:
        bases.remove(base_anterior)

    base_origem: int = 0
    base_origem: int = random.choice(bases)
    bases.remove(base_origem)
    
    base_destino: int = 0 
    base_destino: int = random.choice(bases)
    
    permitidos = tabela_hexadecimal[:2]
    numero_pergunta_antes_virgula: str = gera_numero(tamanho, permitidos, False)
    numero_pergunta_depois_virgula: str = ''
    
    if dificuldade >= 4:
        numero_pergunta_depois_virgula = '.' + gera_numero(4, permitidos, True)
    
    numero_pergunta: str = numero_pergunta_antes_virgula + numero_pergunta_depois_virgula

    if base_origem != 2:
        numero_pergunta = resposta_terminal(2, base_origem, numero_pergunta, False)


    resposta_certa: str = resposta_terminal(base_origem, base_destino, numero_pergunta, False)
    acerto_erro: int = 0
    print(f"Converta o número {numero_pergunta} na base {base_origem}, para base {base_destino}.")
    resposta: str= input("Insira a resposta: ")
    while resposta != resposta_certa and tentativas != 0: 
        print(f"Errado, você tem mais {tentativas} tentativas")
        resposta = input("Insira a resposta: ")
        tentativas = tentativas - 1

    if resposta == resposta_certa:
        acerto_erro = 1

    return base_origem, acerto_erro

def quiz_start(dificuldade: int, quantidade: int) -> int:
    pontuacao: int = 0
    acertos_erros: list[int] = []

    for i in range(0, quantidade):
        base_anterior = 0
        acerto_erro: int = 0
        base_anterior, acerto_erro = quiz_questao(dificuldade, base_anterior)
        acertos_erros.append(acerto_erro)

    pontuacao = sum(acertos_erros)

    return pontuacao
