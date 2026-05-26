from conversor import *

def resposta_calculadora(nBits: int) -> None:
    
    print(f"Maior valor representável em {nBits} bits: ")
    calculadora(nBits)

def resposta_terminal(base_origem: int, base_destino: int, valor: str, passos: bool) -> None: 
    
    if base_origem == 10:
        
        resposta = decimal_universal(valor, base_destino, passos)

    elif base_destino == 10:

        resposta = universal_decimal(valor, base_origem, passos)

    elif base_origem == 2 and (base_destino == 16 or base_destino == 8):

        resposta = binario_ho(valor, base_destino, passos)

    elif (base_origem == 16 or base_origem == 8) and base_destino == 2:

        resposta = ho_binario(valor, base_origem, passos)

    else:
        resposta = ho(valor, base_origem, base_destino, passos)
    
    return resposta

def resposta_csv(valor: str, base_origem: str, base_destino: str) -> None:
    
    import csv
    base_origem = int(base_origem)
    base_destino = int(base_destino)

    if base_origem == 10:
        resposta = decimal_universal(valor, base_destino)

    elif base_destino == 10:
        resposta = universal_decimal(valor, base_origem)

    elif base_origem == 2 and (base_destino == 16 or base_destino == 8):
        resposta = binario_ho(valor, base_destino)

    elif (base_origem == 16 or base_origem == 8) and base_destino == 2:
        resposta = ho_binario(valor, base_origem)

    else:
        resposta = ho(valor, base_origem, base_destino)

    with open("saida.csv", "a", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo, delimiter=";")

        escritor.writerow([valor, base_origem, base_destino, resposta])
    arquivo.close()
    print("Resposta salva no arquivo 'respostas.csv' \n \n")
