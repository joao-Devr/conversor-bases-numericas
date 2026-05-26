import random
from conversor import *
from formatador import resposta_terminal

def gera_numero(tamanho: int, permitidos) -> str:
    
    numero_pergunta: str = ''

    for i in range(0, tamanho):
        numero_pergunta = random.choice(permitidos) + numero_pergunta 

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
    
    trecho_permitido: int = base_origem
    if base_origem == 16 and dificuldade <= 2:
        trecho_permitido = 10
    
    permitidos = tabela_hexadecimal[:2]
    numero_pergunta: str = gera_numero(tamanho, permitidos)   
    while numero_pergunta[0] == '0':
        numero_pergunta = numero_pergunta[1:]
        if numero_pergunta == '':
            numero_pergunta = gera_numero(tamanho, permitidos)
    if base_origem != 2:
        numero_pergunta = resposta_terminal(2, base_origem, numero_pergunta, False)

    resposta_certa: str = resposta_terminal(base_origem, base_destino, numero_pergunta, False)
    acerto_erro: int = 0
    print (resposta_certa)
    print(f"Converta o número {numero_pergunta} na base {base_origem}, para base {base_destino}.")
    resposta: str= input("Insira a resposta: ")
    while resposta != resposta_certa and tentativas != 0: 
        print(f"Errado, você tem mais {tentativas} tentativas")
        resposta = input("Insira a resposta: ")
        tentativas = tentativas - 1

    if resposta == resposta_certa:
        acerto_erro = 1

    return base_origem, acerto_erro

base_anterior = 0
acerto_erro = [0, 0, 0, 0, 0]
for i in range(0, 5):
    base_anterior, acerto_erro[i] = quiz_questao(3, base_anterior)

print(acerto_erro)
