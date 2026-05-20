from conversor import *

def resposta_terminal(base_origem: str, base_destino: str, valor: str) -> None:

    if int(base_origem) == 10:
        resposta = decimal_universal(valor, int(base_destino))
        print(f"Resposta: {resposta} \n \n")   

    if int(base_destino)==10:
        resposta = universal_decimal(valor, int(base_origem))
        print(f"Resposta: {resposta} \n \n")

    if (int(base_origem) == 2 and int(base_destino) == 16) or (int(base_origem) == 16 and int(base_destino) == 2):
        resposta = binario_hexa(valor, int(base_origem))
        print(f"Resposta: {resposta} \n \n")

def resposta_csv( valor: str, base_origem: str, base_destino: str) -> None:
    import csv

    if int(base_origem) == 10:
            resposta = decimal_universal(valor, int(base_destino))
            
    if int(base_destino)==10:
        resposta = universal_decimal(valor, int(base_origem))
    
    if (int(base_origem) == 2 and int(base_destino) == 16) or (int(base_origem) == 16 and int(base_destino) == 2):
        resposta = binario_hexa(valor, int(base_origem))

    with open("respostas.csv", "a", newline="", encoding="utf-8") as arquivo:

                escritor = csv.writer(arquivo, delimiter=";")

                escritor.writerow([valor, base_origem, base_destino, resposta])
    